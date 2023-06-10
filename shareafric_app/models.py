from django.db import models

class IndividualRegistration(models.Model):
    name = models.CharField(max_length=255)
    country_of_origin = models.CharField(max_length=255)
    state_region = models.CharField(max_length=255)
    interest = models.TextField()
    sector = models.TextField()
    additional_info = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin_profile = models.URLField()
    facebook_profile = models.URLField()
    instagram_handle = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class SMERegistration(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    registration_no = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    project = models.TextField()
    project_duration = models.CharField(max_length=255)
    tractions = models.TextField()
    startup_stage = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)
    funds_investment = models.TextField()
    
    pitch_deck = models.FileField(upload_to='sme_pitch_decks/')
    financial_model = models.FileField(upload_to='sme_financial_models/')
    cac_documents = models.FileField(upload_to='sme_cac_documents/')
    valuation_report = models.FileField(upload_to='sme_valuation_reports/')
    business_registration_date = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class CorporateRegistration(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    registration_no = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    project = models.TextField()
    project_duration = models.CharField(max_length=255)
    tractions = models.TextField()
    startup_stage = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)
    funds_investment = models.TextField()
    pitch_deck = models.FileField(upload_to='corporate_pitch_decks/')
    financial_model = models.FileField(upload_to='corporate_financial_models/')
    cac_documents = models.FileField(upload_to='corporate_cac_documents/')
    valuation_report = models.FileField(upload_to='corporate_valuation_reports/')
    business_registration_date = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class MentorRegistration(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    organization = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    sector = models.TextField()
    area_of_expertise_and_title = models.TextField()
    linkedin = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f'{self.full_name}'
# from django.db import models

class ElearningRegistration(models.Model):
    INTEREST_CHOICES = (
        ('improveCapacity', 'To help improve on my professional and corporate capacity.'),
        ('dreamJob', 'To help me get my dream job.'),
        ('paidInternship', 'To help me access opportunities for paid internship opportunities.'),
        ('startupBusiness', 'To help me start up my new business.'),
        ('strengthenLeadership', 'To strengthen my leadership capabilities.'),
        ('allOfTheAbove', 'All of the above.'),
    )
    CONTACT_CHOICES = (
        ('phone', 'With Phone'),
        ('email', 'With Email'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    # interests = models.ManyToManyField('ElearningInterest')
    elearning_interest = models.CharField(max_length=255)
    areas_of_study = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True)
    interests_to_communicate = models.TextField()
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    contact_options = models.CharField(
        max_length=20,
        choices=CONTACT_CHOICES,
        blank=True,
        null=True,
    )
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class ElearningInterest(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ElearningAreaOfStudy(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ElearningContactOption(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TouristRegistration(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    interests = models.ManyToManyField('TouristInterest')
    sector_of_interest = models.ManyToManyField('SectorOfInterest')
    additional_info = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    linkedin_profile = models.URLField()
    facebook_profile = models.URLField()
    instagram_handle = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TouristInterest(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SectorOfInterest(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.email}'