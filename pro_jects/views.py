from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from .models import Project,Profile
from .forms import NewProfileForm,NewProjectForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer
from rest_framework import status
# Create your views here.

def home(request):
  projects=Project.objects.all()
  profiles=Profile.objects.all()
  return render(request,'home.html',{"projects":projects,"profiles":profiles})

def profile(request):
  current_user = request.user
  profile=Profile.objects.filter(user_id=current_user.id)
  projects = Project.objects.filter(user_id=current_user.id)

  return render(request,'profile.html',{"profile":profile,"projects":projects})

@login_required(login_url='/accounts/login')
def new_profile(request):
  current_user=request.user
  if request.method == 'POST':
    form=NewProfileForm(request.POST,request.FILES)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = current_user
      prof_pic=form.cleaned_data['prof_pic']
      bio=form.cleaned_data['bio']
      contact = form.cleaned_data['contact']
      Profile.objects.filter(user=current_user).update(bio=bio,prof_pic=prof_pic,contact=contact)
      profile.save()

    return redirect('profile') 
  else:
    form = NewProfileForm()
    return render(request,'new-profile.html',{"form":form})

@login_required(login_url='/accounts/login')
def project_add(request):
  current_user = request.user
  if request.method == 'POST':
    form = NewProjectForm(request.POST,request.FILES)
    if form.is_valid():
      project = form.save(commit=False)
      project.user = current_user
      project.save()
    return redirect('home')

  else:
    form=NewProjectForm()
    return render(request,'project-add.html',{'form':form})

class Pro_file(APIView):
  def get(self,request,format=None):
    all_profiles=Profile.objects.all()
    serializers=ProfileSerializer(all_profiles,many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers = ProfileSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class Pro_ject(APIView):
  def get(self,request,format=None):
    projects=Project.objects.all()
    serializers=ProjectSerializer(projects,many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers = ProjectSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)