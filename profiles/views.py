from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .update import UpdateProfile,UpdateUser
# Create your views here.
@login_required
def profiles(request):
    if request.method=='POST':
        u_form=UpdateUser(request.POST,instance=request.user)
        p_form=UpdateProfile(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.info(request,'your profile has been updated')
            return redirect('profiles')
    else:
        u_form=UpdateUser(instance=request.user)
        p_form=UpdateProfile(instance=request.user.profile)

    return render(request,'regis/profiles.html',{'uform':u_form,'pform':p_form})