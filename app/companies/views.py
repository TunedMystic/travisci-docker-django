from django.shortcuts import render

from .models import Company


def companies(request):
    companies = Company.objects.all()[:10]
    return render(
        request,
        'companies/companies.html',
        {'companies': companies}
    )
