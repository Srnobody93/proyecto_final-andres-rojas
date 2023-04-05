from django.urls import path
from . import views
from . views import PostListView, PostDetailView, PostCreateView, PostUpdateview, PostDeleteView

urlpatterns = [

    path("", PostListView.as_view(), name = "blog-home"),
    path("post/new", PostCreateView.as_view(), name = "blog-new"),
    path('post/<int:pk>/', PostDetailView.as_view(), name = "blog-detail"),
    path('post/<int:pk>/update', PostUpdateview.as_view(), name = "blog-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name = "blog-delete"),
    path('about/', views.about, name='blog-about'),
    
]
 