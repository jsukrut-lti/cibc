from django.db import models
from core.models import TimeStampedModel,CANADA_PROVENCES,YES_NO, PAYMENT_FREQUENCY,AGENT_PERCEPTION_OF_CUSTOMER_RESPONSE_TYPE,GENDER
from django.utils.translation import ugettext_lazy as _
from ..accounts.models import CustomUser
from enum import Enum
from django.contrib.postgres.fields import JSONField
from django.utils import timezone
# from encrypted_id.models import EncryptedIDModel
import struct
from .cryptographic import *
import uuid


class InsuranceCreditProduct(TimeStampedModel):
    credit_product_code = models.CharField(max_length=100, verbose_name=u"Credit Product Code",
                            help_text=u"Credit Product Code", unique=True,blank=False)
    credit_product_name = models.CharField(max_length=200, verbose_name=u"Credit Product Name", help_text=u"Credit Product Name", blank=False)
    active = models.BooleanField(verbose_name=u"Active", default=True)

    def __str__(self):
        return '{}'.format(self.credit_product_name)

    class Meta:
        db_table = 'insurance_credit_products'
        verbose_name_plural = 'Insurance Credit Products Master'


class InsuranceProduct(TimeStampedModel):
    productCode = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    creditProduct_code = models.ForeignKey(InsuranceCreditProduct, on_delete=models.CASCADE, related_name='creditProduct_code',null=False,blank=False, default=True)
    product_cibc_code = models.CharField(max_length=50, default=True)
    active = models.BooleanField(verbose_name=u"Active", default=True)

    def __str__(self):
        return '{}'.format(self.title)
    #
    # class Meta:
    #     db_table = 'insurance_products'
    #     verbose_name_plural = 'Insurance Products Master'

class DISCUSSION_OUTCOME_TYPE(Enum):
    declined = ('declined','declined')
    acceptedOffer = ('acceptedOffer','acceptedOffer')
    requiresFollowup = ('requiresFollowup', 'requiresFollowup')

    @classmethod
    def get_value(cls,member):
        return cls[member].value[0]

class DISCUSSION_SECTION_TYPE(Enum):
    customerInfoMin = ('customerInfoMin','customerInfoMin')
    lovedOnes = ('lovedOnes','lovedOnes')
    creditInfo = ('creditInfo','creditInfo')
    highLevelIncomeExpensesSaving = ('incomeExpenseSvgs','incomeExpenseSvgs')
    detailedIncome = ('detailedIncome','detailedIncome')
    detailedExpense = ('detailedExpense','detailedExpense')
    detailedSavings = ('detailedSavings','detailedSavings')
    otherInsCoverage = ('otherInsCoverage','otherInsCoverage')
    personalPresentment = ('personalPresentment','personalPresentment')


    @classmethod
    def get_value(cls,member):
        return cls[member].value[0]

"""
Scenario States
0. Inital State: Set inital totals: Expense, Income, and Savings
1. Job Loss: 
    - Change story to that of job loss
    - Set Income to $0
    - Keep Expenses Same
    - If (has Job Loss Cov): 
        Remove morgage from expense
    
2. Critical Illness: 
3. Disability:
4. Death:
"""
class SCENARIO_TYPE(Enum):
    init = ('init', 'init')
    jobLoss = ('jobLoss', 'jobLoss')
    critIllness = ('critIllness', 'critIllness')
    death = ('death', 'death')

    @classmethod
    def get_value(cls,member):
        return cls[member].value[0]


