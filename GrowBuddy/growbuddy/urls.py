from django.contrib import admin
from django.urls import path, include
from skills import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.SkillListView.as_view(), name='home'),
    path('skill/add/', views.SkillCreateView.as_view(), name='skill-add'),
    path('skill/<int:pk>/', views.SkillUpdateView.as_view(), name='skill-update'),
    path('skill/<int:pk>/delete/', views.SkillDeleteView.as_view(), name='skill-delete'),
]