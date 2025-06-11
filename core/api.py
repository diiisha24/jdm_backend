# api.py or views.py (if using django-ninja)

from ninja import NinjaAPI, Form, File
from ninja.files import UploadedFile
from typing import Optional
from ninja.errors import HttpError
from .models import HomePageContent, AboutPageContent, Job, News, JobApplication, Service, ServiceBenefit, ValueAddedService, TeamMember, GalleryEvent, ContactInfo, ContactQuery, IndustrySpecification, Industry
from .schemas import HomePageSchema, AboutPageSchema, JobSchema, NewsSchema, JobApplicationSchema, ServiceSchema, ValueAddedServiceSchema, TeamMemberSchema,GalleryEventSchema, ContactInfoSchema , ContactQuerySchema, IndustrySchema, IndustrySpecificationSchema
import json
from django.shortcuts import get_object_or_404
# import form_
# from djnago.core.files.base import ContentFile

api = NinjaAPI(csrf=True, urls_namespace="core-api")

@api.get("/home/", response=HomePageSchema)
def get_home(request):
    home = HomePageContent.objects.first()  # Get the first instance of HomePageContent
    if not home:
        return HttpError(404, "Home page content not found.")

    return {
        "hero": {
            "video_url": home.hero_video.url if home.hero_video else None,
            "image_url": home.hero_image.url if home.hero_image else None
        },
        "services": {
            "heading": home.services_heading,
            "items": [
                {
                    "id": service.id,
                    "title": service.title,
                    "image": service.image.url if service.image else None
                } for service in home.selected_services.all()
            ]
        },
        "journey": {
            "heading": home.journey_heading,
            "video_url": home.journey_video.url if home.journey_video else None
        },
        "clientele": {
            "heading": home.clientele_heading,
            "items": [item.logo.url for item in home.clientele.all()]
        },
        "associations": {
            "heading": home.associations_heading,
            "items": [item.logo.url for item in home.associations.all()]
        },
        "affiliations": {
            "heading": home.affiliations_heading,
            "items": [item.logo.url for item in home.affiliations.all()]
        },
        "sea_partners": {
            "heading": home.sea_partners_heading,
            "items": [item.logo.url for item in home.sea_partners.all()]
        },
        "air_partners": {
            "heading": home.air_partners_heading,
            "items": [item.logo.url for item in home.air_partners.all()]
        },
        "locations": {
            "heading": home.locations_heading,
            "items": [{
                "id": loc.id,
                "city": loc.city,
                "address": loc.address,
                "phone": loc.phone,
                "email": loc.email,
                "image": loc.image.url,
                "place": loc.place
            } for loc in home.locations.all()]
        },
        "achievements": {
            "heading": home.achievements_heading,
            "items": [
            {
                "id": ach.id,
                "title": ach.title,
                "count": ach.count,
                "icon": ach.icon.url,
                "delay": ach.delay,
                "suffix": ach.suffix,
                "prefix": ach.prefix,
                "is_active": ach.is_active
            } for ach in home.achievements.all()
            if ach.is_active
            ]
        },
        "is_active": home.is_active,
        "is_hero": home.is_hero,
        "is_services": home.is_services,
        "is_journey": home.is_journey,
        "is_clientele": home.is_clientele,
        "is_associations": home.is_associations,
        "is_affiliations": home.is_affiliations,
        "is_sea_partners": home.is_sea_partners,
        "is_air_partners": home.is_air_partners,
        "is_locations": home.is_locations,
        "is_achievements": home.is_achievements,
        "is_news": home.is_news,

        # "newss": [
        #     {
        #         "id": news.id,
        #         "title": news.title,
        #         "tag": news.tag,
        #         "date": news.date.isoformat(),
        #         "image": news.image.url
        #     } for news in home.newss.all()
        # ]
    }

@api.get("/about/", response=AboutPageSchema)
def get_about(request):
    about = AboutPageContent.objects.first()
    if not about:
        return HttpError(404, "About page content not found.")
    
    # Safely parse values_points if stored as a string
    points = about.values_points
    if isinstance(points, str):
        try:
            points = json.loads(points)
        except json.JSONDecodeError:
            points = []

    return {
        "heading": about.heading,
        "story": {
            "heading": about.story_heading,
            "paragraph": about.story_paragraph,
            "points": points,
            "founder_image_url": about.founder_image.url if about.founder_image else None,
            "para1": about.para1,
            "para2": about.para2
        },
        "mission": {
            "heading": about.mission_heading,
            "paragraph": about.mission_paragraph,
            "image_url": about.mission_image.url if about.mission_image else None,
            "is_active": about.is_mission
        },
        "vision": {
            "heading": about.vision_heading,
            "paragraph": about.vision_paragraph,
            "image_url": about.vision_image.url if about.vision_image else None,
            "is_active": about.is_vision
        },
        "values": {
            "heading": about.values_heading,
            "points": points,
            "image_url": about.values_image.url if about.values_image else None,
            "is_active": about.is_values
        },
        "faq": {
            "heading": about.faq_heading,
            "paragraph": about.faq_paragraph,
            "items": [
                {
                    "id": item.id,
                    "title": item.title,
                    "description": item.description,
                    "is_active" : item.is_active
                } for item in about.faqs.all()
                if item.is_active
            ]
        },
        "achievements": {
            "heading": about.achievements_heading,
            "items": [
            {
                "id": ach.id,
                "title": ach.title,
                "count": ach.count,
                "icon": ach.icon.url,
                "delay": ach.delay,
                "suffix": ach.suffix,
                "prefix": ach.prefix,
                "is_active": ach.is_active
            } for ach in about.achievements.all()
            if ach.is_active
            ]
        },
        "team_heading" : about.team_heading,
        "is_active" : about.is_active,
        "is_story" : about.is_story,
        "is_faq" : about.is_faq,
        "is_achievements" : about.is_achievements
    }

