from ninja import NinjaAPI
from .models import Sector, Country
from .schemas import SectorSchema, CountrySchema
# from .
from django.conf import settings

api = NinjaAPI(csrf=True, urls_namespace="clientele-api")



def get_logo_data(logos):
    return [
        {
            "id": logo.id,
            "src": settings.MEDIA_URL + str(logo.image),
            "alt": logo.alt_text or f"Logo {logo.id}"
        }
        for logo in logos
    ]


@api.get("/sectors/", response=list[SectorSchema])
def get_sectors(request):
    sectors = Sector.objects.prefetch_related("logos").all()
    return [
        {
            "name": sector.name,
            "logos": get_logo_data(sector.logos.all())
        }
        for sector in sectors
    ]


@api.get("/countries/", response=list[CountrySchema])
def get_countries(request):
    countries = Country.objects.prefetch_related("subcountries__logos").all()
    result = []
    for country in countries:
        sub_data = []
        for sub in country.subcountries.all():
            sub_data.append({
                "name": sub.name,
                "logos": get_logo_data(sub.logos.all())
            })

        result.append({
            "name": country.name,
            "subcountries": sub_data if sub_data else None
        })

    return result