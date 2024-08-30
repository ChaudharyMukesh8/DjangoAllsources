from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    msg = forms.CharField(widget=forms.Textarea)


class FeedbackForm(forms.Form):
    yourname = forms.CharField(max_length=50)
    your_email = forms.EmailField()
    your_msg = forms.CharField(widget=forms.Textarea)