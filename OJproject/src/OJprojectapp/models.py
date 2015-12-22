#coding=utf-8
from django.db import models
from django.contrib import admin
# Create your models here.


class problemslist(models.Model):
    OJ = models.CharField(max_length=20)
    SID = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    ratio = models.CharField(max_length=50)
    time_limit = models.CharField(max_length=15)
    mem_limit = models.CharField(max_length=15)
    description = models.TextField()
    inputs = models.TextField()
    output = models.TextField()
    sample_input = models.TextField()
    sample_output = models.TextField()
    hint = models.TextField()
    pic = models.CharField(max_length=300)

class group_status(models.Model):
    groupID = models.CharField(max_length=30)
    groupname = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    competedate = models.DateTimeField()
    codes = models.TextField()
    is_codes_private = models.BooleanField()
    is_group_private = models.BooleanField()
    submit_time = models.DateTimeField() 

class user_status(models.Model):
    problemID = models.CharField(max_length=15)
    problemTitle = models.CharField(max_length=35)
    problemSID = models.CharField(max_length=15)
    contestID = models.CharField(max_length=10)
    userID = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    OJ = models.CharField(max_length=10)
    result = models.CharField(max_length=30)
    memory = models.CharField(max_length=15)
    time = models.CharField(max_length=15)
    language = models.CharField(max_length=10)
    code = models.TextField()
    submit_time = models.DateTimeField()
    is_code_private = models.BooleanField()
    is_user_private = models.BooleanField()

class user(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    signature = models.TextField(max_length=200)
    school = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    register_time= models.DateTimeField()
    answered = models.CharField(max_length=50)
    wrong = models.CharField(max_length=50)
    right = models.CharField(max_length=50) 
    contest_number = models.CharField(max_length=50)
    contest_wrong = models.CharField(max_length=50)
    contest_right = models.CharField(max_length=50)
    problems = models.ManyToManyField(user_status)
    contests = models.ManyToManyField(group_status)

class contest(models.Model):
    title = models.CharField(max_length = 50) #比赛标题
    description = models.TextField() #比赛介绍
    announcement = models.TextField() #比赛申明
    password = models.CharField(max_length = 50) #比赛密码，如果为空，则加入空串
    owner = models.CharField(max_length = 50) #创建者ID
    #pcnt = 0 #题目数量统计
    ptitles = [models.CharField(max_length = 50)] * 26 #修改的标题，注意和原来的题目可能不一样
    pids = [models.CharField(max_length = 15)] * 26 #题目编号
    sojs = [models.CharField(max_length = 20)] * 26 #来源OJ
    begintime = models.DateTimeField() #开始时间
    endtime = models.DateTimeField() #结束时间

class contest_ext(models.Model):
    count = models.IntegerField()

class contest_tmp(models.Model):
    title = models.CharField(max_length = 50) #比赛标题
    description = models.TextField() #比赛介绍
    announcement = models.TextField() #比赛申明
    password = models.CharField(max_length = 50) #比赛密码，如果为空，则加入空串
    owner = models.CharField(max_length = 50) #创建者ID
    count = models.IntegerField()
    ptitles = [models.CharField(max_length = 50)] * 26 #修改的标题，注意和原来的题目可能不一样
    pids = [models.CharField(max_length = 15)] * 26 #题目编号
    sojs = [models.CharField(max_length = 20)] * 26 #来源OJ
    begintime = models.DateTimeField() #开始时间
    endtime = models.DateTimeField() #结束时间

class group(models.Model):
    groupname = models.CharField(max_length=50)
    groupmembers = models.ManyToManyField(user)
    register_time= models.DateTimeField()


class discussion(models.Model):
    userID = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    problemID = models.CharField(max_length=15)
    problemTitle = models.CharField(max_length=35)
    speak = models.TextField(max_length=300)
    like = models.TextField(max_length=50)
    dislike = models.TextField(max_length=50)
    submit_time = models.DateTimeField()


class useradmin(admin.ModelAdmin):
    list_display = ('username','register_time')
class groupadmin(admin.ModelAdmin):
    list_display = ('groupname','register_time')
class user_statusadmin(admin.ModelAdmin):
    list_display = ('username','submit_time')
class group_statusadmin(admin.ModelAdmin):
    list_display = ('groupname','submit_time')
class problemslistadmin(admin.ModelAdmin):
    list_display = ('OJ','title')
class discussionadmin(admin.ModelAdmin):
    list_display = ('problemTitle','submit_time')


admin.site.register(user,useradmin)
admin.site.register(group,groupadmin)
admin.site.register(user_status,user_statusadmin)
admin.site.register(group_status,group_statusadmin)
admin.site.register(problemslist,problemslistadmin)
admin.site.register(discussion,discussionadmin)