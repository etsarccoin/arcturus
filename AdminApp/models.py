from django.db import models

class OurSerice(models.Model):
    description = models.TextField()
    updated_at = models.DateTimeField()


class SocialMedialLink(models.Model):
    facebook_link = models.TextField()
    twitter_link = models.TextField()
    googleplus = models.TextField()
    linkedin = models.TextField()

