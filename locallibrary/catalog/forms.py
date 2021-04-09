from django import forms

class ContactForm(forms.Form):
    Station = forms.CharField(max_length=50)
    Model = forms.CharField(max_length=50)
    Username = forms.CharField(max_length=50)
    Password = forms.CharField(max_length=50)
    # message = forms.CharField(widget=forms.Textarea)
    # sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)