from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from .constants import (
    COMPANY,
    DEFAULT_BRANDS,
    DEFAULT_PROJECTS,
    DEFAULT_SERVICES,
    DEFAULT_TESTIMONIALS,
    PROCESS_STEPS,
    STATS,
    WHY_CHOOSE_US,
)
from .models import ProductBrand, ProjectGallery, Service, Testimonials


def _services():
    services = list(Service.objects.all())
    if services:
        return services
    return DEFAULT_SERVICES


def _brands():
    brands = list(ProductBrand.objects.all())
    if brands:
        return brands
    return DEFAULT_BRANDS


def _projects():
    projects = list(ProjectGallery.objects.all())
    if projects:
        return projects
    return DEFAULT_PROJECTS


def _testimonials():
    testimonials = list(Testimonials.objects.filter(is_featured=True)[:6])
    if testimonials:
        return testimonials
    return DEFAULT_TESTIMONIALS


def _grouped_brands(brands):
    grouped = {
        "panel": {"title": "Solar Panel Companies", "items": []},
        "inverter": {"title": "Inverter Brands", "items": []},
        "wire": {"title": "Wires & PVC Pipes", "items": []},
        "structure": {"title": "Structure Pipes", "items": []},
    }
    for brand in brands:
        if isinstance(brand, dict):
            category = brand.get("category")
        else:
            category = brand.category
        grouped[category]["items"].append(brand)
    return grouped


def _base_context(page_title: str, meta_description: str, active_page: str):
    services = _services()
    brands = _brands()
    projects = _projects()
    return {
        "page_title": page_title,
        "meta_description": meta_description,
        "active_page": active_page,
        "stats": STATS,
        "services": services,
        "brands": brands,
        "grouped_brands": _grouped_brands(brands),
        "projects": projects,
        "testimonials": _testimonials(),
        "why_choose_points": WHY_CHOOSE_US,
        "process_steps": PROCESS_STEPS,
        "company_details": COMPANY,
    }


def home(request):
    context = _base_context(
        page_title="Sat GreenTech Pvt. Ltd. | Solar EPC Company in Bhesan",
        meta_description=(
            "Sat GreenTech Pvt. Ltd. delivers residential, commercial, industrial, on-grid, off-grid, "
            "and hybrid solar installation with strong structure and fast local service."
        ),
        active_page="home",
    )
    return render(request, "solar_site/home.html", context)


def about(request):
    context = _base_context(
        page_title="About Sat GreenTech Pvt. Ltd.",
        meta_description="Learn about Sat GreenTech Pvt. Ltd., its founders, approach, and commitment to reliable solar EPC work.",
        active_page="about",
    )
    return render(request, "solar_site/about.html", context)


def services_page(request):
    context = _base_context(
        page_title="Solar Services | Sat GreenTech Pvt. Ltd.",
        meta_description="Explore residential, commercial, industrial, on-grid, off-grid, hybrid, service, and solar structure installation.",
        active_page="services",
    )
    return render(request, "solar_site/services.html", context)


def products_page(request):
    context = _base_context(
        page_title="Solar Products | Sat GreenTech Pvt. Ltd.",
        meta_description="Trusted panel, inverter, cable, and structure brands used by Sat GreenTech Pvt. Ltd.",
        active_page="products",
    )
    return render(request, "solar_site/products.html", context)


def projects_page(request):
    context = _base_context(
        page_title="Projects & Gallery | Sat GreenTech Pvt. Ltd.",
        meta_description="See recent residential, commercial, and industrial solar projects and gallery work by Sat GreenTech Pvt. Ltd.",
        active_page="projects",
    )
    return render(request, "solar_site/projects.html", context)


def why_choose_page(request):
    context = _base_context(
        page_title="Why Choose Us | Sat GreenTech Pvt. Ltd.",
        meta_description="See why customers choose Sat GreenTech for strong structure, trusted brands, fast service, and lasting warranties.",
        active_page="why_choose",
    )
    return render(request, "solar_site/why_choose.html", context)


def brands_page(request):
    context = _base_context(
        page_title="Brands We Use | Sat GreenTech Pvt. Ltd.",
        meta_description="Discover the trusted panel, inverter, wire, and structure brands used by Sat GreenTech Pvt. Ltd.",
        active_page="brands",
    )
    return render(request, "solar_site/brands.html", context)


def contact_page(request):
    context = _base_context(
        page_title="Contact Sat GreenTech Pvt. Ltd.",
        meta_description="Contact Sat GreenTech Pvt. Ltd. for solar installation, service, product information, and local support.",
        active_page="contact",
    )
    return render(request, "solar_site/contact.html", context)


def quote_page(request):
    context = _base_context(
        page_title="Get Free Quote | Sat GreenTech Pvt. Ltd.",
        meta_description="Request a free solar quote for residential, commercial, industrial, on-grid, off-grid, or hybrid solar systems.",
        active_page="quote",
    )
    return render(request, "solar_site/quote.html", context)


def robots_txt(request):
    content = "User-agent: *\nAllow: /\nSitemap: /sitemap.xml\n"
    return HttpResponse(content, content_type="text/plain")


def sitemap_xml(request):
    pages = [
        request.build_absolute_uri("/"),
        request.build_absolute_uri("/about/"),
        request.build_absolute_uri("/services/"),
        request.build_absolute_uri("/products/"),
        request.build_absolute_uri("/projects/"),
        request.build_absolute_uri("/why-choose-us/"),
        request.build_absolute_uri("/brands/"),
        request.build_absolute_uri("/contact/"),
        request.build_absolute_uri("/get-free-quote/"),
    ]
    xml = render_to_string("solar_site/sitemap.xml", {"pages": pages})
    return HttpResponse(xml, content_type="application/xml")
