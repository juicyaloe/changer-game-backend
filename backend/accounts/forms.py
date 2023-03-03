from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('userid', 'name', 'address', 'phone', 'phone_check', 'email', 'email_check', 'date_of_birth', 'level', 'recommendation', 'account')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label=("Password"),
        help_text=("우측 변경 버튼을 눌러 비밀번호를 변경할 수 있습니다. <a href=\"../password/\">변경</a>"))

    class Meta:
        model = User
        fields = ('userid', 'password', 'name', 'address',
                  'phone', 'phone_check', 'email', 'email_check',
                  'date_of_birth', 'level', 'recommendation', 'account', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]