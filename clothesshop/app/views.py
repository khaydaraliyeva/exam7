from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from clothesshop.app.forms import UserProfileForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('user').username
            password = form.cleaned_data.get('user').password
            email = form.cleaned_data.get('user').email

            # Yangi User yaratish
            user = User.objects.create_user(username=username, password=password, email=email)

            # UserProfile yaratish va saqlash
            profile = form.save(commit=False)
            profile.user = user
            profile.save()

            # Foydalanuvchini avtomatik kirish
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('home')  # Kerakli manzilga yo'naltirish
    else:
        form = UserProfileForm()

    return render(request, 'register.html', {'form': form})
