from django import forms
from .models import Parcel, District, Sub, Type


class TypeCreateForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = (
            'name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),

        }


class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = ('name', 'company', 'division', 'district', 'sub', 's_village', 's_phone', 'nid',
                  'reference', 'receiver', 'r_company', 'div', 'dis', 'tha', 'r_village', 'r_phone',
                  'type', 'description', 'price', 'quantity', 'total', 'cod_amount', 'payable', 'order_no',)

        widgets = {
            'name': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'division': forms.Select(attrs={'required': True, 'class': 'form-control', }),
            'district': forms.Select(attrs={'required': True, 'class': 'form-control',}),
            'sub': forms.Select(attrs={'required': True, 'class': 'form-control', }),
            's_village': forms.TextInput(attrs={'required': True,'class': 'form-control'}),
            's_phone': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'nid': forms.TextInput(attrs={'class': 'form-control'}),
            'reference': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'r_company': forms.TextInput(attrs={'class': 'form-control'}),
            'div': forms.Select(attrs={'required': True, 'class': 'form-control select2', }),
            'dis': forms.Select(attrs={'required': True, 'class': 'form-control', }),
            'tha': forms.Select(attrs={'required': True, 'class': 'form-control', }),
            'r_village': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'r_phone': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control', }),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_price', 'oninput': 'myFunction()'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_quantity', 'oninput': 'myFunction()'}),
            'total': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_total', }),
            'cod_amount': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_cod', 'oninput': 'myFunction()'}),
            'payable': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_pay',}),
            'order_no': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),

        }

        labels = {
            'name': 'Sender Name',
            'company': 'Sender Company',
            'division': 'Sender Division',
            'district': 'Sender District',
            'sub': 'Sender Thana',
            's_village': 'Sender Village',
            's_phone': 'Sender Phone',
            'nid': 'Sender Nid',
            'receiver': 'Receiver Name',
            'r_company': 'Receiver Company',
            'div': 'Receiver Division',
            'dis': 'Receiver District',
            'tha': 'Receiver Thana',
            'r_village': 'Receiver Village',
            'r_phone': 'Receiver Phone',
            'price': 'Price',
            'order_no': 'Order No',
        }


class TrackingForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = (
            'order_no', 'tracking')
        widgets = {
            'order_no': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tracking': forms.Select(attrs={'class': 'form-control'}),

        }



