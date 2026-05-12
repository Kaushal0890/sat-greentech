from django.db import models
from django.utils.text import slugify


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Service(TimeStampedModel):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    icon = models.CharField(max_length=80, blank=True)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    sort_order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["sort_order", "title"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductBrand(TimeStampedModel):
    PANEL = "panel"
    INVERTER = "inverter"
    WIRE = "wire"
    STRUCTURE = "structure"
    CATEGORY_CHOICES = [
        (PANEL, "Solar Panel"),
        (INVERTER, "Inverter"),
        (WIRE, "Wires / PVC Pipes"),
        (STRUCTURE, "Structure Pipes"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to="brands/", blank=True, null=True)
    sort_order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["sort_order", "name"]

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class ProjectGallery(TimeStampedModel):
    RESIDENTIAL = "residential"
    COMMERCIAL = "commercial"
    INDUSTRIAL = "industrial"
    ONGRID = "ongrid"
    HYBRID = "hybrid"
    CATEGORY_CHOICES = [
        (RESIDENTIAL, "Residential"),
        (COMMERCIAL, "Commercial"),
        (INDUSTRIAL, "Industrial"),
        (ONGRID, "On-Grid"),
        (HYBRID, "Hybrid"),
    ]

    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=120)
    capacity_kw = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "-created_at", "title"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ContactInquiry(TimeStampedModel):
    NEW = "new"
    CONTACTED = "contacted"
    CLOSED = "closed"
    STATUS_CHOICES = [
        (NEW, "New"),
        (CONTACTED, "Contacted"),
        (CLOSED, "Closed"),
    ]

    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    system_type = models.CharField(max_length=120, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NEW)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.phone}"


class QuoteRequest(TimeStampedModel):
    NEW = "new"
    REVIEWING = "reviewing"
    QUOTED = "quoted"
    STATUS_CHOICES = [
        (NEW, "New"),
        (REVIEWING, "Reviewing"),
        (QUOTED, "Quoted"),
    ]

    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255)
    system_type = models.CharField(max_length=120)
    monthly_bill = models.CharField(max_length=80, blank=True)
    installation_type = models.CharField(max_length=80, blank=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NEW)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.system_type}"


class Testimonials(TimeStampedModel):
    name = models.CharField(max_length=120)
    designation = models.CharField(max_length=120, blank=True)
    company = models.CharField(max_length=120, blank=True)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Testimonials"
        ordering = ["-is_featured", "-created_at", "name"]

    def __str__(self):
        return self.name
