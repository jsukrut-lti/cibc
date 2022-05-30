from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.views import View
from django.template.loader import render_to_string
from django.conf import settings
from .models import InsuranceDiscussion, InsuranceProduct, InsuranceEligibility,ProvinceResidence,OccupationMaster
from django.views.generic.detail import SingleObjectMixin
import logging
from drf_yasg.utils import swagger_auto_schema
import sys
sys.path.append('../../')
from collections import defaultdict
from django.db.models import Q
from datetime import date
import datetime
import json
# Get an instance of a logger
logger = logging.getLogger(__name__)


class CreditInsurance(object):

    insurance_api_data = None
    file_path = settings.DATA_FILE_DIR/'api_data.json'

    @classmethod
    def api_data(cls):
        with open(cls.file_path) as f:
            cls.insurance_api_data = json.load(f)
            return cls.insurance_api_data

    @staticmethod
    def calculate_age(birthDate):
        date_string = str(birthDate)
        birthDate = date(int(date_string[:4]), int(date_string[4:6]), int(date_string[6:8]))
        today = date.today()
        try:
            birthday = birthDate.replace(year=today.year)

        except ValueError:
            birthday = birthDate.replace(year=today.year,
                                         month=birthDate.month + 1, day=1)

        if birthday > today:
            return today.year - birthDate.year - 1
        else:
            return today.year - birthDate.year

    @staticmethod
    def initial_data_storage(*args, **kwargs):

        return True



class EligibilityCheck(object):

    def __init__(self, *args, **kwargs):
        self.list_credit_product = {"mortgage" : ["mortgage", "plc"], "compass" : ["loan"]}
        self.insurance_details = {}
        self.insurance_product_rec = defaultdict(list)

    def get_eligibility(self, request, *args, **kwargs):

        for key, value in kwargs.items():
            self.insurance_details[key] = value

        eligibility_flag = False
        product_details = InsuranceProduct.objects.filter(active=True).all()
        product_details_rec = product_details and list(product_details) or []

        for prod in product_details_rec:
            self.insurance_product_rec[prod.creditProduct_code.credit_product_name.lower()].append(prod.product_cibc_code)

        if "credit_product" in self.insurance_details.keys():
            if self.insurance_details["credit_product"].lower() in self.list_credit_product.keys():
                if "insurance_product_details" in self.insurance_details.keys():

                    if "insProduct_ID" in self.insurance_details["insurance_product_details"][0].keys():
                        insProduct_id = self.insurance_details["insurance_product_details"][0]["insProduct_ID"]
                        cred_prod = self.list_credit_product[self.insurance_details["credit_product"].lower()]

                        for cred in cred_prod:
                            if insProduct_id in self.insurance_product_rec[cred]:
                                eligibility_flag = True

            elif self.insurance_details["credit_product"].upper() == "ECIF":
                eligibility_flag = self.ecif_eligibility_check(request)

        return eligibility_flag

    def ecif_eligibility_check(self, request, *args, **kwargs):

        eligibility_flag = False
        occupation_id = None
        residency = None

        age = CreditInsurance.calculate_age(self.insurance_details["birth_date"])
        occupation_code = self.insurance_details["occupation_code"]
        province = self.insurance_details["province"]

        occupation_rec = OccupationMaster.objects.filter(occupation_code=occupation_code, active=True).values('id').distinct()
        occupation_rec = occupation_rec and list(occupation_rec) or []
        if occupation_rec:
            occupation_rec = occupation_rec and occupation_rec[0] or {}
            occupation_id = occupation_rec.get('id', False)

        residency_rec = ProvinceResidence.objects.filter(province=province, active=True).values('residency').distinct()
        residency_rec = residency_rec and list(residency_rec) or []
        if residency_rec:
            residency_rec = residency_rec and residency_rec[0] or {}
            residency = residency_rec.get('residency', False)

        try:
            eligible_product_count = InsuranceEligibility.objects.filter(Q(residency=residency) | Q(occupation=occupation_id),
                                                                     minAge__lte=age,maxAge__gte=age,
                                                                     effective_start_date__lte=datetime.datetime.now().date(),
                                                                     effective_end_date__gte=datetime.datetime.now().date(),
                                                                     active=True).count()

        except Exception as e:
            eligible_product_count = 0

        if eligible_product_count >= 1:
            eligibility_flag = True

        return eligibility_flag

