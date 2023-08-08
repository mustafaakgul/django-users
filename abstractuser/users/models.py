from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

#Set the USERNAME_FIELD -- which defines the unique identifier for the User model -- to email
class CustomUser(AbstractUser):
    username = None   #Removed the username field
    email = models.EmailField(_('email address'), unique=True)   #Made the email field required and unique
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email  #self.username


"""
class CustomUser(AbstractUser):
    display_name = models.CharField(verbose_name=_("Display name"), max_length=30, help_text=_("Will be shown e.g. when commenting"))
    date_of_birth = models.DateField(verbose_name=_("Date of birth"), blank=True, null=True)
    address1 = models.CharField(verbose_name=_("Address line 1"), max_length=1024, blank=True, null=True)
    address2 = models.CharField(verbose_name=_("Address line 2"), max_length=1024, blank=True, null=True)
    zip_code = models.CharField(verbose_name=_("Postal Code"), max_length=12, blank=True, null=True)
    city = models.CharField(verbose_name=_("City"), max_length=1024, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=_("Enter a valid international mobile phone number starting with +(country code)"))
    mobile_phone = models.CharField(validators=[phone_regex], verbose_name=_("Mobile phone"), max_length=17, blank=True, null=True)
    additional_information = models.CharField(verbose_name=_("Additional information"), max_length=4096, blank=True, null=True)
    photo = models.ImageField(verbose_name=_("Photo"), upload_to='photos/', default='photos/default-user-avatar.png')

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"
"""