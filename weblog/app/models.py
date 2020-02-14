"""
Definition of models.
"""

from django.db import models

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_index=True, blank=False, null=False)
    updated = models.DateTimeField(db_index=True, blank=False, auto_now=True)

    def set_fields_from_dict(self, fields, data, exclusion_list=None):
        """ apply a dictionary to the fields of an object """
        
        if exclusion_list is None:
            exclusion_list = []

        for key in data:
            if key in exclusion_list:
                continue
            if (key in fields) and (key not in exclusion_list):
                if type(data[key]) is set:
                    data[key] = list(data[key])
                setattr(self, key, data[key])

    class Meta:
        abstract = True
        default_permissions = ()
        ordering = ("-created",)
