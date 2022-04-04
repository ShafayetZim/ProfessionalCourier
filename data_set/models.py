from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Division(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class District(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Sub(models.Model):
    name = models.CharField(max_length=30)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def order_no_generate():
    # GET Current Date
    today = datetime.date.today()

    # Format the date like (20-11-28 YY-MM-DD)
    today_string = today.strftime('%y%m%d')
    prefix = "" + today_string

    # For the very first time invoice_number is DD-MM-YY-0001
    next_order_no = '0001'

    # Get Last Employee Start With TPC-MI-
    last_order_no = Parcel.objects.filter(order_no__startswith=prefix).order_by('order_no').last()

    if last_order_no:
        # Cut 4 digit from the Right and converted to int (STC-YY-MM-:xxxx)
        last_order_four_digit = int(last_order_no.order_no[-4:])

        # Increment one with last five digit
        next_order_no = '{0:04d}'.format(last_order_four_digit + 1)

    # Return custom invoice number
    return prefix + next_order_no


class Parcel(models.Model):
    STATUS_CHOICES = (
        ('1', 'Picked'),
        ('2', 'In Transit'),
        ('3', 'Shipped'),
        ('4', 'Out For Delivery'),
        ('5', 'Delivered'),
    )
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, null=True, blank=True)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True, related_name='div1')
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, related_name='dis1')
    sub = models.ForeignKey(Sub, on_delete=models.SET_NULL, null=True, related_name='sub1')
    s_village = models.CharField(max_length=100)
    s_phone = models.CharField(max_length=100)
    nid = models.CharField(max_length=100, null=True, blank=True)
    reference = models.CharField(max_length=100, null=True, blank=True)
    receiver = models.CharField(max_length=100)
    r_company = models.CharField(max_length=100, null=True, blank=True)
    div = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True, related_name='div2')
    dis = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, related_name='dis2')
    tha = models.ForeignKey(Sub, on_delete=models.SET_NULL, null=True, related_name='sub2')
    r_village = models.CharField(max_length=100)
    r_phone = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    date = models.DateField(default=timezone.now)
    order_no = models.CharField(max_length=200, primary_key=True, default=order_no_generate)
    barcode = models.ImageField(upload_to='barcode', blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2,)
    quantity = models.IntegerField(null=True, blank=True, default=1)
    total = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    tracking = models.CharField(max_length=20, choices=STATUS_CHOICES, default=1)
    status = models.CharField(max_length=20, default="Open")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.order_no

    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f'00{self.order_no}', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save('barcode.png', File(buffer), save=False)
        return super().save(*args, **kwargs)
