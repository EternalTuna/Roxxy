from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Post, SocialCard
from .forms import SocialCardForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context = {'error_message': 'Invalid login credentials'}
    else:
        context = {}
    return render(request, 'posts/login.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
        post = Post.objects.create(title=title, content=content, author=author)
        return redirect('view_post', post.id)
    return render(request, 'posts/create_post.html')

@login_required
def view_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/view_post.html', {'post': post})

@login_required
def create_social_card(request):
    if request.method == 'POST':
        form = SocialCardForm(request.POST, request.FILES)
        if form.is_valid():
            social_card = form.save(commit=False)
            social_card.author = request.user
            social_card.save()
            return redirect('view_social_card', social_card.id)
    else:
        form = SocialCardForm()
    return render(request, 'posts/create_social_card.html', {'form': form})

@login_required
def view_social_card(request, social_card_id):
    social_card = SocialCard.objects.get(id=social_card_id)
    return render(request, 'posts/view_social_card.html', {'social_card': social_card})
# Create your views here.


def base(request):
    return render(request, 'posts/base.html')

@csrf_exempt
def nfc_url(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        # TODO: handle the URL and return appropriate response
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})

