from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from enum import Enum
from ..accounts.models import CustomUser
from ..insuranceProducts.models import InsuranceDiscussion
from core.models import TimeStampedModel,AGENT_PERCEPTION_OF_CUSTOMER_RESPONSE_TYPE
from django.utils.html import format_html
from django.conf import settings
from river.models.fields.state import StateField


class Character(TimeStampedModel):
    topType_CHOICES = (
        ('Eyepatch','Eyepatch'),
        ('HairColor','HairColor'),
        ('Hat','Hat'),
        ('HatColor','HatColor'),
        ('Hijab','Hijab'),
        ('LongHairBigHair','LongHairBigHair'),
        ('LongHairBob','LongHairBob'),
        ('LongHairBun','LongHairBun'),
        ('LongHairCurly','LongHairCurly'),
        ('LongHairCurvy','LongHairCurvy'),
        ('LongHairDreads','LongHairDreads'),
        ('LongHairFrida','LongHairFrida'),
        ('LongHairFro','LongHairFro'),
        ('LongHairFroBand','LongHairFroBand'),
        ('LongHairMiaWallace','LongHairMiaWallace'),
        ('LongHairNotTooLong','LongHairNotTooLong'),
        ('LongHairShavedSides','LongHairShavedSides'),
        ('LongHairStraight','LongHairStraight'),
        ('LongHairStraight2','LongHairStraight2'),
        ('LongHairStraightStrand','LongHairStraightStrand'),
        ('NoHair','NoHair'),
        ('ShortHairDreads01','ShortHairDreads01'),
        ('ShortHairDreads02','ShortHairDreads02'),
        ('ShortHairFrizzle','ShortHairFrizzle'),
        ('ShortHairShaggy','ShortHairShaggy'),
        ('ShortHairShaggyMullet','ShortHairShaggyMullet'),
        ('ShortHairShortCurly','ShortHairShortCurly'),
        ('ShortHairShortFlat','ShortHairShortFlat'),
        ('ShortHairShortRound','ShortHairShortRound'),
        ('ShortHairShortWaved','ShortHairShortWaved'),
        ('ShortHairSides','ShortHairSides'),
        ('ShortHairTheCaesar','ShortHairTheCaesar'),
        ('ShortHairTheCaesarSidePart','ShortHairTheCaesarSidePart'),
        ('Turban','Turban'),
        ('WinterHat1','WinterHat1'),
        ('WinterHat2','WinterHat2'),
        ('WinterHat3','WinterHat3'),
        ('WinterHat4','WinterHat4')
        )

    accessoriesType_CHOICES =(
        ('Blank', 'Blank'),
        ('Kurt', 'Kurt'),
        ('Prescription01', 'Prescription01'),
        ('Prescription02', 'Prescription02'),
        ('Round', 'Round'),
        ('Sunglasses', 'Sunglasses'),
        ('Wayfarers', 'Wayfarers')

    )
    hatColor_CHOICES = (
        ('Black','Black'),
        ('Blue01','Blue01'),
        ('Blue02','Blue02'),
        ('Blue03','Blue03'),
        ('Gray01','Gray01'),
        ('Gray02','Gray02'),
        ('Heather','Heather'),
        ('PastelBlue','PastelBlue'),
        ('PastelGreen','PastelGreen'),
        ('PastelOrange','PastelOrange'),
        ('PastelRed','PastelRed'),
        ('PastelYellow','PastelYellow'),
        ('Pink','Pink'),
        ('Red','Red'),
        ('White','White'),
    )

    hairColor_CHOICES = (
        ('Black','Black'),
        ('Blonde','Blonde'),
        ('BlondeGolden','BlondeGolden'),
        ('Brown','Brown'),
        ('BrownDark','BrownDark'),
        ('PastelPink','PastelPink'),
        ('Platinum','Platinum'),
        ('Red','Red'),
        ('SilverGray','SilverGray')
    )

    facialHairType_CHOICES =(
        ('BeardLight', 'BeardLight'),
        ('BeardMagestic', 'BeardMagestic'),
        ('BeardMajestic', 'BeardMajestic'),
        ('BeardMedium', 'BeardMedium'),
        ('Blank', 'Blank'),
        ('Colors', 'Colors'),
        ('MoustacheFancy', 'MoustacheFancy'),
        ('MoustacheMagnum', 'MoustacheMagnum')
    )

    facialHairColor_CHOICES = (
        ('Auburn','Auburn'),
        ('Black','Black'),
        ('Blonde','Blonde'),
        ('BlondeGolden','BlondeGolden'),
        ('Brown','Brown'),
        ('BrownDark','BrownDark'),
        ('Platinum','Platinum'),
        ('Red','Red'),
    )

    clotheType_CHOICES = (
        ('BlazerShirt','BlazerShirt'),
        ('BlazerSweater','BlazerSweater'),
        ('CollarSweater','CollarSweater'),
        ('Colors','Colors'),
        ('GraphicShirt','GraphicShirt'),
        ('Graphics','Graphics'),
        ('Hoodie','Hoodie'),
        ('ShirtVNeck', 'ShirtVNeck'),
        ('ShirtCrewNeck', 'ShirtCrewNeck'),
        ('ShirtScoopNeck', 'ShirtScoopNeck'),
    )
    clotheColor_CHOICES = (
        ('Black','Black'),
        ('Blue01','Blue01'),
        ('Blue02','Blue02'),
        ('Blue03','Blue03'),
        ('Gray01','Gray01'),
        ('Gray02','Gray02'),
        ('Heather','Heather'),
        ('PastelBlue','PastelBlue'),
        ('PastelGreen','PastelGreen'),
        ('PastelOrange','PastelOrange'),
        ('PastelRed','PastelRed'),
        ('PastelYellow','PastelYellow'),
        ('Pink','Pink'),
        ('Red','Red'),
        ('White','White')
    )

    graphicType_CHOICES = (
        ('Bat','Bat'),
        ('Cumbia','Cumbia'),
        ('Deer','Deer'),
        ('Diamond','Diamond'),
        ('Hola','Hola'),
        ('Pizza','Pizza'),
        ('Resist','Resist'),
        ('Selena','Selena'),
        ('Bear','Bear'),
        ('SkullOutline','SkullOutline'),
        ('Skull','Skull')
    )

    eyeType_CHOICES =(
        ('Default','Default'),
        ('Close','Close'),
        ('Cry','Cry'),
        ('Dizzy','Dizzy'),
        ('EyeRoll','EyeRoll'),
        ('Happy','Happy'),
        ('Hearts','Hearts'),
        ('Side','Side'),
        ('Squint','Squint'),
        ('Surprised','Surprised'),
        ('Wink','Wink'),
        ('WinkWacky','WinkWacky')
    )

    eyebrowType_CHOICES = (
        ('Default','Default'),
        ('Angry','Angry'),
        ('AngryNatural','AngryNatural'),
        ('DefaultNatural','DefaultNatural'),
        ('FlatNatural','FlatNatural'),
        ('FrownNatural','FrownNatural'),
        ('RaisedExcited','RaisedExcited'),
        ('RaisedExcitedNatural','RaisedExcitedNatural'),
        ('SadConcerned','SadConcerned'),
        ('SadConcernedNatural','SadConcernedNatural'),
        ('UnibrowNatural','UnibrowNatural'),
        ('UpDown','UpDown'),
        ('UpDownNatural','UpDownNatural'),
    )

    mouthType_CHOICES =(
        ('Default','Default'),
        ('Concerned','Concerned'),
        ('Disbelief','Disbelief'),
        ('Eating','Eating'),
        ('Grimace','Grimace'),
        ('Sad','Sad'),
        ('ScreamOpen','ScreamOpen'),
        ('Serious','Serious'),
        ('Smile','Smile'),
        ('Tongue','Tongue'),
        ('Twinkle','Twinkle'),
        ('Vomit','Vomit'),
    )

    skinColor_CHOICES = (
        ('Tanned','Tanned'),
        ('Yellow','Yellow'),
        ('Pale','Pale'),
        ('Light','Light'),
        ('Brown','Brown'),
        ('DarkBrown','DarkBrown'),
        ('Black','Black'),
    )


    characterName = models.CharField(_("Name"),max_length=50,unique=True)
    backstory = models.CharField(_("Backstory"),max_length=300)

    #Characteristics
    topType = models.CharField(_("Top"),max_length=50,choices=topType_CHOICES,null=True, blank=True)
    accessoriesType = models.CharField(_("👓 Accessories"),max_length=50,choices=accessoriesType_CHOICES,null=True, blank=True)
    hatColor = models.CharField(_("🎨 HatColor"),max_length=50,choices=hatColor_CHOICES,null=True, blank=True)
    hairColor = models.CharField(_("💈 Hair Color"),max_length=50,choices=hairColor_CHOICES,null=True, blank=True)
    facialHairType = models.CharField(_("Facial Hair"),max_length=50,choices=facialHairType_CHOICES,null=True, blank=True)
    facialHairColor = models.CharField(_("✂️ Facial Hair Color"),max_length=50,choices=facialHairColor_CHOICES,null=True, blank=True)
    clotheType = models.CharField(_("👔 Clothes"),max_length=50,choices=clotheType_CHOICES,null=True, blank=True)
    clotheColor = models.CharField(_("Color Fabric"),max_length=50,choices=clotheColor_CHOICES,null=True, blank=True)
    graphicType = models.CharField(_("Graphic"),max_length=50,choices=graphicType_CHOICES,null=True, blank=True)
    eyeType = models.CharField(_("👁 Eyes"),max_length=50,choices=eyeType_CHOICES,null=True, blank=True)
    eyebrowType = models.CharField(_("✏️ Eyebrow"),max_length=50,choices=eyebrowType_CHOICES,null=True, blank=True)
    mouthType = models.CharField(_("👄 Mouth"),max_length=50,choices=mouthType_CHOICES,null=True, blank=True)
    skinColor = models.CharField(_("🎨 Skin"),max_length=50,choices=skinColor_CHOICES,null=True, blank=True)

    # Image Field to leverage to display avatar
    avatarImage = models.ImageField(_("Avatar Image"),null=True, blank=True)

    def __str__(self):
        return '{}:{}'.format(self.characterName,self.backstory)

    def get_character_img_url(self):
        # Example
        # 'https://avataaars.io/?avatarStyle=Circle&topType=LongHairStraight&accessoriesType=Blank&hairColor=BrownDark&facialHairType=Blank&clotheType=BlazerShirt&eyeType=Default&eyebrowType=Default&mouthType=Default&skinColor=Light')
        urlStart = settings.AVATARS_SERVER_URL
        style = 'Circle'
        fullURL = format_html(
            '{}/?avatarStyle={}&topType={}&accessoriesType={}&hairColor={}&facialHairType={}&clotheType={}&eyeType={}&eyebrowType={}&mouthType={}&skinColor={}&clotheColor={}',
            urlStart,
            style,
            self.topType,
            self.accessoriesType,
            self.hairColor,
            self.facialHairType,
            self.clotheType,
            self.eyeType,
            self.eyebrowType,
            self.mouthType,
            self.skinColor,
            self.clotheColor)
        return fullURL

