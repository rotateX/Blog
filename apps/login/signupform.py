from django import forms

class signupform(forms.Form):
    username = forms.CharField(
        min_length=5,
        max_length=16,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'text',
                'placeholder': 'User Name',
                'id':"active"
            }
        ),
       error_messages={
           'required': '你个无名人士',
           'min_length': '太短了',
           'max_length': '太长了',
                        }
    )
    email = forms.EmailField(
        min_length=5,
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                'type': 'text',
                'class': 'text',
                'placeholder': '你的邮箱',
            }
        ),
        error_messages={
            'required': '请输入有效邮箱'
        }
    )
    password = forms.CharField(
        min_length=5,
        max_length=32,
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'class': 'text',
                'placeholder': '输入密码',
            }
        )
    )
    confirm_p = forms.CharField(
        min_length=5,
        max_length=32,
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'class': 'text',
                'placeholder': '确认密码',
                # 'onfocus': "this.value = '';",
                # 'onblur': "if (this.value == '') {this.value = 'Password';}",
            }
        )
    )

class loginform(forms.Form):
    username = forms.CharField(
        min_length=5,
        max_length=16,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-username form-control',
                'id':"form-username",
                'placeholder': "Username...",
                'name':'form-username',
            }
        ),
        error_messages={
            'required': '用户名不能为空'
        }
    )
    password = forms.CharField(
        min_length=5,
        max_length=32,
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'name': 'form-password',
                'placeholder': 'Password...',
                'class': 'form-password form-control',
                'id': 'form-password',
            }
        )
    )