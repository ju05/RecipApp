from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from main.models import Ingredient, Recipe, UserProfile
from .forms import ProfileForm, RecipeForm
from django.db.models import Q
from django.db.models import OuterRef, Subquery
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import generic
from RecipApp.quickstart import main

def home(request):
    total_recipes = Recipe.objects.all().count()
    context = {
        'title':'Homepage',
        'total_recipes': total_recipes
    }    
    return render(request, 'home.html', context)

# -------------------------------------SIGNIN SIGNUP ------------------------------
def signup(request): 
    form = UserCreationForm(request.POST) 
    if form.is_valid(): 
        form.save() 
        username = form.cleaned_data.get('username') 
        password = form.cleaned_data.get('password') 
        user = authenticate(username=username, password=password) 
        login(request, user) 
        return redirect('home') 
    context = { 
        'form': form 
    } 
    return render(request, 'signup.html', context) 

def signin(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authernticate
        user = authenticate(username = username, password = password)
        if user is not None:
            # login takes request and the user associated
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'login.html', {'form': AuthenticationForm(request.POST)})
    
    else:
        return render(request, 'login.html', {'form': AuthenticationForm})


# ------------------------------------PROFILE VIEWS--------------------------------
def update_profile(request):
    
    profile = request.user.userprofile
    form = ProfileForm(request.POST or None, instance=profile)
    context = {'form': form} 

    if form.is_valid():
        form.save()
        return redirect('profile')

    return render(request, 'update_profile.html', context)


def profile(request):
    user = request.user
    profile = user.userprofile        
    context = {'profile': profile}

    return render(request, 'profile.html', context)

# ---------------------------------- SEARCH BAR ----------------------------------------

def search(request):    
    recipes = Recipe.objects.all()    
    if request.method == 'GET':
        query = request.GET.get('search') 
        queryset = recipes.filter(Q(title__icontains=query))       
        results = recipes.filter(Q(title__icontains=query))
        results = recipes.filter(Q(description__icontains=query))
        results = recipes.filter(Q(ingredients__icontains=query))
        results = recipes.filter(Q(instructions__icontains=query))
        total = results.count() 
    if request.GET.get("Meal"):
        results = queryset.filter(Q(meal__title__icontains="breakfast"))
        topic = "breakfast" 
        print(request.POST)    
  
    # if request.GET.get("meal"):
    #     results = queryset.filter(Q(meal__title__icontains="breakfast"))
    #     topic = "meal"

    # if request.method == 'GET':
    #     query = request.GET.get('search')
    #     meal = Meal.objects.filter(title = query)        
    #     results = Recipe.objects.filter(Q(meal__in = Subquery(meal.values('title'))))
    context = {'query': query, 'results': results, 'total':total}
    return render(request, 'search.html', context)

# --------------------------------------------------RECIPES VIWES----------------------------------------------------------------------------

def detail(request, id):    
    recipe = Recipe.objects.filter(id = id)[0]   
    
    context = {'recipe':recipe}
    return render(request, 'detail.html', context)

def add_to_calendar(request, id):
    recipe = Recipe.objects.get(id = id)
    context = {'recipe':recipe}
    if request.method == 'POST':
        request.session['recipe_id'] = str(recipe.id)
        main(request)
    return render(request, 'add_to_calendar.html', context)

# ------------------------------------------------------CHEFS GROUP --------------------------------------------------------------------

def add_recipe(request):
    context = ({'form': RecipeForm, 'ingredients': Ingredient})

    if request.method == 'POST':
        form_filled = RecipeForm(request.POST)
        if form_filled.is_valid():
            form_filled.save()
            return redirect('homepage')
        else:
            print(form_filled.errors)
    
    return render(request, 'add_recipe.html', context)


