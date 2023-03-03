from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, userid, name, address, phone, phone_check, email, email_check, date_of_birth, level, recommendation, account, password=None):
        if not userid:
            raise ValueError('userid를 입력해주세요.')

        user = self.model(
            userid=userid,
            name=name,
            address=address,
            phone=phone,
            phone_check=phone_check,
            email=self.normalize_email(email),
            email_check=email_check,
            date_of_birth=date_of_birth,
            level=level,
            recommendation=recommendation,
            account=account,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, userid, name, address, phone, phone_check, email, email_check, date_of_birth, level, recommendation, account, password):
        user = self.create_user(
            userid,
            password=password,
            name=name,
            address=address,
            phone=phone,
            phone_check=phone_check,
            email=email,
            email_check=email_check,
            date_of_birth=date_of_birth,
            level=level,
            recommendation=recommendation,
            account=account,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    userid = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=10)
    address = models.TextField()
    phone = models.CharField(max_length=15, unique=True)
    phone_check = models.BooleanField(default=False)
    email = models.EmailField(max_length=255, unique=True)
    email_check = models.BooleanField(default=False)
    date_of_birth = models.DateField()
    level = models.CharField(max_length=20)
    recommendation = models.CharField(max_length=20)
    account = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'userid'
    REQUIRED_FIELDS = ['name', 'address', 'phone', 'phone_check', 'email', 'email_check', 'date_of_birth', 'level', 'recommendation', 'account']

    def __str__(self):
        return self.userid

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
