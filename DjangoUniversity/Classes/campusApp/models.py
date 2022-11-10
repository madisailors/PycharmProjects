from django.db import models

class UniversityCampus(models.Model):
    campusName = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=25, default="", blank=True, null=False)
    campusID = models.IntegerField(default="", blank=True, null=False)

    object = models.Manager()

    def __str__(self):
        display_campus = '{0.campusName}: {0.state}'
        return display_campus.format(self)


    class Meta:
        verbose_name_plural = "University Campuses"
