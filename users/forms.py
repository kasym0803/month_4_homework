from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password_repeat = forms.CharField(max_length=50, widget=forms.PasswordInput)
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')
        if password_repeat != password:
            raise forms.ValidationError('password error')
        cleaned_data.pop('password_repeat')
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

