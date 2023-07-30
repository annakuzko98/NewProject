from django.shortcuts import render, redirect, get_object_or_404
from .models import DailyPlan, Blog_Post
from .forms import DailyPlanForm, PlanCompletionForm, Blog_PostForm
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def main(request):
    context = {
        'title': 'Blog'
    }
    return render(request, 'main.html', context)

def daily_plan_create(request):
    if request.method == 'POST':
        form = DailyPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:list_daily_plans')
    else:
        form = DailyPlanForm()

    context = {
        'title': 'Create daily plan',
        'form': form,
    }
    return render(request, 'create_daily_plan.html', context)  # Шаблон для категорії Daily Plan
def view_daily_plan(request, plan_id):
    daily_plan = get_object_or_404(DailyPlan, pk=plan_id)

    if request.method == 'POST':
        form = DailyPlanForm(request.POST, instance=daily_plan)
        if form.is_valid():
            form.save()
            return redirect('blog:view_daily_plan', plan_id=plan_id)
    else:
        form = DailyPlanForm(instance=daily_plan)

    context = {
        'daily_plan': daily_plan,
        'form': form,
    }

    return render(request, 'view_daily_plan.html', context)

def list_daily_plans(request):
    # Отримуємо унікальні дати, для яких є плани
    dates_with_plans = DailyPlan.objects.values_list('plan_date', flat=True).distinct()

    context = {
        'dates_with_plans': dates_with_plans,
    }

    return render(request, 'list_daily_plans.html', context)
def daily_plans_by_date(request, date):
    plans_for_date = DailyPlan.objects.filter(plan_date=date)

    context = {
        'plans_for_date': plans_for_date,
        'selected_date': date,
    }

    return render(request, 'daily_plans_by_date.html', context)
def post(request):
    posts = Blog_Post.objects.all()
    paginator = Paginator(posts, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'title': 'Blog Post',
        'posts': posts,
        'page_request_var': page_request_var
    }
    return render(request, 'blog_post.html', context) # Шаблон для категорії Thought
def create_post(request):
    if request.method == 'POST':
        form = Blog_PostForm(request.POST)
        if form.is_valid():  # Validate the form data
            form.save()  # Save the data to the database
            return redirect('blog:blog_post')  # Replace 'name_of_redirect_view' with the appropriate URL name to redirect after successful form submission
    else:
        form = Blog_PostForm()
    context = {
        'title': 'Create post',
        'form': form,
    }

    return render(request, 'create_post.html', context)  # Replace 'your_template_name.html' with the actual template name





