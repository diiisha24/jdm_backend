from django.contrib import admin
from .models import HomePageContent, ServiceItem, ClienteleItem, AssociationItem, AffiliationItem, SeaPartnerItem, AirPartnerItem, Location, Achievement, News, AboutPageContent, FAQ, Job, JobApplication, Service, ServiceBenefit, ValueAddedService, TeamMember, GalleryPhoto, GalleryEvent, ContactInfo, ContactQuery, IndustrySpecification, Industry
from django.utils.html import format_html
from django import forms
from django.core.exceptions import ValidationError
# from django.contrib.admin import ModelAdmin

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'is_active', 'is_image_left', 'created_at')
    list_filter = ('type', 'is_active', 'is_image_left')
    search_fields = ('title',)

@admin.register(IndustrySpecification)
class PageSpecificationAdmin(admin.ModelAdmin):
    list_display = ('is_industry',)
    list_filter = ('is_industry',)

class HomePageContentForm(forms.ModelForm):
    class Meta:
        model = HomePageContent
        fields = '__all__'

    def clean_selected_services(self):
        selected = self.cleaned_data.get('selected_services')
        if selected and selected.count() > 6:
            raise ValidationError("You can only select up to 6 services.")
        return selected

class ServiceItemInline(admin.TabularInline):
    model = ServiceItem
    extra = 1
    readonly_fields = ['preview']  # This makes the image preview read-only

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="auto" style="object-fit: contain;" />', obj.image.url)
        return "-"
    preview.short_description = "Image Preview" 
 
class ClienteleItemInline(admin.TabularInline):
    model = ClienteleItem
    extra = 1  # Number of empty forms to display for quick addition
    # max_num = 6  # Maximum number of items that can be added
    readonly_fields = ['preview']

    def preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="100" />', obj.logo.url)
        return ""

class AssociationItemInline(admin.TabularInline):
    model = AssociationItem
    extra = 1  # Number of empty forms to display for quick addition
    # max_num = 6  # Maximum number of items that can be added
    readonly_fields = ['preview']

    def preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="100" />', obj.logo.url)
        return ""

class AffiliationItemInline(admin.TabularInline):
    model = AffiliationItem
    extra = 1  # Number of empty forms to display for quick addition
    # max_num = 6  # Maximum number of items that can be added
    readonly_fields = ['preview']

    def preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="100" />', obj.logo.url)
        return ""

class SeaPartnerItemInline(admin.TabularInline):
    model = SeaPartnerItem
    extra = 1  # Number of empty forms to display for quick addition
    # max_num = 6  # Maximum number of items that can be added
    readonly_fields = ['preview']

    def preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="100" />', obj.logo.url)
        return ""

class AirPartnerItemInline(admin.TabularInline):
    model = AirPartnerItem
    extra = 1  # Number of empty forms to display for quick addition
    # max_num = 6  # Maximum number of items that can be added
    readonly_fields = ['preview']

    def preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="100" />', obj.logo.url)
        return ""

class LocationInline(admin.TabularInline):
    model = Location
    extra = 1  # Number of empty forms to display for quick addition
    # max_num = 6  # Maximum number of items that can be added
    readonly_fields = ['preview']  # This makes the image preview read-only

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="auto" style="object-fit: contain;" />', obj.image.url)
        return "-"
    preview.short_description = "Image Preview"


class AchievementInline(admin.TabularInline):
    model = Achievement
    extra = 1  # Number of empty forms to display for quick addition
    # max_num = 6  # Maximum number of items that can be added

    # def preview(self, obj):
    #     if obj.image:
    #         return format_html('<img src="{}" width="100" />', obj.image.url)
    #     return ""

# @admin.register(HomePageContent)
# class HomePageContentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'created_at', 'updated_at')
#     search_fields = ('services_heading', 'journey_heading', 'clientele_heading')
#     inlines = [ServiceItemInline, ClienteleItemInline, AssociationItemInline, AffiliationItemInline, SeaPartnerItemInline, AirPartnerItemInline, LocationInline, AchievementInline]
#     readonly_fields = ('created_at', 'updated_at')

@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    form = HomePageContentForm
    list_display = ('id', 'created_at', 'updated_at')
    search_fields = ('services_heading', 'journey_heading', 'clientele_heading')
    inlines = [ServiceItemInline, ClienteleItemInline, AssociationItemInline, AffiliationItemInline, AirPartnerItemInline, LocationInline, AchievementInline]
    readonly_fields = ('created_at', 'updated_at')



@admin.register(News)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'date')
    search_fields = ('title', 'tag')
    readonly_fields = ('id',)


# About Page Admin Registration
class FAQInline(admin.TabularInline):
    model = FAQ
    extra = 1  # Displays one extra empty FAQ form for quick addition

