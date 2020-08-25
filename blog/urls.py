from django.contrib import admin
from django.urls import path
from post.views import PostListView, PostDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view()),
    path('<pk>', PostDetailView.as_view())
]
