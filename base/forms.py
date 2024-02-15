from django import forms

from base.models import filter_table


class filter_form(forms.ModelForm):
    class Meta:
        model = filter_table
        fields = '__all__'
