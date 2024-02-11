from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from chunked_upload.views import ChunkedUploadCompleteView, ChunkedUploadView
from rest_framework.permissions import AllowAny
# Create your views here.

def index(request):
    """
    This will basiclly render index page.
    """
    return render(request, 'welcome.html')

def users(request):
    """
    This function will fetch all users info from Users model and then will pass it to 
    users.html template for tempalte patching.
    """
    users = User.objects.all()
    return render(request, 'users.html', {'user_list': users})

def add_user(request):
    if request.method == 'POST':    
        user_name = request.POST['user_name']
        first_name = request.POST['first_name'] 
        last_name =  request.POST['last_name']
        email =  request.POST['email']
        pass1 =  request.POST['pass1']
        pass2 =  request.POST['pass2']
        print('user_name,pass1, pass2', user_name, pass1, pass2)
        if user_name and first_name and email and pass1 == pass2:
            user = User(username=user_name, first_name=first_name, last_name=last_name, 
                   email=email, password=pass2)
            user.save()
            return redirect('users')
        else:
            return HttpResponse("please fill all the fileds.")
    return render(request, 'add_user.html')

def delete_user(request, id):
    """
    This function will get id from url mapping end point.
    and on basis of thta id will fecth that unique users and will delete user.
    """
    user_id = int(id)
    if user_id:
        users = User.objects.get(id=id)
        users.delete()
        return HttpResponse("User deleted successfully.")
    else:
        return HttpResponse("Failed to delete user.")


def upload_data(request):
    """
    This function will handle upload chunk data. 
    """
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        UploadedData.objects.create(data_file=uploaded_file)
        return render(request, 'upload_data.html')
    return render(request, 'upload_data.html')

class MyChunkedUploadCompleteView(ChunkedUploadCompleteView):
    permission_classes = [AllowAny] 
    def on_completion(self, uploaded_file):
        pass

class MyChunkedUploadView(ChunkedUploadView):
    permission_classes = [AllowAny] 
    pass

def query_builder(request):
    return render(request, 'query_builder.html')