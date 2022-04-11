from rest_framework import serializers
from .models import InsuranceDiscussion, InsuranceProduct, CustomUser
from core.models import TimeStampedModel,CANADA_PROVENCES,YES_NO, PAYMENT_FREQUENCY,AGENT_PERCEPTION_OF_CUSTOMER_RESPONSE_TYPE,GENDER
from django.utils.translation import ugettext_lazy as _

class InsuranceProductSerializers(serializers.ModelSerializer):
    productCode = serializers.CharField(max_length=50)
    title = serializers.CharField(max_length=200)

    class Meta:
        model = InsuranceProduct
        fields = '__all__'

    def create(self, validated_data):
        obj = InsuranceProduct.objects.create(
            productCode=validated_data['productCode'],
            title=validated_data['title']
        )
        return obj


class InsuranceDiscussionSerializers(serializers.ModelSerializer):
    insProduct = serializers.IntegerField()
    agent = serializers.IntegerField()
    primaryFirstName = serializers.CharField(max_length=50)
    primaryMiddleName = serializers.CharField(max_length=50)
    primaryLastName = serializers.CharField(max_length=50)
    primaryAge = serializers.IntegerField()
    primaryGender = serializers.CharField(max_length=10)
    coFirstName = serializers.CharField(max_length=50)
    coMiddleName = serializers.CharField(max_length=50)
    coLastName = serializers.CharField(max_length=50)
    coAge = serializers.IntegerField()
    coGender = serializers.CharField(max_length=10)
    canada_provence = serializers.CharField(max_length=50)
    hasPartnerFinResponsibility = serializers.CharField(max_length=3)
    hasChildrenFinResponsibility = serializers.CharField(max_length=3)
    hasParentsFinResponsibility = serializers.CharField(max_length=3)
    hasOthersFinResponsibility = serializers.CharField(max_length=3)
    mortgageBalance = serializers.DecimalField(max_digits=8, decimal_places=2)
    mortgagePmtAmount = serializers.DecimalField(max_digits=8, decimal_places=2)
    mortgagePmtFrequency = serializers.CharField(max_length=1)
    hlocLimit = serializers.DecimalField(max_digits=8, decimal_places=2)
    hlocBalance = serializers.DecimalField(max_digits=8, decimal_places=2)
    hlocMonthlyPmt = serializers.DecimalField(max_digits=8, decimal_places=2)
    personalLoanLimit = serializers.DecimalField(max_digits=8, decimal_places=2)
    personalAmortizationMonths = serializers.IntegerField()
    personalLoanBalance = serializers.DecimalField(max_digits=8, decimal_places=2)
    personalLoanMonthlyPmt = serializers.DecimalField(max_digits=8, decimal_places=2)
    personalPmtFrequency = serializers.CharField(max_length=2)
    creditCardLimit = serializers.DecimalField(max_digits=8, decimal_places=2)
    creditCardBalance = serializers.DecimalField(max_digits=8, decimal_places=2)
    monthlyIncomeAfterTaxes = serializers.DecimalField(max_digits=8, decimal_places=2)
    totalMonthlyExpenses = serializers.DecimalField(max_digits=8, decimal_places=2)
    monthlyExpenseOtherCredit = serializers.DecimalField(max_digits=8, decimal_places=2)
    monthlyExpensePersonal = serializers.DecimalField(max_digits=8, decimal_places=2)
    monthlyExpenseOtherHousing = serializers.DecimalField(max_digits=8, decimal_places=2)
    monthlyExpensePropTaxFees = serializers.DecimalField(max_digits=8, decimal_places=2)
    monthlyExpenseOther = serializers.DecimalField(max_digits=8, decimal_places=2)
    totalSavings = serializers.DecimalField(max_digits=8, decimal_places=2)
    totalSavingsChequing = serializers.DecimalField(max_digits=8, decimal_places=2)
    totalSavingsTaxFreeAccts = serializers.DecimalField(max_digits=8, decimal_places=2)
    totalSavingsRegRetirement = serializers.DecimalField(max_digits=8, decimal_places=2)
    totalSavingsGuarantedInvestmentCerts =serializers.DecimalField(max_digits=8, decimal_places=2)
    totalSavingsOther = serializers.DecimalField(max_digits=8, decimal_places=2)
    lifeInsuranceLimit = serializers.DecimalField(max_digits=8, decimal_places=2)
    criticalIllnessLimit = serializers.DecimalField(max_digits=8, decimal_places=2)
    disabilityInsuranceMonthlyBenefit = serializers.DecimalField(max_digits=8, decimal_places=2)
    disabilityInsurancePercentCoveredByEmployer = serializers.IntegerField()
    disabilityInsuranceUnknownEmployerCoverage = serializers.CharField(max_length=2)
    # Coverage Costs
    lifeInsurancePremiumPerMonth = serializers.DecimalField(max_digits=8, decimal_places=2)
    criticalIllnessPremiumPerMonth = serializers.DecimalField(max_digits=8, decimal_places=2)
    disabilityPremiumPerMonth = serializers.DecimalField(max_digits=8, decimal_places=2)
    agentOverallPerceptionOfCustomerResp = serializers.CharField(max_length=20)
    isRelatedToFinalizedSoldProduct =serializers.BooleanField()
    currentSection = serializers.CharField(max_length=40)

    class Meta:
        model = InsuranceDiscussion
        fields = '__all__'

    def create(self,validated_data):
        print("--validated_data-",validated_data)
        insuranceDiscussion_obj = InsuranceDiscussion.objects.create(
            insProduct = InsuranceProduct.objects.get(id=validated_data['insProduct']),
            agent = CustomUser.objects.get(id=validated_data['agent']),
            primaryFirstName = validated_data['primaryFirstName'],
            primaryMiddleName = validated_data['primaryMiddleName'],
            primaryLastName = validated_data['primaryLastName'],
            primaryAge = validated_data['primaryAge'],
            primaryGender = validated_data['primaryGender'],
            coFirstName = validated_data['coFirstName'],
            coMiddleName = validated_data['coMiddleName'],
            coLastName = validated_data['coLastName'],
            coAge = validated_data['coAge'],
            coGender = validated_data['coGender'],
            canada_provence = validated_data['canada_provence'],
            hasPartnerFinResponsibility = validated_data['hasPartnerFinResponsibility'],
            hasChildrenFinResponsibility = validated_data['hasChildrenFinResponsibility'],
            hasParentsFinResponsibility = validated_data['hasParentsFinResponsibility'],
            hasOthersFinResponsibility = validated_data['hasOthersFinResponsibility'],
            mortgageBalance = validated_data['mortgageBalance'],
            mortgagePmtAmount = validated_data['mortgagePmtAmount'],
            mortgagePmtFrequency = validated_data['mortgagePmtFrequency'],
            hlocLimit = validated_data['hlocLimit'],
            hlocBalance = validated_data['hlocBalance'],
            hlocMonthlyPmt = validated_data['hlocMonthlyPmt'],
            personalLoanLimit = validated_data['personalLoanLimit'],
            personalAmortizationMonths = validated_data['personalAmortizationMonths'],
            personalLoanBalance = validated_data['personalLoanBalance'],
            personalLoanMonthlyPmt = validated_data['personalLoanMonthlyPmt'],
            personalPmtFrequency = validated_data['personalPmtFrequency'],
            creditCardLimit = validated_data['creditCardLimit'],
            creditCardBalance = validated_data['creditCardBalance'],
            monthlyIncomeAfterTaxes = validated_data['monthlyIncomeAfterTaxes'],
            totalMonthlyExpenses = validated_data['totalMonthlyExpenses'],
            monthlyExpenseOtherCredit = validated_data['monthlyExpenseOtherCredit'],
            monthlyExpensePersonal = validated_data['monthlyExpensePersonal'],
            monthlyExpenseOtherHousing = validated_data['monthlyExpenseOtherHousing'],
            monthlyExpensePropTaxFees = validated_data['monthlyExpensePropTaxFees'],
            monthlyExpenseOther = validated_data['monthlyExpenseOther'],
            totalSavings = validated_data['totalSavings'],
            totalSavingsChequing = validated_data['totalSavingsChequing'],
            totalSavingsTaxFreeAccts = validated_data['totalSavingsTaxFreeAccts'],
            totalSavingsRegRetirement = validated_data['totalSavingsRegRetirement'],
            totalSavingsGuarantedInvestmentCerts = validated_data['totalSavingsGuarantedInvestmentCerts'],
            totalSavingsOther = validated_data['totalSavingsOther'],
            lifeInsuranceLimit = validated_data['lifeInsuranceLimit'],
            criticalIllnessLimit = validated_data['criticalIllnessLimit'],
            disabilityInsuranceMonthlyBenefit = validated_data['disabilityInsuranceMonthlyBenefit'],
            disabilityInsurancePercentCoveredByEmployer = validated_data['disabilityInsurancePercentCoveredByEmployer'],
            disabilityInsuranceUnknownEmployerCoverage = validated_data['disabilityInsuranceUnknownEmployerCoverage'],
            lifeInsurancePremiumPerMonth = validated_data['lifeInsurancePremiumPerMonth'],
            criticalIllnessPremiumPerMonth = validated_data['criticalIllnessPremiumPerMonth'],
            disabilityPremiumPerMonth = validated_data['disabilityPremiumPerMonth'],
            agentOverallPerceptionOfCustomerResp = validated_data['agentOverallPerceptionOfCustomerResp'],
            isRelatedToFinalizedSoldProduct = validated_data['isRelatedToFinalizedSoldProduct'],
            currentSection = validated_data['currentSection'],
        )
        return insuranceDiscussion_obj

    def update(self, instance, validated_data):
        instance.insProduct_id = validated_data['insProduct']
        instance.agent_id = validated_data['agent']
        instance.primaryFirstName = validated_data['primaryFirstName']
        instance.primaryMiddleName = validated_data['primaryMiddleName']
        instance.primaryLastName = validated_data['primaryLastName']
        instance.primaryAge = validated_data['primaryAge']
        instance.primaryGender = validated_data['primaryGender']
        instance.coFirstName = validated_data['coFirstName']
        instance.coMiddleName = validated_data['coMiddleName']
        instance.coLastName = validated_data['coLastName']
        instance.coAge = validated_data['coAge']
        instance.coGender = validated_data['coGender']
        instance.canada_provence = validated_data['canada_provence']
        instance.hasPartnerFinResponsibility = validated_data['hasPartnerFinResponsibility']
        instance.hasChildrenFinResponsibility = validated_data['hasChildrenFinResponsibility']
        instance.hasParentsFinResponsibility = validated_data['hasParentsFinResponsibility']
        instance.hasOthersFinResponsibility = validated_data['hasOthersFinResponsibility']
        instance.mortgageBalance = validated_data['mortgageBalance']
        instance.mortgagePmtAmount = validated_data['mortgagePmtAmount']
        instance.mortgagePmtFrequency = validated_data['mortgagePmtFrequency']
        instance.hlocLimit = validated_data['hlocLimit']
        instance.hlocBalance = validated_data['hlocBalance']
        instance.hlocMonthlyPmt = validated_data['hlocMonthlyPmt']
        instance.personalLoanLimit = validated_data['personalLoanLimit']
        instance.personalAmortizationMonths = validated_data['personalAmortizationMonths']
        instance.personalLoanBalance = validated_data['personalLoanBalance']
        instance.personalLoanMonthlyPmt = validated_data['personalLoanMonthlyPmt']
        instance.personalPmtFrequency = validated_data['personalPmtFrequency']
        instance.creditCardLimit = validated_data['creditCardLimit']
        instance.creditCardBalance = validated_data['creditCardBalance']
        instance.monthlyIncomeAfterTaxes = validated_data['monthlyIncomeAfterTaxes']
        instance.totalMonthlyExpenses = validated_data['totalMonthlyExpenses']
        instance.monthlyExpenseOtherCredit = validated_data['monthlyExpenseOtherCredit']
        instance.monthlyExpensePersonal = validated_data['monthlyExpensePersonal']
        instance.monthlyExpenseOtherHousing = validated_data['monthlyExpenseOtherHousing']
        instance.monthlyExpensePropTaxFees = validated_data['monthlyExpensePropTaxFees']
        instance.monthlyExpenseOther = validated_data['monthlyExpenseOther']
        instance.totalSavings = validated_data['totalSavings']
        instance.totalSavingsChequing = validated_data['totalSavingsChequing']
        instance.totalSavingsTaxFreeAccts = validated_data['totalSavingsTaxFreeAccts']
        instance.totalSavingsRegRetirement = validated_data['totalSavingsRegRetirement']
        instance.totalSavingsGuarantedInvestmentCerts = validated_data['totalSavingsGuarantedInvestmentCerts']
        instance.totalSavingsOther = validated_data['totalSavingsOther']
        instance.lifeInsuranceLimit = validated_data['lifeInsuranceLimit']
        instance.criticalIllnessLimit = validated_data['criticalIllnessLimit']
        instance.disabilityInsuranceMonthlyBenefit = validated_data['disabilityInsuranceMonthlyBenefit']
        instance.disabilityInsurancePercentCoveredByEmployer = validated_data[
                                                                   'disabilityInsurancePercentCoveredByEmployer']
        instance.disabilityInsuranceUnknownEmployerCoverage = validated_data[
                                                                  'disabilityInsuranceUnknownEmployerCoverage']
        instance.lifeInsurancePremiumPerMonth = validated_data['lifeInsurancePremiumPerMonth']
        instance.criticalIllnessPremiumPerMonth = validated_data['criticalIllnessPremiumPerMonth']
        instance.disabilityPremiumPerMonth = validated_data['disabilityPremiumPerMonth']
        instance.agentOverallPerceptionOfCustomerResp = validated_data['agentOverallPerceptionOfCustomerResp']
        instance.isRelatedToFinalizedSoldProduct = validated_data['isRelatedToFinalizedSoldProduct']
        instance.currentSection = validated_data['currentSection']
        instance.save()
        return instance








