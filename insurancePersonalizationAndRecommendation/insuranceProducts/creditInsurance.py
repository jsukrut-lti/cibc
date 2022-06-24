from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.views import View
from django.template.loader import render_to_string
from django.conf import settings
from .models import *
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
import logging
import traceback

class CreditInsurance(object):

    insurance_api_data = None
    file_path = settings.DATA_FILE_DIR/'cibc_application_data.json'

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

        pre_data = {}

        pre_data['application_number'] = kwargs.get('application_number',False)
        pre_data['data'] = json.dumps(kwargs)
        pre_data_ID = 0

        try:
            preProecssData = InsurancePreProcessData.objects.create(**pre_data)
            preProecssData.save()
            pre_data_ID = preProecssData.pk

        except Exception as e:
            logging.getLogger("error_logger").error(traceback.format_exc())


        return pre_data_ID


    def get_agent_id(self):
        return 1

    def get_ins_product(self,prod_code):
        p = InsuranceProduct.objects.filter(product_cibc_code=prod_code)
        return p[0]

    def format_raw_data_for_insdisc(self,queryset, select):

        raw_data = json.loads(queryset['data'])
        appl_details = raw_data.get('applicants', list())

        ins_product = CreditInsurance.get_ins_product(self,raw_data['insProducts_details'][0]['insProduct_ID'])
        ins_product_type = ins_product.creditProduct_code.credit_product_name.lower()
        d = CreditInsurance.create_ins_disc_template(self, ins_product_type)
        # d = dict()
        d['preProcessData_id'] = queryset['id']
        d['insProduct_id'] = ins_product.id
        d['agent_id'] = CreditInsurance.get_agent_id(self)
        # todo - Need to change 'canada_provence' to 'canada_province' in model
        d['canada_province'] = raw_data['canada_province']
        d['currentApplicationPmt'] = raw_data['currentApplicationPmt']

        if ins_product_type == 'hpp':
            # HPP
            d['hppMaxRebalancingLmt'] = raw_data['hpp']['hppMaxRebalancingLmt']
            d['hppCreditLmt'] = raw_data['hpp']['hppCreditLmt']
            d['plcCLassNumber'] = raw_data['hpp']['plcCLassNumber']
            d['plcMMortgageNumber'] = raw_data['hpp']['plcMMortgageNumber']
            d['plcRepaymentType'] = raw_data['hpp']['plcRepaymentType']
            d['plcCreditLmt'] = raw_data['hpp']['plcCreditLmt']
            d['plcInterestRate'] = raw_data['hpp']['plcInterestRate']
            d['mortgageCLassNumber'] = raw_data['hpp']['mortgageCLassNumber']
            d['mortgageNumber'] = raw_data['hpp']['mortgageNumber']
            d['mortgageBalance'] = raw_data['hpp']['mortgageAmt']
            d['mortgagePmtAmt'] = raw_data['hpp']['mortgagePmtAmt']
            d['mortgagePmtFrequency'] = raw_data['hpp']['mortgagePmtFrequency']

        elif ins_product_type == 'loan':
            d['loanClassNumber'] = raw_data['loan']['loanClassNumber']
            d['loanAmt'] = raw_data['loan']['loanAmt']
            d['loanPmtAmt'] = raw_data['loan']['loanPmtAmt']
            d['loanPmtFrequency'] = raw_data['loan']['loanPmtFrequency']

        elif ins_product_type == 'plc':
            d['plcCLassNumber'] = raw_data['plc']['plcCLassNumber']
            d['plcMMortgageNumber'] = raw_data['plc']['plcMMortgageNumber']
            d['plcRepaymentType'] = raw_data['plc']['plcRepaymentType']
            d['plcCreditLmt'] = raw_data['plc']['plcCreditLmt']
            d['plcInterestRate'] = raw_data['plc']['plcInterestRate']

        elif ins_product_type == 'mortgage':
            d['mortgageCLassNumber'] = raw_data['mortgage']['classNumber']
            d['mortgageNumber'] = raw_data['mortgage']['mortgageNumber']
            d['mortgageBalance'] = raw_data['mortgage']['balance']
            d['mortgagePmtAmt'] = raw_data['mortgage']['pmtAmount']
            d['mortgagePmtFrequency'] = raw_data['mortgage']['pmtFrequency']

        for index, appl in enumerate(appl_details):
            if appl['applicantId'] in select:
                if index == 0:
                    d['primaryApplicantId'] = appl['applicantId']
                    d['primaryFirstName'] = appl['FirstName']
                    d['primaryMiddleName'] = appl['MiddleName']
                    d['primaryLastName'] = appl['LastName']
                    d['primaryAge'] = CreditInsurance.calculate_age(appl["birth_date"])
                    d['primaryGender'] = appl['Gender']
                    d['approxNetIncome'] = appl['monthlyGrossIncome']
                    d['totalUnsecuredAmt'] = appl['existingDebts']['cibcUnsecured']
                    d['totalSecuredAmt'] = appl['existingDebts']['cibcSecured']
                    d['totalExistingDebt'] = appl['existingDebts']['cibcSecured'] + appl['existingDebts'][
                        'cibcUnsecured']
                    d['totalMonthlyPmt'] = appl['monthlyIncomeAfterTaxes']
                    d['savingsEmergencyFund'] = appl['savingsEmergencyFund']
                    d['creditCardBalance'] = appl['creditCard']['balance']
                    d['totalMonthlyExpenses'] = appl['expenses']['totalMonthlyExpenses']
                    d['isJoint'] = 'n'
                if index == 1:
                    d['coApplicantId'] = appl['applicantId']
                    d['coFirstName'] = appl['FirstName']
                    d['coMiddleName'] = appl['MiddleName']
                    d['coLastName'] = appl['LastName']
                    d['coAge'] = CreditInsurance.calculate_age(appl["birth_date"])
                    d['coGender'] = appl['Gender']
                    d['approxNetIncome'] += appl['monthlyGrossIncome']
                    d['totalUnsecuredAmt'] += appl['existingDebts']['cibcUnsecured']
                    d['totalSecuredAmt'] += appl['existingDebts']['cibcSecured']
                    d['totalExistingDebt'] += appl['existingDebts']['cibcSecured'] + appl['existingDebts'][
                        'cibcUnsecured']
                    d['totalMonthlyPmt'] += appl['monthlyIncomeAfterTaxes']
                    d['savingsEmergencyFund'] += appl['savingsEmergencyFund']
                    d['creditCardBalance'] += appl['creditCard']['balance']
                    d['totalMonthlyExpenses'] += appl['expenses']['totalMonthlyExpenses']
                    d['isJoint'] = 'y'

        return d

    def create_ins_disc_template(self, ins_product_type):
        temp = {
            # demographics
            'primaryFirstName': '',
            'primaryMiddleName': '',
            'primaryLastName': '',
            'primaryPreferredName': '',
            'primaryAge': None,
            'primaryGender': '',
            'primaryEmail': '',
            'coFirstName': '',
            'coMiddleName': '',
            'coLastName': '',
            'coAge': None,
            'coGender': '',
            'isJoint': '',
            'canada_province': '',
            # source info
            'agent_id': None,
            'insProduct_id': None,
            'preProcessData_id': None,
            # approx net income
            'approxNetIncome': None,
            # existing debt
            'totalExistingDebt': None,
            # current application payment
            'currentApplicationPmt': None,
            # monthly payment
            'totalMonthlyPmt': None,
            # saving and emergency fund
            'savingsEmergencyFund': None,
            # current insurance coverage
            'lifeInsuranceLimit': None,
            'criticalIllnessLimit': None,
            'disabilityInsuranceMonthlyBenefit': None,
            'disabilityInsurancePercentCoveredByEmployer': None,
            # existing fields / extras
            'totalUnsecuredAmt': None,
            'totalSecuredAmt': None,
            'creditCardBalance': None,
            'totalMonthlyExpenses': None,
        }
        # current application details
        t = dict()
        if ins_product_type == 'hpp':
            # HPP
            t = {
                'hppMaxRebalancingLmt': None,
                'hppCreditLmt': None,
                'plcCLassNumber': '',
                'plcMMortgageNumber': '',
                'plcRepaymentType': '',
                'plcCreditLmt': None,
                'plcInterestRate': None,
                'mortgageCLassNumber': '',
                'mortgageNumber': '',
                'mortgageBalance': None,
                'mortgagePmtAmt': None,
                'mortgagePmtFrequency': None
                }
        elif ins_product_type == 'loan':
            t = {
                'loanClassNumber': '',
                'loanAmt': None,
                'loanPmtAmt': None,
                'loanPmtFrequency': None
            }
        elif ins_product_type == 'plc':
            t = {
                'plcCLassNumber': '',
                'plcMMortgageNumber': '',
                'plcRepaymentType': None,
                'plcCreditLmt': None,
                'plcInterestRate': None
            }
        elif ins_product_type == 'mortgage':
            t = {
                'mortgageCLassNumber': '',
                'mortgageNumber': '',
                'mortgageBalance': None,
                'mortgagePmtAmt': None,
                'mortgagePmtFrequency': None
            }
        if t:
            temp.update(t)
        return temp

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
                eligibility_applicant_list = self.ecif_eligibility_check(request)

                if eligibility_applicant_list:
                    eligibility_flag = True

        return eligibility_flag

    def ecif_eligibility_check(self, request, *args, **kwargs):

        eligibility_flag = False
        occupation_id = None
        residency = None
        eligible_applicant_list = []

        if "applicants" in self.insurance_details.keys():

            for applicant_dict in self.insurance_details['applicants']:

                age = CreditInsurance.calculate_age(applicant_dict["birth_date"])
                occupation_code = applicant_dict["occupation_code"]
                province = applicant_dict["province_residence"]


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
                    eligible_applicant_list.append(applicant_dict["applicantId"])

        return eligible_applicant_list


class AssessmentQuestionnaire(object):

    def __init__(self, *args, **kwargs):
        pass

    def assessment_data(self,request):

        assessment_detail = {}
        assessment_rec = AssessmentQuestionnaireMaster.objects.filter(effective_start_date__lte=datetime.datetime.now().date(),
                                                                 effective_end_date__gte=datetime.datetime.now().date(),
                                                                 active=True).values('assessment_id','assessment_details').all()

        assessment_rec = assessment_rec and list(assessment_rec) or []

        if assessment_rec:
            for qust in assessment_rec:
                assessment_detail[qust['assessment_id']] = qust['assessment_details']

        return assessment_detail



