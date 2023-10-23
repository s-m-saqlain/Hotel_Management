from django import forms
from .models import Customer

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Customer
        fields = ['first_name','last_name','image', 'email',"password","phone", 'address']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        
        if email and password:
            # Add your custom validation logic here
            user = Customer.objects.filter(email=email).first()
            if user is None:
                raise forms.ValidationError("Invalid email ")
            
            if password != user.password:
                raise forms.ValidationError("Invalid password")

            return cleaned_data
            
            
    


# class AuthenticationForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
