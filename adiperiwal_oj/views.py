from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import User,Problem,TestCases,Submissions
from django.utils import timezone
import subprocess
import filecmp

def options(request):
    return render(request, 'adiperiwal_oj/options.html')

def signin(request):
    return render(request, 'adiperiwal_oj/signin.html')

def login(request):
    return render(request, 'adiperiwal_oj/login.html')

def signincheck(request):
    z=request.POST
    latest_user_list=User.objects.filter(username=z['op'])
    if latest_user_list.exists():
        return render(request, 'adiperiwal_oj/options.html')
    else:
        s=User(username=z['op'],password=z['pswd'])
        s.problem=Problem.objects.all()
        s.save()
        g=User.objects.get(username=z['op'])
        h=g
        return render(request,'adiperiwal_oj/successful.html',{'h':h})

def logincheck(request):
    z=request.POST
    latest_user_list=User.objects.filter(username=z['op'])
    if latest_user_list.exists():
        g=User.objects.get(username=z['op'])
        h=g
        if h.password==z['pswd']:
            return render(request,'adiperiwal_oj/successful.html',{'h':h})
        else:
            return render(request, 'adiperiwal_oj/options.html')
    else:
        return render(request, 'adiperiwal_oj/options.html')

def index(request,user_id):
    user=get_object_or_404(User, pk=user_id)
    latest_problem_list = Problem.objects.order_by('difficulty')
    return render(request, 'adiperiwal_oj/index.html', {'user':user,'latest_problem_list': latest_problem_list})

def allsubmissionslist(request,user_id):
    user=get_object_or_404(User, pk=user_id)
    k=[]
    x=0
    for s in user.submissions_set.all():
        x=x+1
        if x&1:
            k.append(s)
    k.reverse()
    return render(request, 'adiperiwal_oj/allsubmissionslist.html', {'k':k,'user':user})

def detail(request, problem_id,user_id):
    user=get_object_or_404(User, pk=user_id)
    problem = get_object_or_404(Problem, pk=problem_id)
    return render(request, 'adiperiwal_oj/detail.html', {'user':user,'problem': problem})

def code(request, problem_id,user_id):
    user=get_object_or_404(User, pk=user_id)
    problem = get_object_or_404(Problem, pk=problem_id)
    return render(request, 'adiperiwal_oj/code.html', {'user':user,'problem': problem})

def history(request, problem_id,user_id):
    user=get_object_or_404(User, pk=user_id)
    problem = get_object_or_404(Problem, pk=problem_id)
    a=request.POST
    text_file = open("E:/Adi_oj/adiperiwal_oj/data.cpp", "w")
    n = text_file.write(a['mycode'])
    text_file.close()
    x=0
    if problem.name=="Dice Combinations":
        x=1
    elif problem.name=="Grid Paths":
        x=3
    else:
        x=2
    c=problem.testcases_set.get(id=x)
    b=open("E:/Adi_oj/adiperiwal_oj/input.txt", "w")
    m=b.write(c.input_text)
    b.close()
    b=open("E:/Adi_oj/adiperiwal_oj/expectedoutput.txt", "w")
    m=b.write(c.output_text)
    b.close()
    subprocess.call([r'E:/Adi_oj/adiperiwal_oj/abc.bat'])
    b=open("E:/Adi_oj/adiperiwal_oj/output.txt", "r")
    m=b.read()
    b.close()
    e="E:/Adi_oj/adiperiwal_oj/expectedoutput.txt"
    d="E:/Adi_oj/adiperiwal_oj/output.txt"
    if filecmp.cmp(d, e, shallow = False)==True:
        problem.submissions_set.create(qwerty=user,coder=a['mycode'],useroutput=m,sub_date=timezone.now(),verdict=True)
        user.submissions_set.create(answer=problem,coder=a['mycode'],useroutput=m,sub_date=timezone.now(),verdict=True)
        problem.solved_status=True
    else:
        problem.submissions_set.create(qwerty=user,coder=a['mycode'],useroutput=m,sub_date=timezone.now(),verdict=False)
        user.submissions_set.create(answer=problem,coder=a['mycode'],useroutput=m,sub_date=timezone.now(),verdict=False)
        problem.solved_status=False
    b=open("E:/Adi_oj/adiperiwal_oj/output.txt", "w")
    m=b.write("")
    b.close()
    x=0
    k=[]
    for s in user.submissions_set.all():
        x=x+1
        if x&1:
            k.append(s)
    k.reverse()
    return render(request, 'adiperiwal_oj/history.html', {'k':k,'user':user,'problem': problem})

def particular(request,problem_id,submission_id,user_id):
    user=get_object_or_404(User, pk=user_id)
    problem = get_object_or_404(Problem, pk=problem_id)
    submission= user.submissions_set.get(id=submission_id)
    return render(request, 'adiperiwal_oj/particular.html', {'submission':submission})