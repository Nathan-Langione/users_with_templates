from django.shortcuts import render, redirect
from .models import Users
def index(request):
    context = {
        "all_users": Users.objects.all()    
    }
    return render(request,'index.html', context)

def process(request):
    if request.method=="POST":
        for key, value in request.POST.items():
            print('Key: %s' % (key) ) 
            # print(f'Key: {key}') in Python >= 3.7
            print('Value %s' % (value) )
            # print(f'Value: {value}') in Python >= 3.7 
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        new_user = Users.objects.create(first_name=first_name,last_name=last_name, email_address=email, age=age)
        new_user.save()
    return redirect("/")

