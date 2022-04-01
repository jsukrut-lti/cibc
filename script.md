# Script Snips
from insurancePersonalizationAndRecommendation.insuranceProducts.models import InsuranceProduct, InsuranceDiscussion
InsuranceProduct.objects.all()
InsuranceProduct.objects.get(productCode="mortgage")

# Delete all the discussions
InsuranceDiscussion.objects.all().delete()

from insurancePersonalizationAndRecommendation.stories.models import *