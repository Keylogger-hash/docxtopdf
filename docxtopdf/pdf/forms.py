from django import forms


class UploadPdfForm(forms.Form):
    filename = forms.FileField(widget=forms.FileInput(attrs={'accept':'.doc,.docx,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document'}))
