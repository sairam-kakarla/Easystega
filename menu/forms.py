from django import forms
class Encode(forms.Form):
    image=forms.ImageField(label="Select Image")
    data =forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter your information here'}),label="")

