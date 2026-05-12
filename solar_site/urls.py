from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services_page, name="services"),
    path("products/", views.products_page, name="products"),
    path("projects/", views.projects_page, name="projects"),
    path("why-choose-us/", views.why_choose_page, name="why_choose"),
    path("brands/", views.brands_page, name="brands"),
    path("contact/", views.contact_page, name="contact"),
    path("get-free-quote/", views.quote_page, name="quote"),
    path("robots.txt", views.robots_txt, name="robots_txt"),
    path("sitemap.xml", views.sitemap_xml, name="sitemap_xml"),
]
