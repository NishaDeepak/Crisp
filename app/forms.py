from django import forms
val=[['Django','Django'],['Python','PYTHON']]

def check_for_h(value):
    if value[0].lower()!='h':
        raise forms.ValidationError('Name should startwith h')

class Crispyform(forms.Form):
    name=forms.CharField(max_length=200,required=True,validators=[check_for_h])
    email=forms.EmailField(required=True)
    course=forms.ChoiceField(choices=val)
