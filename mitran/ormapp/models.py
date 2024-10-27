from django.db import models
from django.contrib import admin
class Bank(models.Model):
	Name=models.CharField(max_length=20)
	AccNo=models.IntegerField(primary_key="AccNo")
	IFSC_Coad=models.CharField(max_length=20)
	Loan_Amount=models.IntegerField()
	Time_Period=models.FloatField()
	Rate_of_Interest=models.FloatField()
	PhoneNo=models.IntegerField()

class BankAdmin(admin.ModelAdmin):
	list_display=('Name','AccNo','IFSC_Coad','Loan_Amount','Time_Period','Rate_of_Interest','PhoneNo')
