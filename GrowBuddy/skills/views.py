from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Skill

class SkillListView(ListView):
    model = Skill
    template_name = 'skills/home.html'
    context_object_name = 'skills'

class SkillCreateView(CreateView):
    model = Skill
    fields = ['name', 'description', 'progress']
    success_url = '/'

class SkillUpdateView(UpdateView):
    model = Skill
    fields = ['name', 'description', 'progress']
    success_url = '/'

class SkillDeleteView(DeleteView):
    model = Skill
    success_url = '/'
