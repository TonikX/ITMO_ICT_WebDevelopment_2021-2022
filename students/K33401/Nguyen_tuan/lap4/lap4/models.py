from django.db import models



class historybill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    check_in = models.DateField()
    check_out = models.DateField()
    hotel_name = models.CharField(max_length=500)
    adress_hotel = models.CharField(max_length=500)
    money = models.IntegerField()