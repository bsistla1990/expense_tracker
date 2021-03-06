from django.db import models
from django.utils import timezone
import uuid
from django.contrib.postgres.fields import ArrayField
import string, random


from django.contrib.auth.models import User


# Create your models here.

class Root(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=20, null=False, unique=True)

class Family(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key = True)
    date_of_birth = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=10)
    root = models.ForeignKey(Root, on_delete=models.CASCADE, null=True)
    member = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    """
    def __str__(self):
        return self.member_first_name +" "+self.member_last_name
    """

class Member(User):
    is_head =  models.BooleanField(default=False)
    root = models.ForeignKey(Root, on_delete=models.CASCADE, null=True)

    class Meta:
        proxy=True


class Income(models.Model):
    earned_by= models.ForeignKey(Family, on_delete=models.CASCADE)
    id = models.UUIDField(default = uuid.uuid4, primary_key = True)
    source = models.CharField(max_length=255)
    date_of_income = models.DateField(default=timezone.now)

class Expense_category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    category = models.CharField(max_length=255)
    expense_type = ArrayField(models.CharField(max_length=200), blank=True)

class Payment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    mode = models.CharField(max_length=255)

class Cards(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key = True)
    type = models.CharField(max_length=10)
    card_holder = models.ForeignKey(Family, on_delete=models.CASCADE)
    bank = models.CharField(max_length=30)

class Expenditure(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key = True)
    spent_by = models.ForeignKey(Family, on_delete=models.CASCADE)
    category = models.ForeignKey(Expense_category , related_name="%(class)s_category", on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    date_of_expenditure =  models.DateField(default=timezone.now)
    comments = models.CharField(max_length=255)
    payment_type=models.ForeignKey(Payment, on_delete=models.CASCADE)
    type= models.ForeignKey(Expense_category, related_name="%(class)s_type", on_delete=models.CASCADE)

class User(models.Model):
    id= models.AutoField(primary_key=True)
