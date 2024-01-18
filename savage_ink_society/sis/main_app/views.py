# main_app/views 
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Profile, TattooImg, Comment
from django.urls import reverse_lazy

# Create your views here.

# Splash View
def splash(request):
    return render(request, 'splash.html')

# About View
def about(request):
    return render(request, 'about.html')

# Profile Create
class ProfileCreate(CreateView):
    model = Profile
    fields = ['profile_img', 'bio', 'location', 'birth_date', 'astrological_sign']
    template_name = 'profiles/profile_form.html'  # Specify the template name
    success_url = reverse_lazy('profile_list')

# Profile list 
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/list.html', {
        'profiles': profiles
    })
    
# Profile Detail
def profile_details(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    tattoo_imgs = TattooImg.objects.filter(comments__username=profile.username)
    comments = Comment.objects.filter(username=profile.username)
    
    return render(request, 'profiles/details.html', {
        'profile': profile,
        'tattoo_imgs': tattoo_imgs,
        'comments': comments,
    })
