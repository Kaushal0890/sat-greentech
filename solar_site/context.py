from solar_site.constants import COMPANY


def company_context(request):
    return {"company": COMPANY}
