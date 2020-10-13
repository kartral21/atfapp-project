from .models import User
from django import forms
import datetime


class UserSerializer(forms.ModelForm):

    ROLE_CHOICE = (('admin', 'Admin'),
                   ('developer', 'Developer'))
    DOMAIN_CHOICE = (('webride', 'Webride'),
                     ('sisense', 'Sisense'),
                     ('cloudshell', 'CloudShell'))
    role = forms.ChoiceField(choices=ROLE_CHOICE, show_hidden_initial=True)
    domain = forms.ChoiceField(choices=DOMAIN_CHOICE, show_hidden_initial=True)

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = User
        fields = ("__all__")
