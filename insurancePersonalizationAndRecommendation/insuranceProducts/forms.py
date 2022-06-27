from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from .models import InsuranceDiscussion
from enum import Enum




class INS_SHEET_SECTION_AREAS(Enum):
    primary = 'primary'
    co_borrow= 'co_borrow'
    loved_ones = 'loved_ones'
    creditProduct = 'creditProduct'
    incomeExpenseSavingsTotals = 'incomeExpenseSavingsTotals'
    expenseEstimation = 'expenseEstimation'
    savingsEstimation = 'savingsEstimation'
    otherInsurance = 'otherInsurance'
    coverageOptions = 'coverageOptions'

    @classmethod
    def get_value(cls,member):
        return cls[member]

class InsuranceDiscussionForm(ModelForm):
    formID = "unset"

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()

        # Setup Helper Info
        self.helper.form_id = 'id-{}'.format(self.formID)
        self.helper.form_method = 'post'
        self.helper.form_action = '/insurance/insConvo/{}/'.format(kwargs.get("instance").id)
        self.helper.add_input(Submit('submit', 'Submit {}'.format(self.formID.value), css_class='btn-primary'))

        super(InsuranceDiscussionForm, self).__init__(*args, **kwargs)



class TestPrimaryInsuranceDiscussionForm(ModelForm):
    class Meta:
        model = InsuranceDiscussion
        fields = ['primaryFirstName', 'primaryMiddleName', 'primaryLastName', 'primaryAge']


class PrimaryInsuranceDiscussionForm(InsuranceDiscussionForm):
    formID = INS_SHEET_SECTION_AREAS.primary

    class Meta:
        model = InsuranceDiscussion
        fields = ['primaryFirstName', 'primaryMiddleName', 'primaryLastName', 'primaryAge','canada_province','hoursWeekWorking']


class CoBorrowerInsuranceDiscussionForm(InsuranceDiscussionForm):
    formID = INS_SHEET_SECTION_AREAS.co_borrow

    class Meta:
        model = InsuranceDiscussion
        fields = ['coFirstName', 'coMiddleName', 'coLastName', 'coAge']


class LovedOnesInsuranceDiscussionForm(InsuranceDiscussionForm):
    formID = INS_SHEET_SECTION_AREAS.loved_ones
    class Meta:
        model = InsuranceDiscussion
        fields = ['hasPartnerFinResponsibility', 'hasChildrenFinResponsibility', 'hasParentsFinResponsibility', 'hasOthersFinResponsibility']

class CreditProductInsuranceDiscussionForm(InsuranceDiscussionForm):
    formID = INS_SHEET_SECTION_AREAS.creditProduct

    class Meta:
        model = InsuranceDiscussion
        fields = ['mortgageBalance', 'mortgagePmtAmt', 'mortgagePmtFrequency',]

class IncomeExpenseSvgTotalsInsuranceDiscussionForm(InsuranceDiscussionForm):
    formID = INS_SHEET_SECTION_AREAS.incomeExpenseSavingsTotals

    class Meta:
        model = InsuranceDiscussion
        fields = ['monthlyIncomeAfterTaxes', 'totalMonthlyExpenses', 'totalSavings',]


class ExpensesEstInsuranceDiscussionForm(InsuranceDiscussionForm):
    formID = formID = INS_SHEET_SECTION_AREAS.expenseEstimation

    class Meta:
        model = InsuranceDiscussion
        fields = ['monthlyExpenseOtherCredit', 'monthlyExpensePersonal', 'monthlyExpenseOtherHousing', 'monthlyExpensePropTaxFees','monthlyExpenseOther']


class SavingsEstOnesInsuranceDiscussionForm(InsuranceDiscussionForm):
    formID = INS_SHEET_SECTION_AREAS.savingsEstimation

    class Meta:
        model = InsuranceDiscussion
        fields = ['totalSavingsChequing','totalSavingsTaxFreeAccts', 'totalSavingsRegRetirement', 'totalSavingsGuarantedInvestmentCerts','totalSavingsOther', ]


class OtherInsuranceInsuranceDiscussionForm(InsuranceDiscussionForm):
    formID = INS_SHEET_SECTION_AREAS.savingsEstimation

    class Meta:
        model = InsuranceDiscussion
        fields = ['lifeInsuranceLimit','criticalIllnessLimit', 'disabilityInsuranceMonthlyBenefit', 'disabilityInsurancePercentCoveredByEmployer','disabilityInsuranceUnknownEmployerCoverage', ]


