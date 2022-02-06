from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.blog, name='blog'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/edit', login_required(views.PostUpdateView.as_view()), name='post_edit'),
    path('<int:pk>/delete', views.post_delete, name='post_delete'),
]