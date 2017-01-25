from django import forms
from django.core.exceptions import ValidationError
#校验函数
def words_validators(comment):
    if len(comment) < 5:
        raise ValidationError('Not enough words!(at least 5)')

def comments_validators(comment):
    if 'a' in comment:
        raise ValidationError("No,you con't say it!")
#创建一个评论表单模型
class Commentform(forms.Form):
    comment = forms.CharField(label='评论内容',
        widget=forms.Textarea(),
        #系统自带的校验器
        error_messages={'required':'what?'},
        #自定义的校验器
        validators=[words_validators,comments_validators]
    )

#留言表单
class Messageform(forms.Form):
    content = forms.CharField(label='填写留言',
        widget=forms.Textarea(),
        #系统自带的校验器
        error_messages={'required':'what?'},
    )





#创建一个注册表单模型
class Registerform(forms.Form):
    username = forms.CharField(label='用户名',widget=forms.TextInput(attrs={'autofocus':'','placeholder':'请在此输入用户名'}),max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput(attrs={'placeholder':'请在此输入密码'}),max_length=50)
    photo = forms.ImageField(label='头像',required=False)
    gender = forms.ChoiceField(label='性别',choices=(('male','male'),('female','female')))

#创建一个修改个人信息
class Editform(forms.Form):
    username = forms.CharField(label='用户名',widget=forms.TextInput(attrs={'autofocus':'','placeholder':'请在此输入用户名'}),required=False)
    password = forms.CharField(label='密码',widget=forms.PasswordInput(attrs={'placeholder':'请在此输入密码'}),max_length=50,required=False)
    photo = forms.ImageField(label='头像',required=False)
    gender = forms.ChoiceField(label='性别',choices=(('male','male'),('female','female')),required=False)

#创建一个登陆用表单
class Loginform(forms.Form):
    username = forms.CharField(label='用户名',widget=forms.TextInput(attrs={'autofocus':'','placeholder':'请在此输入用户名'}))
    password = forms.CharField(label='密码',widget=forms.PasswordInput(attrs={'placeholder':'请在此输入密码'}))
