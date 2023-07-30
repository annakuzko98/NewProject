from django import forms
from .models import DailyPlan, Blog_Post

class PlanCompletionForm(forms.Form):
    plan_id = forms.IntegerField(widget=forms.HiddenInput())

class DailyPlanForm(forms.ModelForm):
    class Meta:
        model = DailyPlan
        fields = ['plan_name', 'plan_description', 'plan_date', 'plan_time', 'completed']
        widgets = {
            'plan_date': forms.DateInput(attrs={'type': 'date'}),
            'plan_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class Blog_PostForm(forms.ModelForm):
    class Meta:
        model = Blog_Post
        fields = ['post_name', 'post_description', 'post_date', 'post_time', 'Feeling', 'image']
        widgets = {
            'post_date': forms.DateInput(attrs={'type': 'date'}),
            'post_time': forms.TimeInput(attrs={'type': 'time'}),
            'Feeling': forms.Select(attrs={'class': 'form-control'}),
        }
