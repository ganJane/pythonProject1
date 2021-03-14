
from django.urls import path
from project1 import views
urlpatterns = [
    path('project1/', views.ProjectViews.as_view()),
    path('project1/<int:pk>',views.ProjectDetailView.as_view())
    ]