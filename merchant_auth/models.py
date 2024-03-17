from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Role(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Merchant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    phone_country_code = models.CharField(max_length=10)
    phone_verified = models.BooleanField(default=False)
    support_email = models.EmailField()
    email_verified = models.BooleanField(default=False)
    merchant_id = models.CharField(max_length=32)   
    merchant_name = models.CharField(max_length=16)
    
    def __str__(self) -> str:
        return self.merchant_name or self.merchant_id
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Merchant.objects.create(
            user=instance,
            merchant_id=instance.username)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.merchant.save()


class Application(models.Model):
    merchant = models.ForeignKey("Merchant", on_delete=models.CASCADE)
    application_id = models.CharField(max_length=64)
    application_name = models.CharField(max_length=64)
    website_url = models.URLField(max_length=64)
    secret = models.CharField(max_length=64)
    is_active = models.BooleanField()

    def __str__(self) -> str:
        return self.application_name


class Customer(models.Model):
    application = models.ForeignKey("Application", on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.customer_id
