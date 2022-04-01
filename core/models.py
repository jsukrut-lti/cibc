from django.db import models
from enum import Enum

class AGENT_PERCEPTION_OF_CUSTOMER_RESPONSE_TYPE(Enum):
    positive = ('positive','positive')
    neutral = ('neutral', 'neutral')
    negative = ('negative','negative')

    @classmethod
    def get_value(cls,member):
        return cls[member].value[0]

class TimeStampedModel(models.Model):
    """
    Abstract base class for all models
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CANADA_PROVENCES(Enum):
    nl = ('nl','Newfoundland and Labrador')
    pe = ('pw','Prince Edward Island')
    ns = ('ns','Nova Scotia')
    nb = ('nb','New Brunswick')
    qc = ('qc','Quebec')
    on = ('on','Ontario')
    mb = ('mb','Manitoba')
    sk = ('sk','Saskatchewan')
    ab = ('ab','Alberta')
    bc = ('bc','British Columbia')
    yt = ('yt','Yukon')
    nt = ('nt','Northwest Territories')
    nu = ('nu','Nunavut')

    @classmethod
    def get_value(cls,member):
        return cls[member].value[0]

class GENDER(Enum):
    m = ('m','Male')
    f = ('f','Female')
    o = ('o','Other')

    @classmethod
    def get_value(cls,member):
        return cls[member].value[0]

class YES_NO(Enum):
    y = ('y','Yes')
    n = ('n','No')

    @classmethod
    def get_value(cls,member):
        return cls[member].value[0]


class PAYMENT_FREQUENCY(Enum):
    m = ('m','Monthly')
    bm = ('bm','Bi-Monthly')
    w = ('w','Weekly')
    sw = ('sw','Semi-Weekly')

    @classmethod
    def get_value(cls,member):
        return cls[member].value[0]

