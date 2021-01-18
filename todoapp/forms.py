from django import forms
from django.contrib.auth.forms import UsernameField

class LoginForm(forms.Form):
    username = UsernameField(
        label='ユーザー名',
        max_length=255,
    )
    password = forms.CharField(
        label='パスワード',
        strip=False,
        widget=forms.PasswordInput(render_value=True),
    )

    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
    #     try:
    #         user = User.objects.get(username=username)
    #     except ObjectDoesNotExist:
    #         raise forms.ValidationError("正しいユーザー名を入力してください")
    #     if not user.check_password(password):
    #         raise forms.ValidationError("正しいパスワードを入力してください")