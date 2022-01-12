"""AnmolSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pubpages.views import home_view, login_view
from Journal.views import journal_detail_view
from Pwd.views import pwd_list_view
from Tasks.views import TaskCreateView, TaskListView, TaskUpdateView, TaskDeleteView
from vocab.views import vocab_view
from Exercise_Day.views import ExerciseDayListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('home/', home_view),
    path('login/', login_view),
    path('journal/', journal_detail_view),
    path('pwd/', pwd_list_view),
    path('create_task/', TaskCreateView.as_view(), name='create-task'),
    path('<int:pk>/selectedDD=<selectedDD>/update/', TaskUpdateView.as_view(), name='update-task'),
    path('task_list/',TaskListView.as_view(), name='task-list'),
    path('<int:pk>/selectedDD=<selectedDD>/delete/',TaskDeleteView.as_view(), name='delete-task'),
    path('vocab', vocab_view),
    path('exerciseday_list/',ExerciseDayListView.as_view(), name='ExerciseDay-list')
]
