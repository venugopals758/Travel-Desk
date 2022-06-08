from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


Group.add_to_class('priority',models.IntegerField(null=True))




class User(AbstractUser):
    phone = models.BigIntegerField(null=True)
    gender=models.CharField(max_length=30,null=True)
    designation=models.CharField(max_length=100,null=True)
    pin_number=models.CharField(max_length=15,null=True)
    image = models.FileField(upload_to='media/user/profileimages',null=True)
    campus = models.CharField(max_length=100, null=True)
    institution = models.CharField(max_length=100, null=True)
    department = models.CharField(max_length=100, null=True)
    emp_id = models.CharField(max_length=15,null=True)
    dob = models.CharField(max_length=50,null=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="user_set",
        related_query_name="user",
        through="UserGroups"
    )
    class Meta:
        db_table = "users"
    def __str__(self):
        return self.id


class UserGroups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)
    is_block = models.BooleanField(default=False)
    class Meta:
        db_table = "user_groups"
    def __str__(self):
        return self.id

class UserAuthLogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ip_address=models.GenericIPAddressField()
    login_time = models.DateTimeField()
    logout_time = models.DateTimeField(null=True)
    session_key = models.TextField(null=True)
    login_data = models.TextField(null=True)
    class Meta:
        db_table = "user_auth_logs"