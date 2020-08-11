from django import forms


class BlogNewsForm(forms.Form):

    title = forms.CharField()
    description = forms.CharField(widget=forms.HiddenInput())
