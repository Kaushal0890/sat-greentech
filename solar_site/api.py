from decimal import Decimal

from fastapi import FastAPI
from pydantic import BaseModel, Field

from .models import ContactInquiry, ProductBrand, ProjectGallery, QuoteRequest, Service


class ContactPayload(BaseModel):
    name: str = Field(..., min_length=2, max_length=120)
    phone: str = Field(..., min_length=10, max_length=20)
    email: str | None = Field(default=None, max_length=254)
    address: str | None = Field(default="", max_length=255)
    system_type: str | None = Field(default="", max_length=120)
    message: str = Field(..., min_length=4)


class QuotePayload(BaseModel):
    name: str = Field(..., min_length=2, max_length=120)
    phone: str = Field(..., min_length=10, max_length=20)
    email: str | None = Field(default=None, max_length=254)
    address: str = Field(..., min_length=5, max_length=255)
    system_type: str = Field(..., min_length=3, max_length=120)
    monthly_bill: str | None = Field(default="", max_length=80)
    installation_type: str | None = Field(default="", max_length=80)
    message: str | None = Field(default="", max_length=2000)


api_app = FastAPI(
    title="Sat GreenTech API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


def _brand_payload(brand: ProductBrand) -> dict:
    return {
        "id": brand.id,
        "name": brand.name,
        "category": brand.category,
        "category_label": brand.get_category_display(),
        "description": brand.description,
        "website": brand.website,
        "logo": brand.logo.url if brand.logo else None,
    }


def _project_payload(project: ProjectGallery) -> dict:
    capacity_value = None
    if isinstance(project.capacity_kw, Decimal):
        capacity_value = float(project.capacity_kw)
    elif project.capacity_kw is not None:
        capacity_value = float(project.capacity_kw)
    return {
        "id": project.id,
        "title": project.title,
        "slug": project.slug,
        "category": project.category,
        "category_label": project.get_category_display(),
        "location": project.location,
        "capacity_kw": capacity_value,
        "completion_date": project.completion_date.isoformat() if project.completion_date else None,
        "description": project.description,
        "image": project.image.url if project.image else None,
    }


@api_app.get("/services")
def get_services():
    return [
        {
            "id": service.id,
            "title": service.title,
            "slug": service.slug,
            "icon": service.icon,
            "short_description": service.short_description,
            "description": service.description,
        }
        for service in Service.objects.all()
    ]


@api_app.get("/projects")
def get_projects():
    return [_project_payload(project) for project in ProjectGallery.objects.all()]


@api_app.get("/brands")
def get_brands():
    return [_brand_payload(brand) for brand in ProductBrand.objects.all()]


@api_app.post("/contact")
def create_contact(payload: ContactPayload):
    inquiry = ContactInquiry.objects.create(
        name=payload.name,
        phone=payload.phone,
        email=payload.email or "",
        address=payload.address or "",
        system_type=payload.system_type or "",
        message=payload.message,
    )
    return {"success": True, "message": "Thank you. Our team will contact you shortly.", "id": inquiry.id}


@api_app.post("/quote")
def create_quote(payload: QuotePayload):
    quote = QuoteRequest.objects.create(
        name=payload.name,
        phone=payload.phone,
        email=payload.email or "",
        address=payload.address,
        system_type=payload.system_type,
        monthly_bill=payload.monthly_bill or "",
        installation_type=payload.installation_type or "",
        message=payload.message or "",
    )
    return {"success": True, "message": "Quote request submitted successfully.", "id": quote.id}