@api.get("/jobs/", response=list[JobSchema])
def jobs(request):
    return Job.objects.all()

@api.get("/jobs/{job_id}/", response=JobSchema)
def get_job(request, job_id: str):
    job = get_object_or_404(Job, id=job_id)
    return {
        "id": job.id,
        "title": job.title,
        "location": job.location,
        "type": job.type,
        "description": job.description,
        "apply_link": job.apply_link,
        "created_at": job.created_at.isoformat(),
        "updated_at": job.updated_at.isoformat()
    }

@api.post("/job-apply/")
def apply_for_job(
    request,
    name: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),
    city: str = Form(...),
    state: str = Form(...),
    department: str = Form(...),
    jobTitle: Optional[str] = Form(None),
    resume: UploadedFile = File(...),
):
    job = Job.objects.filter(title__iexact=jobTitle).first() if jobTitle else None

    application = JobApplication.objects.create(
        name=name,
        phone=phone,
        email=email,
        city=city,
        state=state,
        department=department,
        job=job,
        cv=resume
    )

    return {"success": True, "application_id": application.id}

# newss

@api.get("/news/", response=list[NewsSchema])
def news(request):
    news = News.objects.all()
    return [
        {
            "id": news.id,
            "title": news.title,
            "tag": news.tag,
            "date": news.date.isoformat(),
            "image": news.image.url,
            "short_description": news.short_description,
            "long_description": news.long_description,
            "quote": news.quote,
            "category": news.category,
            "in_between_image": news.in_between_image.url if news.in_between_image else None,
            "created_at": news.created_at.isoformat(),
            "updated_at": news.updated_at.isoformat()
        } for news in news
    ]

@api.get("/news/{news_id}/", response=NewsSchema)
def get_news(request, news_id: str):
    news = get_object_or_404(News, id=news_id)
    return {
        "id": news.id,
        "title": news.title,
        "tag": news.tag,
        "date": news.date.isoformat(),
        "image": news.image.url,
        "short_description": news.short_description,
        "long_description": news.long_description,
        "quote": news.quote,
        "category": news.category,
        "in_between_image": news.in_between_image.url if news.in_between_image else None,
        "created_at": news.created_at.isoformat(),
        "updated_at": news.updated_at.isoformat()
    }

# Service Items

# GET all services
@api.get("/services/", response=list[ServiceSchema])
def get_services(request):
    services = Service.objects.all()
    return [
        {
            **service.__dict__,
            "image": service.image.url if service.image else None,
            "benefits": [{"text": b.text} for b in service.benefits.all()]
        }
        for service in services
    ]

@api.get("/services/{service_id}/", response=ServiceSchema)
def get_service_by_id(request, service_id: str):
    service = get_object_or_404(Service, id=service_id)
    return {
        **service.__dict__,
        "image": service.image.url if service.image else None,
        "benefits": [{"text": b.text} for b in service.benefits.all()]
    }

# VAS endpoints
@api.get("/vas/", response=list[ValueAddedServiceSchema])
def get_vas(request):
    return list(ValueAddedService.objects.all())

# TEAM MEMBERS
@api.get("/team/", response=list[TeamMemberSchema])
def list_team_members(request):
    queryset = TeamMember.objects.filter(is_active=True)
    return [
        {
            "id": member.id,
            "name": member.name,
            "role": member.role,
            "excerpt": member.excerpt,
            "image": member.image.url if member.image else None,
            "bio": member.bio,
            "is_active": member.is_active,
        } for member in queryset
    ]

# Gallery

@api.get("/gallery/", response=list[GalleryEventSchema])
def get_events(request, active_only: bool = True):
    events = GalleryEvent.objects.prefetch_related("photos")
    if active_only:
        events = events.filter(is_active=True)

    result = []
    for event in events:
        photos = event.photos.all()
        if active_only:
            photos = photos.filter(is_active=True)

        result.append({
            "id": event.id,
            "title": event.title,
            "is_active": event.is_active,
            "images": [
                {
                    "id": p.id,
                    "image": p.image.url,
                    "alt": p.alt,
                    "caption": p.caption,
                    "is_active": p.is_active
                } for p in photos
            ]
        })

    return result

# Contact Page
@api.get("/contact/", response=ContactInfoSchema)
def get_contact_info(request):
    contact = ContactInfo.objects.first()
    if not contact:
        raise HttpError(404, "Contact information not found")
    return contact

@api.post("/contact-query/")
def submit_contact_query(request, payload: ContactQuerySchema):
    ContactQuery.objects.create(**payload.dict())
    return {"success": True, "message": "Your message has been received."}

@api.get("/industry-v1/", response=IndustrySpecificationSchema)
def list_page_specs(request):
    return IndustrySpecification.objects.first()

@api.get("/industry/", response=list[IndustrySchema])
def get_industry(request):
    queryset = Industry.objects.filter(is_active=True)
    if not queryset.exists():
        return {"detail": "Not found"}, 404

    # Serialize each Industry object manually
    result = [
        {
            "title": obj.title,
            "type": obj.type,
            "content": obj.content,
            "list_items": obj.list_items,
            "image": request.build_absolute_uri(obj.image.url) if obj.image else "",
            "is_image_left": obj.is_image_left,
            "is_active": obj.is_active,
        }
        for obj in queryset
    ]

    return result
