import uuid

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    '''
    The BaseModel class abstracts basic model fields
    and functionality. All models in this application
    should inherit from BaseModel.
    '''

    # UUID as primary key.
    id = models.UUIDField(
        db_index=True,
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        default=timezone.now
    )

    @property
    def id_(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if self.id:
            self.updated_on = timezone.now()
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
