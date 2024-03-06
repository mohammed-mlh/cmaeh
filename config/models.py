from django.db import models

class Config(models.Model):
  hero_title = models.CharField(max_length=100, null=True)
  hero_image = models.ImageField()
  facebook_page = models.CharField(max_length=100)
  instagram_page = models.CharField(max_length=100)
  whatsapp_number = models.CharField(max_length=100)
  cta_title = models.CharField(max_length=100)
  cta_description = models.TextField()
  cta_image = models.ImageField()
  
class Testimonial(models.Model):
  text = models.TextField()
  client_name = models.CharField(max_length=50)