from django.contrib import admin

from .models import ContactInquiry, ProductBrand, ProjectGallery, QuoteRequest, Service, Testimonials


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "sort_order", "is_featured", "updated_at")
    list_filter = ("is_featured",)
    search_fields = ("title", "short_description", "description")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("sort_order", "title")


@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "sort_order", "is_featured", "updated_at")
    list_filter = ("category", "is_featured")
    search_fields = ("name", "description")
    ordering = ("sort_order", "name")


@admin.register(ProjectGallery)
class ProjectGalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "location", "capacity_kw", "is_featured", "updated_at")
    list_filter = ("category", "is_featured")
    search_fields = ("title", "location", "description")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("sort_order", "-created_at")


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "system_type", "status", "created_at")
    list_filter = ("status", "system_type", "created_at")
    search_fields = ("name", "phone", "address", "message")
    ordering = ("-created_at",)


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "system_type", "monthly_bill", "status", "created_at")
    list_filter = ("status", "system_type", "created_at")
    search_fields = ("name", "phone", "address", "message")
    ordering = ("-created_at",)


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "rating", "is_featured", "created_at")
    list_filter = ("is_featured", "rating")
    search_fields = ("name", "designation", "content")
    ordering = ("-is_featured", "-created_at")
