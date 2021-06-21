from django import forms
from .models import Upload

class FileUploadForm(forms.Form):
    file_source = forms.FileField()

class ContactForm(forms.Form):
    Station = forms.CharField(max_length=50)
    Model = forms.CharField(max_length=50)
    Username = forms.CharField(max_length=50)
    Password = forms.CharField(max_length=50)
    # message = forms.CharField(widget=forms.Textarea)
    # sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)

class UploadForm(forms.ModelForm):
    image = forms.FileField(label='')
    class Meta:
        model = Upload
        fields = ('image',)

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'file-upload-field','label':''})
