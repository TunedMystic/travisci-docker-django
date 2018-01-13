from django.db import models

from common.models import BaseModel


class Company(BaseModel):
    '''
    Company model.
    '''
    name = models.CharField(
        max_length=200,
        verbose_name='Name',
        help_text='Asset Name',
    )

    address = models.CharField(
        max_length=300,
        verbose_name='Address',
        help_text='Asset Address',
    )

    def __str__(self):
        return self.name

    @property
    def legal_name(self):
        return self.name.upper()

    class Meta:
        verbose_name_plural = 'Companies'
        ordering = ('-created_on',)