# Registering the AboutPageContent model with customized admin display
# @admin.register(AboutPageContent)
# class AboutPageContentAdmin(admin.ModelAdmin):
#     # Fields to display in the list view of the admin panel for AboutPageContent
#     list_display = ("heading", "story_heading", "mission_heading", "vision_heading")
    
#     # Add the inline FAQs so they can be edited in the same form as AboutPageContent
#     inlines = [FAQInline]
    
#     # Make created_at and updated_at fields read-only (not editable in admin)
#     readonly_fields = ("created_at", "updated_at","mission_image_preview", "vision_image_preview", "values_image_preview", "founder_image_preview")
#     def mission_image_preview(self, obj):
#         if obj.mission_image:
#             return format_html('<img src="{}" width="150" />', obj.mission_image.url)
#         return "-"
#     mission_image_preview.short_description = "Mission Image"

#     def vision_image_preview(self, obj):
#         if obj.vision_image:
#             return format_html('<img src="{}" width="150" />', obj.vision_image.url)
#         return "-"
#     vision_image_preview.short_description = "Vision Image"

#     def values_image_preview(self, obj):
#         if obj.values_image:
#             return format_html('<img src="{}" width="150" />', obj.values_image.url)
#         return "-"
#     values_image_preview.short_description = "Values Image"

#     def founder_image_preview(self, obj):
#         if obj.founder_image:
#             return format_html('<img src="{}" width="150" />', obj.founder_image.url)
#         return "-"
#     founder_image_preview.short_description = "Founder Image"

@admin.register(AboutPageContent)
class AboutPageContentAdmin(admin.ModelAdmin):
    inlines = [FAQInline, AchievementInline]
    readonly_fields = ("created_at", "updated_at", "mission_image_preview", "vision_image_preview", "values_image_preview", "founder_image_preview")

    fieldsets = (
        (None, {
            'fields': (
                'heading',
                'story_heading',
                'story_paragraph',
                ('founder_image', 'founder_image_preview'),
                'para1',
                'para2',
                'mission_heading',
                'mission_paragraph',
                ('mission_image', 'mission_image_preview'),
                'vision_heading',
                'vision_paragraph',
                ('vision_image', 'vision_image_preview'),
                'values_heading',
                ('values_image', 'values_image_preview'),
                'values_points',
                'faq_heading',
                'faq_paragraph',
                'team_heading',
                'is_active',
                'is_mission',
                'is_vision',
                'is_values',
                'is_story',
                'is_achievements',
                'is_faq',
                ('created_at', 'updated_at'),
            )
        }),
    )

    def mission_image_preview(self, obj):
        if obj.mission_image:
            return format_html('<img src="{}" width="150" />', obj.mission_image.url)
        return "-"
    mission_image_preview.short_description = "Preview"

    def vision_image_preview(self, obj):
        if obj.vision_image:
            return format_html('<img src="{}" width="150" />', obj.vision_image.url)
        return "-"
    vision_image_preview.short_description = "Preview"

    def values_image_preview(self, obj):
        if obj.values_image:
            return format_html('<img src="{}" width="150" />', obj.values_image.url)
        return "-"
    values_image_preview.short_description = "Preview"

    def founder_image_preview(self, obj):
        if obj.founder_image:
            return format_html('<img src="{}" width="150" />', obj.founder_image.url)
        return "-"
    founder_image_preview.short_description = "Preview"

# Registering the FAQ model separately, though it’s already manageable inline
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    # Fields to show in the list view of FAQs in the admin panel
    list_display = ("title", "description")  
    # Enables a search box that filters FAQs by title
    search_fields = ("title",)

# Registering the Job model for the Career page
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "type", "created_at")
    search_fields = ("title", "location", "type")
    list_filter = ("type", "location")

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'job', 'created_at')
    search_fields = ('name', 'email', 'job__title')

# Registering The ServiceItem model
class BenefitInline(admin.TabularInline):
    model = ServiceBenefit
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [BenefitInline]
    list_display = ('title',)

admin.site.register(ValueAddedService)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "is_active", "preview_image")
    list_filter = ("is_active",)
    readonly_fields = ("preview_image",)

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "-"
    preview_image.short_description = "Image"

class GalleryPhotoInline(admin.TabularInline):
    model = GalleryPhoto
    extra = 1
    readonly_fields = ("preview_image",)

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "-"
    preview_image.short_description = "Image"

@admin.register(GalleryEvent)
class GalleryEventAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    inlines = [GalleryPhotoInline]
    

# Contact Page
@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("title", "email", "phone")
    search_fields = ("title", "email", "phone", "address")

@admin.register(ContactQuery)
class ContactQueryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('first_name', 'last_name', 'email', 'phone', 'message', 'created_at')

    def has_add_permission(self, request):
        return False  # Prevent manual additions via admin (optional)

    def has_change_permission(self, request, obj=None):
        return False  # Make entries read-only (optional)