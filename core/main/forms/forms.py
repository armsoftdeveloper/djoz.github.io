
'''

    In This Python File You Find All Necessary Modules ,  Packages and Important Forms Function For Handling With AJAX

'''
# For work with forms
from django import forms
# Important mdoels
from ..models import Newsletter, Contact
# Validator for forms
from django.core.validators import RegexValidator


from django.forms import widgets
from django.utils.safestring import mark_safe


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"

# Form for handling user messages in the contact page
class MessageForm(forms.ModelForm):
    # Custom field for the name with length and character validators
    name = forms.CharField(
        label='Name',
        min_length=3,
        max_length=100,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message="Only letters are allowed!")],
        widget=forms.TextInput(attrs={'placeholder': 'Name'}),
        required=True
    )

    # Custom field for the email with length and email validators
    email = forms.EmailField(
        label='Email',
        min_length=8,
        max_length=100,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message="Please provide a valid email address!")],
        widget=forms.TextInput(attrs={'placeholder': 'Email'}),
        required=True
    )

    # Custom field for the phone number with length and number validators
    phone = forms.CharField(
        label='Phone',
        min_length=2,
        max_length=30,
        validators=[RegexValidator(r'^[0-9]*$', message="Only numbers are allowed!")],
        widget=forms.TextInput(attrs={'placeholder': 'Phone'}),
        required=True
    )

    # Custom field for the message with length and text area widget
    message = forms.CharField(
        label='Message',
        min_length=10,
        max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': 'Message', 'cols': 99}),
        required=True
    )

    class Meta:
        model = Contact
        fields = "__all__"

