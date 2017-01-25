from django.shortcuts import render,redirect,HttpResponse
from Sengokuapp.models import People,Domain,Domain,Road,Comment,UserProfile,Message
from django.template import Context
from Sengokuapp.forms import Commentform,Registerform,Loginform,Editform,Messageform
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.







#@login_required
def index(request):
    Context={}
    query = request.GET.get('gender')
    if query:
        Thelist = Domain.objects.filter(gender=query)
    else:
        Thelist = Domain.objects.all()
    #分页功能
    page_machine = Paginator(Thelist,9)
    Thepage = request.GET.get('page')
    try:
        Thelist = page_machine.page(Thepage)
    except EmptyPage:
        Thelist = page_machine.page(page_machine.num_pages)
    except PageNotAnInteger:
        Thelist = page_machine.page(1)
    #导航栏
    Roadlist = Road.objects.all()
    Context['Roadlist'] = Roadlist
    Context['Thelist'] = Thelist
    Domainjj = Domain.objects.filter(gender='jj')
    Context['Domainjj'] = Domainjj
    Domaindhd = Domain.objects.filter(gender='dhd')
    Context['Domaindhd'] = Domaindhd
    Domaindsd = Domain.objects.filter(gender='dsd')
    Context['Domaindsd'] = Domaindsd
    Domainxhd = Domain.objects.filter(gender='xhd')
    Context['Domainxhd'] = Domainxhd
    Domainnhd = Domain.objects.filter(gender='nhd')
    Context['Domainnhd'] = Domainnhd
    Domainbld = Domain.objects.filter(gender='bld')
    Context['Domainbld'] = Domainbld
    Domainsyd = Domain.objects.filter(gender='syd')
    Context['Domainsyd'] = Domainsyd
    Domainsyad = Domain.objects.filter(gender='syad')
    Context['Domainsyad'] = Domainsyad
    return render(request,'index.html',Context)

def domain(request,domainid):
    Context={}
    query=request.GET.get('gender')
    if query:
        Thelist = Domain.objects.filter(gender=query)
    else:
        Thelist = Domain.objects.all()
    #导航栏
    Roadlist = Road.objects.all()
    Context['Roadlist'] = Roadlist
    Context['Thelist'] = Thelist
    Domainjj = Domain.objects.filter(gender='jj')
    Context['Domainjj'] = Domainjj
    Domaindhd = Domain.objects.filter(gender='dhd')
    Context['Domaindhd'] = Domaindhd
    Domaindsd = Domain.objects.filter(gender='dsd')
    Context['Domaindsd'] = Domaindsd
    Domainxhd = Domain.objects.filter(gender='xhd')
    Context['Domainxhd'] = Domainxhd
    Domainnhd = Domain.objects.filter(gender='nhd')
    Context['Domainnhd'] = Domainnhd
    Domainbld = Domain.objects.filter(gender='bld')
    Context['Domainbld'] = Domainbld
    Domainsyd = Domain.objects.filter(gender='syd')
    Context['Domainsyd'] = Domainsyd
    Domainsyad = Domain.objects.filter(gender='syad')
    Context['Domainsyad'] = Domainsyad
    #获取对应id的文章
    thedomain = Domain.objects.get(id=domainid)
    Context['thedomain'] = thedomain
    #评论表单
    if request.method == 'GET':
        form = Commentform
    if request.method == 'POST':
        form = Commentform(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            c = Comment(comment=comment,belong_to=thedomain,belong_for=request.user)
            c.save()
            return redirect(to='domain',domainid=domainid)
    Context['form'] = form
    comment_list = Comment.objects.filter(belong_to=thedomain)
    #添加一个最优评论
    best_comment = Comment.objects.filter(best_comment=True,belong_to=thedomain)
    if best_comment:
        Context['best_comment'] = best_comment[0]
    Context['comment_list'] = comment_list
    return render(request,'Domain.html',Context)

def message_f(request):
    Context={}
    form = Messageform
    message_list = Message.objects.all()
    if request.method == 'POST':
        form = Messageform(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            c = Message(content=content,belong_to = request.user)
            c.save()
            return redirect(to='message_f')
    Context['form'] = form
    Context['message_list'] = message_list
    return render(request,'message.html',Context)


#注册函数
def register(request):
    Context={}
    if request.method=='GET':
        form = Registerform
    if request.method=='POST':
        print(request.POST)
        form = Registerform(request.POST,request.FILES)
        #创建一个用户实例
        user = User()
        user.username = request.POST['username']
        user.set_password(request.POST['password'])
        user.save()
        userprofile = UserProfile(belong_to = user)
        user.profile.gender = request.POST['gender']
        if form.is_valid():
            user_avatar = form.cleaned_data.get('photo')
            if user_avatar:
                userprofile.profile_image = user_avatar
        userprofile.save()
        return HttpResponse('<h4>注册成功!</h4>')
    Context['form'] = form
    return render(request,'register.html',Context)

#修改个人信息
def user_info(request):
    Context={}
    user = request.user
    if request.method=='GET':
        form = Editform(initial={
            "username":user.username,
            "gender":user.profile.gender,
            "photo":user.profile.profile_image,
        })
    if request.method=='POST':
        print(request.POST)
        form = Editform(request.POST,request.FILES)
        user_name = request.POST['username']
        user_password = request.POST['password']
        if user_name:
            user.username = user_name
        if user_password:
            user.set_password(user_password)
        user.save()
        try:
            userprofile = UserProfile.objects.get(belong_to = user)
        except objectDoseNotExist:
            userprofile = UserProfile(belong_to = user)
        userprofile.gender = request.POST['gender']
        if form.is_valid():
            user_avatar = form.cleaned_data.get('photo')
            if user_avatar:
                userprofile.profile_image = user_avatar
        userprofile.save()
        return HttpResponse('<h4>修改成功!</h4>')
    Context['form'] = form
    return render(request,'user_info.html',Context)

#登陆函数
def login_f(request):
    Context = {}
    if request.method=='GET':
        form = Loginform

    if request.method=='POST':
        form = Loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request, user)
                return redirect(to='index')
            else:
                return HttpResponse('<h4>用户不存在</h4>')
    Context['form'] = form
    return render(request,'login.html',Context)