class InsuranceDiscussion(TimeStampedModel):

    STATUS_CHOICES = (
        ('inprocess', 'INPROCESS'),
        ('complete', 'COMPLETE'),
        ('incomplete', 'INCOMPLETE'),
    )

    insProduct = models.ForeignKey(InsuranceProduct, on_delete=models.CASCADE,null=False,blank=False)
    agent = models.ForeignKey(CustomUser, related_name='agent', on_delete=models.CASCADE,null=False,blank=False)
    # unique = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    #Application Details
    application_number = models.CharField(max_length=100, verbose_name=u"Application Number",
                                          help_text=u"Application Number",null=True,blank=True)

    application_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inprocess')

    # Primary Demographics
    primaryFirstName = models.CharField(_("First Name"), max_length=50,blank=True)
    primaryMiddleName = models.CharField(_("Middle Name"), max_length=50,blank=True)
    primaryLastName = models.CharField(_("Last Name"), max_length=50,blank=True)
    primaryAge = models.PositiveSmallIntegerField(_("Age"),null=True,blank=True)
    primaryGender = models.CharField(_("Gender"), max_length=2, choices=[x.value for x in GENDER], null=True, blank=True)

    coFirstName = models.CharField(_("Co Borrower - First Name"), max_length=50,blank=True)
    coMiddleName = models.CharField(_("Co Borrower - Middle Name"), max_length=50,blank=True)
    coLastName = models.CharField(_("Co Borrower - Last Name"), max_length=50,blank=True)
    coAge = models.PositiveSmallIntegerField(_("Age"),null=True,blank=True)
    coGender = models.CharField(_("Co Borrower - Gender"), max_length=2, choices=[x.value for x in GENDER], null=True, blank=True)

    canada_provence = models.CharField(_("Province"), max_length=2, choices=[x.value for x in CANADA_PROVENCES],null=True,blank=True)
    hoursWeekWorking = models.IntegerField(_("Hours a Week Working"), null=True, blank=True)

    #Loved Ones financial responsibility
    hasPartnerFinResponsibility = models.CharField(_("Partner Financial Responsibility"), max_length=2, choices=[x.value for x in YES_NO],null=True, blank=True)
    hasChildrenFinResponsibility = models.CharField(_("Children Financial Responsibility"), max_length=2, choices=[x.value for x in YES_NO],null=True, blank=True)
    hasParentsFinResponsibility = models.CharField(_("Other Relatives Financial Responsibility"), max_length=2, choices=[x.value for x in YES_NO],null=True, blank=True)
    hasOthersFinResponsibility = models.CharField(_("Other Financial Responsibility"), max_length=2, choices=[x.value for x in YES_NO],null=True, blank=True)

    #Creditor Information
    mortgageBalance = models.DecimalField(_("Mortgage Balance"),max_digits=8, decimal_places=2,null=True, blank=True)
    mortgagePmtAmount = models.DecimalField(_("Mortgage Payment Amount"),max_digits=8, decimal_places=2,null=True, blank=True)
    mortgagePmtFrequency = models.CharField(_("Mortgage Payment Frequency"), max_length=2,choices=[x.value for x in PAYMENT_FREQUENCY], null=True, blank=True)

    hlocLimit = models.DecimalField(_("HLOC Limit"),max_digits=8, decimal_places=2,null=True, blank=True)
    hlocBalance = models.DecimalField(_("HLOC Balance"),max_digits=8, decimal_places=2,null=True, blank=True)
    hlocMonthlyPmt = models.DecimalField(_("HLOC Monthly Payment"),max_digits=8, decimal_places=2,null=True, blank=True)

    personalLoanLimit = models.DecimalField(_("Personal Loan Limit"),max_digits=8, decimal_places=2,null=True, blank=True)
    personalAmortizationMonths = models.IntegerField(_("Personal Loan Amortization In Months"), null=True,blank=True)
    personalLoanBalance = models.DecimalField(_("Personal Loan Balance"),max_digits=8, decimal_places=2,null=True, blank=True)
    personalLoanMonthlyPmt = models.DecimalField(_("Personal Loan Monthly Payment"),max_digits=8, decimal_places=2,null=True, blank=True)
    personalPmtFrequency = models.CharField(_("Personal Loan Payment Frequency"), max_length=2,choices=[x.value for x in PAYMENT_FREQUENCY], null=True, blank=True)

    creditCardLimit = models.DecimalField(_("Credit Card Limit"),max_digits=8, decimal_places=2,null=True, blank=True)
    creditCardBalance = models.DecimalField(_("Credit Card Balance"),max_digits=8, decimal_places=2,null=True, blank=True)

    # Income, Expenses, and Savings
    monthlyIncomeAfterTaxes = models.DecimalField(_("Monthly Income After Taxes"), max_digits=8, decimal_places=2, null=True, blank=True)

    # Other Monthly Expense
    totalMonthlyExpenses = models.DecimalField(_("Total monthly expenses"), max_digits=8, decimal_places=2, null=True, blank=True)
    monthlyExpenseOtherCredit = models.DecimalField(_("Other Debts Monthly expenses"), max_digits=8, decimal_places=2, null=True, blank=True)
    monthlyExpensePersonal = models.DecimalField(_("Personal Monthly expenses"), max_digits=8, decimal_places=2, null=True, blank=True)
    monthlyExpenseOtherHousing = models.DecimalField(_("Other Housing Payments monthly expenses"), max_digits=8, decimal_places=2, null=True, blank=True)
    monthlyExpensePropTaxFees = models.DecimalField(_("Property taxes, condo fees, etc monthly expenses"), max_digits=8, decimal_places=2, null=True, blank=True)
    monthlyExpenseOther = models.DecimalField(_("Other monthly expenses"), max_digits=8, decimal_places=2, null=True, blank=True)

    # Other Saving sExpense
    totalSavings = models.DecimalField(_("Total Savings"), max_digits=8, decimal_places=2, null=True, blank=True)
    totalSavingsChequing = models.DecimalField(_("Chequing and savings amounts"), max_digits=8, decimal_places=2, null=True, blank=True)
    totalSavingsTaxFreeAccts = models.DecimalField(_("Tax-Free Savings Account"), max_digits=8, decimal_places=2, null=True, blank=True)
    totalSavingsRegRetirement = models.DecimalField(_("Registered Retirement Savings Plans"), max_digits=8, decimal_places=2, null=True, blank=True)
    totalSavingsGuarantedInvestmentCerts = models.DecimalField(_("Guaranteed Investment Certificate"), max_digits=8, decimal_places=2, null=True, blank=True)
    totalSavingsOther = models.DecimalField(_("Other Savings"), max_digits=8, decimal_places=2, null=True, blank=True)

    # Other Insurance
    lifeInsuranceLimit = models.DecimalField(_("Life Insurance Limit"), max_digits=8, decimal_places=2, null=True, blank=True)
    criticalIllnessLimit = models.DecimalField(_("Critical Illness Limit"), max_digits=8, decimal_places=2, null=True, blank=True)
    disabilityInsuranceMonthlyBenefit = models.DecimalField(_("Disability Insurance Monthly Benefit"), max_digits=8, decimal_places=2, null=True, blank=True)
    disabilityInsurancePercentCoveredByEmployer = models.PositiveSmallIntegerField(_("Disability Insurance Percent Covered By Employer"), null=True, blank=True)
    disabilityInsuranceUnknownEmployerCoverage = models.CharField(_("Not sure what my employer covers"), max_length=2, choices=[x.value for x in YES_NO],null=True, blank=True)


    # Coverage Costs
    lifeInsurancePremiumPerMonth = models.DecimalField(_("Life Insurance Premium Per Month"), max_digits=8, decimal_places=2, null=True, blank=True)
    criticalIllnessPremiumPerMonth = models.DecimalField(_("Critical Illness Premium Per Month"), max_digits=8, decimal_places=2, null=True, blank=True)
    disabilityPremiumPerMonth = models.DecimalField(_("Disability Insurance Premium Per Month"), max_digits=8, decimal_places=2, null=True, blank=True)


    # Tracking
    agentOverallPerceptionOfCustomerResp = models.CharField(_("Agent Perception of customer response"),  choices=[x.value for x in AGENT_PERCEPTION_OF_CUSTOMER_RESPONSE_TYPE], null=True, blank=True, max_length=20)
    isRelatedToFinalizedSoldProduct = models.BooleanField(_("Discussion lead to sale"),default=False )
    discussionOutcomes = models.CharField(_("Outcome of discussion"),  choices=[x.value for x in DISCUSSION_OUTCOME_TYPE], null=True, blank=True, max_length=20)
    currentSection = models.CharField(_("Discussion Section"), choices=[x.value for x in DISCUSSION_SECTION_TYPE],null=True, blank=True, max_length=40)

    # additional fields
    approxNetIncome = models.DecimalField(_("Approximate Net Income"), max_digits=8, decimal_places=2, null=True, blank=True)
    totalUnsecuredAmt = models.DecimalField(_("Total Unsecured Amount"), max_digits=8, decimal_places=2, null=True, blank=True)
    totalSecuredAmt = models.DecimalField(_("Total Secured Amount"), max_digits=8, decimal_places=2, null=True, blank=True)
    totalExistingDebt = models.DecimalField(_("Total Existing Debt"), max_digits=8, decimal_places=2, null=True, blank=True)
    currentApplicationPmt = models.DecimalField(_("Current Application Payment"), max_digits=8, decimal_places=2, null=True, blank=True)
    totalMonthlyPmt = models.DecimalField(_("Total Monthly Payment"), max_digits=8, decimal_places=2, null=True, blank=True)
    savingsEmergencyFund = models.DecimalField(_("Saving & Emergency Fund"), max_digits=8, decimal_places=2, null=True, blank=True)

    sssavingsEmergencyFund = models.DecimalField(_("Saving & Emergency Fund"), max_digits=8, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.insProduct)

    def totalInsPlusMortgage(self):
        return self.totalinsuranceCost() + self.mortgagePmtAmount

    def totalinsuranceCost(self):
        return self.lifeInsurancePremiumPerMonth + self.criticalIllnessPremiumPerMonth + self.disabilityPremiumPerMonth


