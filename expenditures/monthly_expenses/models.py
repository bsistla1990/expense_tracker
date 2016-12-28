from django.db import models
from django.utils import timezone
import uuid
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Family(models.Model):
    member_first_name = models.CharField(max_length=200, default='sistla', null=False)
    member_last_name = models.CharField(max_length=200, default= 'test',null=False)
    id = models.UUIDField(default=uuid.uuid4, primary_key = True)
    date_of_birth = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=10)
    """
    def __str__(self):
        return self.member_first_name +" "+self.member_last_name
    """
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
