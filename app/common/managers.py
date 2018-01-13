from django.db import models


class BaseQuerySet(models.query.QuerySet):

    def flat_ids(self):
        '''
        Returns a list of queryset ids.
        '''
        return [
            pk.__str__() for pk in
            self.values_list('id', flat=True)
        ]
