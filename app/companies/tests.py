from django.test import TestCase

from .models import Company


class CompaniesTestCase(TestCase):
    fixtures = ['companies.json', 'users.json']

    def test_company_legal_name(self):
        for company in Company.objects.all():
            self.assertEqual(company.legal_name, company.name.upper())

    def test_company_creation(self):
        data = {
            'name': 'TEST-COMPANY',
            'address': '5 Main street'
        }
        company = Company.objects.create(**data)
        self.assertEqual(company.name, data['name'])
