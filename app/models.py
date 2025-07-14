from django.db import models
#from django.contrib.postgres.fields import JSONField  # for PostgreSQL


class WheelSpecification(models.Model):
    formNumber = models.CharField(max_length=100)
    submittedBy = models.CharField(max_length=100)
    submittedDate = models.DateField()
    fields = models.JSONField()  # or use JSONField from postgres.fields for Django < 3.1

    def __str__(self):
        return self.formNumber
