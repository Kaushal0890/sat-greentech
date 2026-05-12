from django.db import migrations


SERVICES = [
    {
        "title": "Residential Solar System",
        "slug": "residential-solar-system",
        "icon": "ri-home-gear-line",
        "short_description": "Smart rooftop systems that lower household power bills and protect against rising energy costs.",
        "description": "Complete residential rooftop solar planning, installation, structure fabrication, wiring, and post-installation support.",
        "sort_order": 1,
        "is_featured": True,
    },
    {
        "title": "Commercial Solar System",
        "slug": "commercial-solar-system",
        "icon": "ri-building-4-line",
        "short_description": "Efficient solar solutions for shops, offices, schools, and commercial premises.",
        "description": "Designed for dependable daytime generation, stronger ROI, and smoother business operations with lower electricity costs.",
        "sort_order": 2,
        "is_featured": True,
    },
    {
        "title": "Industrial Solar System",
        "slug": "industrial-solar-system",
        "icon": "ri-factory-line",
        "short_description": "Heavy-duty systems built for factories, plants, and high-load operational sites.",
        "description": "Engineered structures, quality electrical balance-of-system components, and scalable project planning for industrial energy demand.",
        "sort_order": 3,
        "is_featured": True,
    },
    {
        "title": "On-Grid Solar System",
        "slug": "on-grid-solar-system",
        "icon": "ri-flashlight-line",
        "short_description": "Grid-connected setups for maximum return and optimized consumption savings.",
        "description": "Ideal for customers seeking net-metering benefits, daytime savings, and streamlined rooftop performance.",
        "sort_order": 4,
        "is_featured": True,
    },
    {
        "title": "Off-Grid Solar System",
        "slug": "off-grid-solar-system",
        "icon": "ri-battery-charge-line",
        "short_description": "Independent systems for remote areas and properties needing backup energy security.",
        "description": "Reliable solar plus battery design for places where grid access is limited or power reliability is a concern.",
        "sort_order": 5,
        "is_featured": True,
    },
    {
        "title": "Hybrid Solar System",
        "slug": "hybrid-solar-system",
        "icon": "ri-recycle-line",
        "short_description": "The flexibility of grid power combined with backup storage and solar generation.",
        "description": "Hybrid systems are planned for uninterrupted energy performance and better protection from outages.",
        "sort_order": 6,
        "is_featured": True,
    },
    {
        "title": "Solar Maintenance & Service",
        "slug": "solar-maintenance-service",
        "icon": "ri-tools-line",
        "short_description": "Inspection, cleaning, fault diagnosis, and after-sales support for healthy plant performance.",
        "description": "Regular service improves generation efficiency, extends system life, and reduces unexpected downtime.",
        "sort_order": 7,
        "is_featured": True,
    },
    {
        "title": "Solar Structure Installation",
        "slug": "solar-structure-installation",
        "icon": "ri-hammer-line",
        "short_description": "Strong structure work built for stability, weather resistance, and long-life mounting.",
        "description": "Our team focuses on heavy support structures and neat installation practices for secure rooftop execution.",
        "sort_order": 8,
        "is_featured": True,
    },
]

BRANDS = [
    {"name": "Raaj", "category": "panel", "sort_order": 1, "is_featured": True},
    {"name": "Waaree", "category": "panel", "sort_order": 2, "is_featured": True},
    {"name": "Tata", "category": "panel", "sort_order": 3, "is_featured": True},
    {"name": "Goldi", "category": "panel", "sort_order": 4, "is_featured": True},
    {"name": "Adani", "category": "panel", "sort_order": 5, "is_featured": True},
    {"name": "Polycab", "category": "inverter", "sort_order": 6, "is_featured": True},
    {"name": "Deye", "category": "inverter", "sort_order": 7, "is_featured": True},
    {"name": "Solaryaan", "category": "inverter", "sort_order": 8, "is_featured": True},
    {"name": "Tata", "category": "inverter", "sort_order": 9, "is_featured": True},
    {"name": "Polycab", "category": "wire", "sort_order": 10, "is_featured": True},
    {"name": "Apollo", "category": "structure", "sort_order": 11, "is_featured": True},
]

PROJECTS = [
    {
        "title": "Rooftop Home Solar Installation",
        "slug": "rooftop-home-solar-installation",
        "category": "residential",
        "location": "Bhesan",
        "capacity_kw": "3.00",
        "description": "Residential rooftop system designed for consistent daytime savings and tidy structural finishing.",
        "is_featured": True,
        "sort_order": 1,
    },
    {
        "title": "Commercial Shopline Solar Setup",
        "slug": "commercial-shopline-solar-setup",
        "category": "commercial",
        "location": "Junagadh Road",
        "capacity_kw": "12.00",
        "description": "Commercial solar installation focused on bill reduction, structured cable management, and reliable generation.",
        "is_featured": True,
        "sort_order": 2,
    },
    {
        "title": "Industrial Energy Saving Project",
        "slug": "industrial-energy-saving-project",
        "category": "industrial",
        "location": "Junagadh District",
        "capacity_kw": "50.00",
        "description": "Industrial-grade solar deployment with a strong heavy structure and efficient EPC execution.",
        "is_featured": True,
        "sort_order": 3,
    },
]

TESTIMONIALS = [
    {
        "name": "Hitesh Patel",
        "designation": "Homeowner",
        "content": "Sat GreenTech handled the rooftop work neatly and the service team responded quickly after installation.",
        "rating": 5,
        "is_featured": True,
    },
    {
        "name": "Mehul Vora",
        "designation": "Commercial Customer",
        "content": "We wanted a dependable system and strong structure quality. The execution was timely and professional.",
        "rating": 5,
        "is_featured": True,
    },
    {
        "name": "Vijay Solanki",
        "designation": "Industrial Client",
        "content": "The project planning was practical, the team communicated clearly, and the installation quality met expectations.",
        "rating": 5,
        "is_featured": True,
    },
]


def seed_content(apps, schema_editor):
    Service = apps.get_model("solar_site", "Service")
    ProductBrand = apps.get_model("solar_site", "ProductBrand")
    ProjectGallery = apps.get_model("solar_site", "ProjectGallery")
    Testimonials = apps.get_model("solar_site", "Testimonials")

    for item in SERVICES:
        Service.objects.update_or_create(slug=item["slug"], defaults=item)

    for item in BRANDS:
        ProductBrand.objects.update_or_create(
            name=item["name"],
            category=item["category"],
            defaults=item,
        )

    for item in PROJECTS:
        ProjectGallery.objects.update_or_create(slug=item["slug"], defaults=item)

    for item in TESTIMONIALS:
        Testimonials.objects.update_or_create(
            name=item["name"],
            designation=item["designation"],
            defaults=item,
        )


def unseed_content(apps, schema_editor):
    Service = apps.get_model("solar_site", "Service")
    ProductBrand = apps.get_model("solar_site", "ProductBrand")
    ProjectGallery = apps.get_model("solar_site", "ProjectGallery")
    Testimonials = apps.get_model("solar_site", "Testimonials")

    Service.objects.filter(slug__in=[item["slug"] for item in SERVICES]).delete()
    ProductBrand.objects.filter(
        name__in=[item["name"] for item in BRANDS],
        category__in=[item["category"] for item in BRANDS],
    ).delete()
    ProjectGallery.objects.filter(slug__in=[item["slug"] for item in PROJECTS]).delete()
    Testimonials.objects.filter(name__in=[item["name"] for item in TESTIMONIALS]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("solar_site", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_content, unseed_content),
    ]
