# schemas.py
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, HttpUrl, Field, ConfigDict, EmailStr
from datetime import datetime, date

from ninja.files import UploadedFile

class IndustrySchema(BaseModel):
    title: str
    type: str
    content: Optional[str] = None
    list_items: Optional[List[str]] = None
    image: str
    is_image_left: bool
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

class IndustrySpecificationSchema(BaseModel):
    id: UUID
    is_industry: bool

    model_config = ConfigDict(from_attributes=True)

class ServiceItemSchema(BaseModel):
    id: UUID
    title: str
    image: str

class ClienteleItemSchema(BaseModel):
    logo: str

class LocationSchema(BaseModel):
    id: UUID
    city: str
    address: str
    phone: List[str]
    email: str
    image: str
    place: str

class AchievementSchema(BaseModel):
    id: UUID
    title: str
    count: int
    icon: dict
    delay: str = ".4s"
    suffix: str = ""
    prefix: str = ""
    is_active: bool

class NewsSchema(BaseModel):
    id: UUID
    title: str
    tag: List[str]
    date: date
    image: str
    short_description: str
    long_description: str
    category: str
    quote: Optional[str] = None
    in_between_image: Optional[str] = None
    created_at: datetime
    updated_at: datetime    

    model_config = ConfigDict(from_attributes=True)

class ServiceItem(BaseModel):
    id: UUID
    title: str
    image: Optional[str]

class ServicesSection(BaseModel):
    heading: Optional[str] = None
    items: List[ServiceItem]

class HomePageSchema(BaseModel):
    hero: dict
    services: ServicesSection
    journey: dict
    clientele: dict
    associations: dict
    affiliations: dict
    sea_partners: dict
    air_partners: dict
    locations: dict
    achievements: dict
    is_active: bool
    is_hero: bool
    is_services: bool
    is_journey: bool
    is_clientele: bool
    is_associations: bool
    is_affiliations: bool
    is_sea_partners: bool
    is_air_partners: bool
    is_locations: bool
    is_achievements: bool
    is_news: bool



# ABOUT PAGE SCHEMA
class StorySchema(BaseModel):
    heading: str
    paragraph: str
    points: List[str]
    founder_image_url: Optional[str]  # Optional, could be None if no image
    para1: str
    para2: str

class MissionSchema(BaseModel):
    heading: str
    paragraph: str
    is_active: bool
    image_url: Optional[str]  # Optional, could be None if no image

class FAQItemSchema(BaseModel):
    id: int
    title: str
    description: str
    is_active: bool

class FAQSchema(BaseModel):
    heading: str
    paragraph: str
    items: List[FAQItemSchema]

class ValuesSchema(BaseModel):
    heading: str
    points: List[str]
    is_active: bool
    image_url: Optional[str]  # Optional, could be None if no image

class AboutPageSchema(BaseModel):
    heading: str
    story: StorySchema
    mission: MissionSchema
    vision: MissionSchema  # Assuming you want 'vision' to have a similar structure as 'mission'
    values: ValuesSchema
    faq: FAQSchema
    achievements: dict
    team_heading: str
    is_active: bool
    is_story: bool
    is_faq:  bool
    is_achievements: bool
    

# JOB PAGE SCHEMA
class JobSchema(BaseModel):
    id: UUID
    title: str
    location: str
    type: str
    description: str
    apply_link: str
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)


class JobApplicationSchema(BaseModel):
    name: str
    phone: str
    email: str
    city: str
    state: str
    department: str
    job_id: Optional[UUID] = None
    resume: UploadedFile

# SERVICE PAGE SCHEMA
class ServiceBenefitSchema(BaseModel):
    text: str

class ServiceSchema(BaseModel):
    id: UUID
    title: str
    image: str
    description: str
    icon: str
    description1: str
    heading: str
    description2: str
    benefits: List[ServiceBenefitSchema]

    model_config = {"from_attributes": True}


class ValueAddedServiceSchema(BaseModel):
    id: UUID
    title: str
    para1: str
    para2: str

    model_config = {"from_attributes": True}

# TEAM PAGE SCHEMA
class TeamMemberSchema(BaseModel):
    id: UUID
    name: str
    role: str
    excerpt: str
    image: str  # You may convert to `HttpUrl` if using full URLs
    bio: str
    is_active: bool

    model_config = {"from_attributes": True}

# Gallery Schema

class GalleryPhotoSchema(BaseModel):
    id: UUID
    image: str
    alt: str
    caption: str
    is_active: bool

class GalleryEventSchema(BaseModel):
    id: UUID
    title: str
    is_active: bool
    images: List[GalleryPhotoSchema]

# Contact Page
class ContactInfoSchema(BaseModel):
    id: UUID
    title: str
    address_title: str
    address: str
    contact_title: str
    phone_label: str
    phone: str
    phone_href: str
    email_label: str
    email: str
    email_href: str
    iframe: str

    model_config = ConfigDict(from_attributes=True)

class ContactQuerySchema(BaseModel):
    first_name: str = Field(..., min_length=1)
    last_name: str = Field(..., min_length=1)
    phone: str = Field(..., min_length=5)
    email: EmailStr
    message: str = Field(..., min_length=5)

    model_config = ConfigDict(from_attributes=True)