class InsuranceDiscussionApplicantDetails(TimeStampedModel):
    insDiscussion = models.ForeignKey(InsuranceDiscussion, on_delete=models.CASCADE, null=False, blank=False)
    application_number = models.CharField(max_length=100, verbose_name=u"Application Number",
                                          help_text=u"Application Number", blank=False)
    applicantID = models.CharField(max_length=100, verbose_name=u"Applicant ID",
                                          help_text=u"Applicant ID", blank=False)
    active = models.BooleanField(verbose_name=u"Active", default=True)


class InsurancePreProcessData(TimeStampedModel):
    STATUS_CHOICES =(
        ('draft', 'DRAFT'),
        ('active', 'ACTIVE'),
        ('deactivate', 'DEACTIVATE'),
    )

    application_number = models.CharField(max_length=100, verbose_name=u"Application Number", help_text=u"Application Number",blank=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    data = models.JSONField()

    def __str__(self):
        return '{}'.format(self.application_number)

class ProvinceResidence(TimeStampedModel):

    RESIDENCY = [
        ('Canada', 'Canadian Residence'),
        ('Other', 'Others'),
    ]
    province = models.CharField(max_length=3, verbose_name=u"Province",help_text=u"Province", blank=False)
    description = models.CharField(max_length=100, verbose_name=u"Province Description",help_text=u"Province Description", blank=False)
    residency = models.CharField(_("Residency"), max_length=50, choices=RESIDENCY,null=True, blank=True)
    active = models.BooleanField(verbose_name=u"Active", default=True)

    def __str__(self):
        return '{}'.format(self.description)

    class Meta:
        db_table = 'province_residence_master'
        verbose_name_plural = 'Province Residence Master'


class OccupationMaster(TimeStampedModel):
    occupation_code = models.CharField(max_length=10, verbose_name=u"Occupation Code",help_text=u"Occupation Code", blank=False)
    occupation_name = models.CharField(max_length=100, verbose_name=u"Occupation Name",help_text=u"Occupation Name", blank=False)
    active = models.BooleanField(verbose_name=u"Active", default=True)

    def __str__(self):
        return '{}'.format(self.occupation_name)

    class Meta:
        db_table = 'occupation_master'
        verbose_name_plural = 'Occupation Master'


class InsuranceEligibility(TimeStampedModel):

    RESIDENCY = [
        ('Canada', 'Canadian Residence'),
        ('Other', 'Others'),
    ]

    insProduct = models.ForeignKey(InsuranceProduct, on_delete=models.CASCADE,null=False,blank=False)
    minAge = models.PositiveSmallIntegerField(_("Min Age"),null=True,blank=True)
    maxAge = models.PositiveSmallIntegerField(_("Max Age"), null=True, blank=True)
    residency = models.CharField(_("Residency"), max_length=50, choices=RESIDENCY,null=True, blank=True)
    occupation = models.ForeignKey(OccupationMaster, on_delete=models.CASCADE,null=True,blank=True)
    effective_start_date = models.DateField(verbose_name=u"Effective Start Date", default=timezone.now)
    effective_end_date = models.DateField(verbose_name=u"Effective End Date", default="2099-12-31")
    active = models.BooleanField(verbose_name=u"Active", default=True)

    def __str__(self):
        return '{}'.format(self.insProduct)

    class Meta:
        db_table = 'insurance_eligibility_master'
        verbose_name_plural = 'Insurance Eligibility Master'


class InsuranceNonEligibleContent(TimeStampedModel):

    content = models.TextField(verbose_name=u"Non Eligible Content")
    effective_start_date = models.DateField(verbose_name=u"Effective Start Date", default=timezone.now)
    effective_end_date = models.DateField(verbose_name=u"Effective End Date", default="2099-12-31")
    active = models.BooleanField(verbose_name=u"Active", default=True)

    def __str__(self):
        return '{}'.format(self.content)


class ClientDetails(TimeStampedModel):

    client_id = models.CharField(max_length=11, verbose_name=u"Client ID",
                            help_text=u"Client ID", unique=True,blank=False)
    client_name = models.CharField(max_length=100, verbose_name=u"Client Name",help_text=u"Client Name", blank=False)
    client_email = models.CharField(max_length=100, verbose_name=u"Client Email",help_text=u"Client Email", blank=False)
    client_phone = models.CharField(max_length=100, verbose_name=u"Client Phone", help_text=u"Client Phone",blank=False)
    effective_start_date = models.DateField(verbose_name=u"Effective Start Date", default=timezone.now)
    effective_end_date = models.DateField(verbose_name=u"Effective End Date", default="2099-12-31")
    active = models.BooleanField(verbose_name=u"Active", default=True)

    def __str__(self):
        return '{}'.format(self.content)


class AssessmentQuestionnaireMaster(TimeStampedModel):

    assessment_id = models.CharField(max_length=11, verbose_name=u"Assessment ID",
                            help_text=u"Assessment ID", unique=True,blank=False)
    assessment_details = models.TextField(verbose_name=u"Non Assessment Details")
    effective_start_date = models.DateField(verbose_name=u"Effective Start Date", default=timezone.now)
    effective_end_date = models.DateField(verbose_name=u"Effective End Date", default="2099-12-31")
    active = models.BooleanField(verbose_name=u"Active", default=True)

    def __str__(self):
        return '{}'.format(self.assessment_details)


class ExitSurveyMaster(TimeStampedModel):
    exit_id = models.CharField(max_length=11, verbose_name=u"Exit ID",
                            help_text=u"Exit ID", unique=True,blank=False)
    exit_selector = models.CharField(max_length=100, verbose_name=u"Exit Selector",
                            help_text=u"Exit Selector", unique=True,blank=False)
    exit_radio_display = models.CharField(max_length=500, verbose_name=u"Radio Msg",
                                          help_text=u"Radio Message", unique=False, blank=True)
    exit_msg_line0 = models.CharField(max_length=500, verbose_name=u"Exit Msg0",
                                help_text=u"Exit Message0", unique=False, blank=True)
    exit_msg_line1 = models.CharField(max_length=500, verbose_name=u"Exit Msg1",
                                              help_text=u"Exit Message1", unique=False, blank=True)
    exit_msg_line2 = models.CharField(max_length=500, verbose_name=u"Exit Msg2",
                                              help_text=u"Exit Message2", unique=False, blank=True)

    def __str__(self):
        return '{}'.format(self.exit_selector)
