# KultureKorner_postArt/models.py
from django.db import models


class PostArt(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, default="")
    post_date = models.DateField()
    style = models.CharField(max_length=20, blank=True, null=True, default="")
    purchase_link = models.CharField(max_length=100, blank=True, null=True, default="")
    story = models.TextField(max_length=5000, blank=False, null=False, default="")
    image_1 = models.ImageField(upload_to="artImage", blank=True, null=True)
    image_2 = models.ImageField(upload_to="artImage", blank=True, null=True)
    image_3 = models.ImageField(upload_to="artImage", blank=True, null=True)
    image_4 = models.ImageField(upload_to="artImage", blank=True, null=True)
    image_5 = models.ImageField(upload_to="artImage", blank=True, null=True)
    image_6 = models.ImageField(upload_to="artImage", blank=True, null=True)

    def __str__(self):
        return self.title
