from django import forms

class DateInput(forms.DateInput):
    input_type='date'
# create the form inputs
class AnnouncementForm(forms.Form):
    title = forms.CharField(label="title", max_length=55, widget=forms.TextInput())
    name = forms.CharField(label="name", max_length=55, widget=forms.TextInput())
    email = forms.CharField(label="email", max_length=255, widget=forms.TextInput(attrs={'type': 'email'}))
    expiration_date = forms.DateTimeField(label="date",widget=DateInput())
    custom_text = forms.CharField(label="description", max_length=255, widget=forms.Textarea())
    category = forms.ChoiceField(label="type", choices=[('Selling', 'Selling'),('Buying', 'Buying')])
