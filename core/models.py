from django.db import models
from uuid import uuid4
from django.core.exceptions import ValidationError


class Industry(models.Model):
    TYPE_CHOICES = (
        ("para", "Paragraph"),
        ("bullet", "Bullet Points"),
    )

    title = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    content = models.TextField(blank=True, null=True)  # For 'para' type
    list_items = models.JSONField(blank=True, null=True)  # For 'bullet' type
    image = models.ImageField(upload_to="industry_images/")
    is_image_left = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class IndustrySpecification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    is_industry = models.BooleanField(default=False)


# Create your models here.
class HomePageContent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    hero_video = models.FileField(upload_to='videos/hero/', blank=True, null=True)
    hero_image = models.ImageField(upload_to='hero/', blank=True, null=True)
    services_heading = models.CharField(max_length=200, default="Our Services", blank=True, null=True)
    selected_services = models.ManyToManyField('Service', blank=True, help_text='Select up to 6 services to feature on the homepage.')
    journey_heading = models.CharField(max_length=200, default="Our Journey", blank=True, null=True)
    journey_video = models.FileField(upload_to='videos/journey/', blank=True, null=True)
    clientele_heading = models.CharField(max_length=200, default="Our Clientele", blank=True, null=True)
    associations_heading = models.CharField(max_length=200, default="Associations", blank=True, null=True)
    affiliations_heading = models.CharField(max_length=200, default="Affiliations & Accreditation", blank=True, null=True)
    sea_partners_heading = models.CharField(max_length=200, default="Sea Carrier Partners", blank=True, null=True)
    air_partners_heading = models.CharField(max_length=200, default="Air Carrier Partners", blank=True, null=True)
    achievements_heading = models.CharField(max_length=200, default="Achievements", blank=True, null=True)
    locations_heading = models.CharField(max_length=200, default="Our Locations", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    is_active = models.BooleanField(default=True)  # Toggle visibility
    # is_home = models.BooleanField(default=True)  # Toggle home page visibility
    is_hero = models.BooleanField(default=True)  # Toggle hero section visibility
    is_services = models.BooleanField(default=True)  # Toggle services section visibility
    is_journey = models.BooleanField(default=True)  # Toggle journey section visibility
    is_clientele = models.BooleanField(default=True)  # Toggle clientele section visibility
    is_associations = models.BooleanField(default=True)  # Toggle associations section visibility
    is_affiliations = models.BooleanField(default=True)  # Toggle affiliations section visibility
    is_sea_partners = models.BooleanField(default=True)  # Toggle sea partners section visibility
    is_air_partners = models.BooleanField(default=True)  # Toggle air partners section visibility
    is_locations = models.BooleanField(default=True)  # Toggle locations section visibility
    is_achievements = models.BooleanField(default=True)  # Toggle achievements section visibility
    is_news = models.BooleanField(default=True)  # Toggle news section visibility

    def __str__(self):
        return "Home Page Content"
    def clean(self):
        super().clean()
        if self.selected_services.count() > 6:
            raise ValidationError("You can only select up to 6 services.")


class ServiceItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    home = models.ForeignKey(HomePageContent, related_name='services', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='services/')
    is_active = models.BooleanField(default=True)  # Toggle visibility

    def __str__(self):
        return self.title
    
class ClienteleItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    home = models.ForeignKey(HomePageContent, related_name='clientele', on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='clients/')
    is_active = models.BooleanField(default=True)  # Toggle visibility

class AssociationItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    home = models.ForeignKey(HomePageContent, related_name='associations', on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='associations/')
    is_active = models.BooleanField(default=True)  # Toggle visibility

class AffiliationItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    home = models.ForeignKey(HomePageContent, related_name='affiliations', on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='affiliations/')
    is_active = models.BooleanField(default=True)  # Toggle visibility

class SeaPartnerItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    home = models.ForeignKey(HomePageContent, related_name='sea_partners', on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='carriers/sea/')
    is_active = models.BooleanField(default=True)  # Toggle visibility

class AirPartnerItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    home = models.ForeignKey(HomePageContent, related_name='air_partners', on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='carriers/air/')
    is_active = models.BooleanField(default=True)  # Toggle visibility

class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    home = models.ForeignKey(HomePageContent, related_name='locations', on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.JSONField(default=list)
    email = models.EmailField()
    image = models.ImageField(upload_to='locations/')
    place = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)  # Toggle visibility

    def __str__(self):
        return f"{self.city} - {self.place}"

class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    tag = models.JSONField(default=list)
    date = models.DateField()
    image = models.ImageField(upload_to='news/')
    short_description = models.TextField()
    long_description = models.TextField()
    category = models.CharField(max_length=20, default='Transport')
    quote = models.TextField(blank=True)
    in_between_image = models.ImageField(upload_to='News/in_between/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# About Page Models
class AboutPageContent(models.Model):
    heading = models.CharField(max_length=255)
    story_heading = models.CharField(max_length=255)
    story_paragraph = models.TextField()
    founder_image = models.ImageField(upload_to="founder/")
    para1 = models.TextField()
    para2 = models.TextField()
    mission_heading = models.CharField(max_length=255)
    mission_paragraph = models.TextField()
    mission_image = models.ImageField(upload_to="about/mission/")
    vision_heading = models.CharField(max_length=255)
    vision_paragraph = models.TextField()
    vision_image = models.ImageField(upload_to="about/vision/")
    values_heading = models.CharField(max_length=255)
    values_image = models.ImageField(upload_to="about/values/")
    values_points = models.JSONField(default=list)
    # achievements = models.JSONField(default=list)
    achievements_heading = models.CharField(max_length=200, default="Achievements")
    team_heading = models.CharField(max_length=200, default="Our Team")
    faq_heading = models.CharField(max_length=255)
    faq_paragraph = models.TextField()
    is_active = models.BooleanField(default=True)
    is_mission = models.BooleanField(default=True)
    is_vision = models.BooleanField(default=True)
    is_values = models.BooleanField(default=True)
    is_story = models.BooleanField(default=True)
    is_faq = models.BooleanField(default=True)
    is_achievements = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def validate_svg(file):
    if not file.name.endswith('.svg'):
        raise ValidationError("Only SVG files are allowed.")

class Achievement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    home = models.ForeignKey(HomePageContent, related_name='achievements', on_delete=models.CASCADE, default=None, null=True)
    about = models.ForeignKey(AboutPageContent, related_name='achievements', on_delete=models.CASCADE, default=None, null=True, blank=True )
    title = models.CharField(max_length=200)
    count = models.IntegerField()
    icon = models.FileField(upload_to='achievements/', validators=[validate_svg])
    delay = models.CharField(default=".4s", max_length=200)
    suffix = models.CharField(default="", blank=True, null=True, max_length=200)
    prefix = models.CharField(default="", blank=True, null=True, max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class FAQ(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    about = models.ForeignKey(AboutPageContent, related_name="faqs", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_active= models.BooleanField(default=True)

# Carrer Page Models
class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ("full-time", "Full Time"),
        ("part-time", "Part Time"),
        ("internship", "Internship"),
        ("contract", "Contract"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    description = models.TextField()
    apply_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, blank=True)
    cv = models.FileField(upload_to="resumes/")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.job.title if self.job else 'General'}"
    

# SERVICES PAGE MODELS

class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="services/")
    description = models.TextField()
    icon = models.CharField(max_length=100)
    description1 = models.TextField()
    heading = models.CharField(max_length=255)
    description2 = models.TextField()

    def __str__(self):
        return self.title

class ServiceBenefit(models.Model):
    service = models.ForeignKey(Service, related_name='benefits', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.service.title} - {self.text}"


class ValueAddedService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    para1 = models.TextField()
    para2 = models.TextField()

    def __str__(self):
        return self.title
    
# CLIENT PAGE MODELS
class Sector(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SectorLogo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    sector = models.ForeignKey(Sector, related_name='logos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='customer_logo/sector_wise/')
    alt_text = models.CharField(max_length=255)

class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SubCountry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    country = models.ForeignKey(Country, related_name='subcountries', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.country.name} - {self.name}"

class CountryLogo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    subcountry = models.ForeignKey(SubCountry, related_name='logos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='customer_logo/country_wise/')
    alt_text = models.CharField(max_length=255)


# TEAM MEMBER MODELS
class TeamMember(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=255)
    image = models.ImageField(upload_to="team/")
    bio = models.TextField()
    is_active = models.BooleanField(default=True)  # Toggle visibility

    def __str__(self):
        return self.name
    
# Gallery Section

class GalleryEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class GalleryPhoto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    event = models.ForeignKey(GalleryEvent, related_name="photos", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="gallery/")
    alt = models.CharField(max_length=255, blank=True)
    caption = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.alt or self.caption or "Photo"

# Contact Page
class ContactInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    address_title = models.CharField(max_length=255)
    address = models.TextField()
    contact_title = models.CharField(max_length=255)
    phone_label = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    phone_href = models.CharField(max_length=100)
    email_label = models.CharField(max_length=255)
    email = models.EmailField()
    email_href = models.CharField(max_length=100)
    iframe = models.TextField()

    def __str__(self):
        return self.title
    
class ContactQuery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"