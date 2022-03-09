from django import forms


class UploadPdfForm(forms.Form):
    filename = forms.FileField()
