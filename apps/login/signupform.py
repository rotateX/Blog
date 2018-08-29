from django import forms

class signupform(forms.Form):
    username = forms.CharField(min_length=5, max_length=16, widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'text',
        'value': 'User Name',
        'onfocus': "this.value = '';",
        'onblur': "if (this.value == '') {this.value = 'User Name';}",
        'id':"active"
    }))
    email = forms.EmailField(min_length=5, max_length=254, widget=forms.EmailInput(attrs={
        'type': 'text',
        'class': 'text',
        'value': '你的邮箱',
        'onfocus': "this.value = '';",
        'onblur': "if (this.value == '') {this.value = 'your@email.com';}",
    }))
    password = forms.CharField(min_length=5,max_length=32,widget=forms.PasswordInput(attrs={
        'type': 'text',
        'class': 'text',
        'value': '输入密码',
        'onfocus': "this.value = '';",
        'onblur': "if (this.value == '') {this.value = 'Password';}",
    }))
    password2 = forms.CharField(min_length=5,max_length=32,widget=forms.PasswordInput(attrs={
        'type': 'text',
        'class': 'text',
        'value': '确认密码',
        'onfocus': "this.value = '';",
        'onblur': "if (this.value == '') {this.value = 'Password';}",
    }))
