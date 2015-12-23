#coding=utf-8
'''
Created on 2015年12月22日

@author: Rhapsody
'''
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import date, datetime
#from django import forms
from OJprojectapp.UserManager import UserInit
from OJprojectapp.models import *
from OJprojectapp.DataManager import DataManager
#from django.templatetags.i18n import language

def createcontest(username):
    tmp = contest.objects.get(owner = username, IsReady = False)
    tmp.IsReady = True
    tmp.save()

class LoadForm():
    def __init__(self):
        self.title = ""
        self.description = ""
        self.announcement = ""
        self.password = ""
        self.owner = ""
        self.list = []
        self.begintime = datetime.now()
        self.endtime = datetime.now()

class ProblemForm():
    def __init__(self, titles, pids, sojs):
        self.titles = titles
        self.pids = pids
        self.sojs = sojs
        
class ProblemShow():
    def __init__(self, titles, pids, sojs):
        self.titles = titles
        self.pids = pids
        self.sojs = sojs
        self.merge = sojs + '$' + pids

def loaddata(username):
    tmp = contest.objects.filter(owner = username, IsReady = False)
    if len(tmp) == 0:
        tmp = contest(owner = username, 
                      begintime = datetime.now(), 
                      endtime = datetime.now(), 
                      IsReady = False, 
                      )
        tmp.save()
    tmp = contest.objects.get(owner = username, IsReady = False)
    #print tmp.owner
    Ans = LoadForm()
    Ans.title = tmp.title
    Ans.description = tmp.description
    Ans.announcement = tmp.announcement
    Ans.password = tmp.password
    Ans.owner = tmp.owner
    for problem in tmp.list.all():
        Ans.list.append(ProblemForm(problem.titles, problem.pids, problem.sojs))
    Ans.begintime = tmp.begintime
    Ans.endtime = tmp.endtime
    return Ans
    
def savedata(username, Data):
    print 'Save data'
    tmp = contest.objects.filter(owner = username, IsReady = False)
    if len(tmp) == 0:
        tmp = contest(owner = username, 
                      begintime = datetime.now(), 
                      endtime = datetime.now(), 
                      IsReady = False, 
                      )
        tmp.save()
    tmp = contest.objects.get(owner = username, IsReady = False)
    #print tmp.owner
    tmp.title = Data.title
    tmp.description = Data.description
    tmp.announcement = Data.announcement
    tmp.password = Data.password
    tmp.owner = Data.owner
    for problem in Data.list:
        print 'Add :', problem.sojs, problem.pids, problem.titles
        p = contest_problem(titles = problem.titles, 
                            pids = problem.pids, 
                            sojs = problem.sojs, )
        if len(contest_problem.objects.filter(titles = problem.titles, 
                                              pids = problem.pids, 
                                              sojs = problem.sojs, )) == 0:
            p.save()
        #tmp.list = None
        if not find(tmp.list.all(), p):
            p.save()
            tmp.list.add(p)
    tmp.begintime = Data.begintime
    tmp.endtime = Data.endtime
    tmp.save()

def check(add):
    #print 'Check', add.sojs, add.pids
    tmp = problemslist.objects.filter(OJ = add.sojs, SID = add.pids)
    #print 'size =', len(tmp)
    return len(tmp) == 0

def find(list, aim):
    print 'Begin find :'
    for i in list:
        print 'Have =', i.sojs, i.pids
        if i.sojs == aim.sojs and i.pids == aim.pids:
            return True
    return False