class Story(TimeStampedModel):
    storyName = models.CharField(_("Name"), max_length=50, unique=True)
    summary = models.CharField(_("Summary"), max_length=300)
    introduction = models.CharField(_("Introduction"), max_length=300)
    middle = models.CharField(_("Middle"), max_length=300)
    conclusion = models.CharField(_("Conclusion"), max_length=300)
    keyInsights = models.CharField(_("Key Insights, Messaging or Lessons"), max_length=300)

    def get_absolute_url(self):
        return reverse('story-update', kwargs={'pk': self.pk})

    def __str__(self):
        return '{}'.format(self.storyName)

class StoryCharacter(TimeStampedModel):
    story = models.ForeignKey(Story, related_name='Story', on_delete=models.CASCADE, null=False, blank=False)
    character = models.ForeignKey(Character,related_name='Character', on_delete=models.CASCADE, null=False, blank=False)
    priorityOrder = models.PositiveSmallIntegerField(_("Priority Order"), null=True, blank=True)

    def __str__(self):
        return '{} {} {}'.format(self.story.storyName,self.character.characterName,self.priorityOrder)


class BUTTLE_TYPE(Enum):
    prebuttle = ('prebuttle','Prebuttle')
    rebuttle = ('rebuttle','Rebuttle')

    @classmethod
    def get_value(cls,member):
        return cls[member].value[0]

