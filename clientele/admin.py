from django.contrib import admin
from .models import Sector, SectorLogo, Country, SubCountry, CountryLogo
from django.utils.html import format_html

# Register your models here.
# Registering the ClienteleItem model
class SectorLogoInline(admin.TabularInline):
    model = SectorLogo
    extra = 1
    readonly_fields = ["preview"]

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return ""
    preview.short_description = "Preview"


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [SectorLogoInline]


class CountryLogoInline(admin.TabularInline):
    model = CountryLogo
    extra = 1
    readonly_fields = ["preview"]

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return ""
    preview.short_description = "Preview"


class SubCountryInline(admin.TabularInline):
    model = SubCountry
    extra = 1


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [SubCountryInline]


@admin.register(SubCountry)
class SubCountryAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
    inlines = [CountryLogoInline]