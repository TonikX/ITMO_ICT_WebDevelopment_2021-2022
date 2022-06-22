from django import forms
from .models import Bill, Hotel, Comment, Client, Room



class create_client1(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'first_name',
            'last_name',
            'Birthday',
            'Sex',
            'Phone',
            'Nationality',
        ]

class create_bill1(forms.ModelForm):
    class Meta:
        model = Bill
        fields = [
            "Date",
            "Check_in",
            "Check_out",
            "id_client",
            "id_room",
        ]

class create_commnent1(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "Name_hotel",
            "Content",
            "Check_in",
            "Check_out",
            "Rate",
            "id_client",
        ]