class Objection(TimeStampedModel):
    objectionName = models.CharField(_("Name of Objection"), max_length=50, unique=True)
    primaryIssueOrConcern = models.CharField(_("Primary issues or concerns"), max_length=300)
    my_state_field = StateField()

    def __str__(self):
        return '{}'.format(self.objectionName)

class ObjectionHandle(TimeStampedModel):
    buttleName = models.CharField(_("Name of Re-Buttle or Pre-Buttle"), max_length=50, unique=True)
    buttleMessaging = models.CharField(_("Message"), max_length=300)
    buttleType = models.CharField(_("Buttle Type"), max_length=12, choices=[x.value for x in BUTTLE_TYPE],null=True,blank=True)
    objection = models.ForeignKey(Objection,related_name='Objection', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.buttleName)

class MESSAGE_TRANSMISSION_TYPE(Enum):
    spokenByAgent = ('spokenByAgent','spokenByAgent')
    showedByAgent = ('shownByAgent','shownByAgent')
    selfServiceDisplay = ('selfServiceDisplay', 'selfServiceDisplay')
    agentDeclinedUsage = ('agentDeclinedUsage', 'agentDeclinedUsage')

    @classmethod
    def get_value(cls,member):
        return cls[member].value[0]



# Was the story, objection, or objectionHandled
class StatsTracker(TimeStampedModel):
    insuranceDiscussion = models.ForeignKey(InsuranceDiscussion, on_delete=models.CASCADE,null=False,blank=False)
    agent = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)
    hasMessagingTransmitted = models.BooleanField(_("Messaging relayed to customer"),default=False )
    messagingTransmissionType = models.CharField(_("How message relayed to customer"), choices=[x.value for x in MESSAGE_TRANSMISSION_TYPE], null=False, blank=False,max_length=20)
    agentPerceptionOfCustomerResp = models.CharField(_("Agent Perception of customer response"), choices=[x.value for x in AGENT_PERCEPTION_OF_CUSTOMER_RESPONSE_TYPE], null=False, blank=True,max_length=20)

    class Meta:
        abstract = True


class StoryStatsTracker(StatsTracker):
    story = models.ForeignKey(Story, related_name='StoryStat', on_delete=models.CASCADE, null=False,blank=False)

class ObjectionHandleStatsTracker(StatsTracker):
    objectionHandle = models.ForeignKey(ObjectionHandle, related_name='ObjectionHandleStat', on_delete=models.CASCADE, null=False, blank=False)

class ObjectioonStatsTracker(StatsTracker):
    objection = models.ForeignKey(Objection, related_name='ObjectionStat', on_delete=models.CASCADE, null=False,blank=False)





