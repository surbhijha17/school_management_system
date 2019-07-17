from django.utils import six, timezone
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import(
	AbstractUser,UserManager
	)



class CustomUserManager(UserManager):

    def _create_user(self,  email, password,
                     is_staff, is_superuser, username=None,**extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None,username=None, **extra_fields):
        return self._create_user( email, password, False, False,None,
                                 **extra_fields)

    def create_superuser(self,  email, password,username=None ,**extra_fields):
        return self._create_user( email, password, True, True,None,
                                 **extra_fields)


class CustomUser(AbstractUser):
	email=models.EmailField(unique=True)
	username=models.CharField(max_length=10,blank=True,null=True)
	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
	USERNAME_FIELD='email'
	REQUIRED_FIELDS=[]
	def __str__(self):
		return self.first_name

	def send_email(self, request, queryset):
		form = SendEmailForm(initial={'users': queryset})
		return render(request, 'accounts/send_email.html', {'form': form})
	objects=CustomUserManager()
# Create your models here.
