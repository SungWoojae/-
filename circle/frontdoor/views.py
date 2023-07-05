from django.shortcuts import render, redirect, get_object_or_404
from .models import Circle, Comment
from django.utils import timezone
# Create your views here.
def home(request):
    circles=Circle.objects.all()
    return render(request,'home.html',{'circles':circles})

def new(request):
    return render(request,"create.html")

def create(request):
    new_circle=Circle()
    new_circle.name=request.POST['name']
    new_circle.intro=request.POST['intro']
    new_circle.num=request.POST['num']
    new_circle.save()
    return redirect('detail',new_circle.id)

def detail(request,id):
    circle=get_object_or_404(Circle,pk=id)
    return render(request,'detail.html',{'circle':circle})

def comment(request,id):
    new_comment=Comment()
    new_comment.circle=Circle.objects.get(id=id)
    new_comment.comment=request.POST['new_comment']
    new_comment.time=timezone.now()
    new_comment.save()
    return redirect('detail',new_comment.circle.id)

def edit(request,id):
    if request.method=="POST":
        update_circle=Circle.objects.get(id=id)
        update_circle.name=request.POST['name']
        update_circle.intro=request.POST['intro']
        update_circle.num=request.POST['num']
        update_circle.save()
        return redirect('detail',update_circle.id)
    else:    
        edit_circle=Circle.objects.get(id=id)
        return render(request,'edit.html',{'circle':edit_circle})

    

def delete(request,id):
    delete_circle=Circle.objects.get(id=id)
    delete_circle.delete()
    return redirect('home')
