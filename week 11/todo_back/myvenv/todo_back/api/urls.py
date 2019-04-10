from django.urls import path, re_path
from api.views import show_lists, index, n_list, n_list_tasks
urlpatterns = [
    path('task_lists/', show_lists),
    path('task_lists/<int:num>/', n_list),
    path('task_lists/<int:num>/tasks/', n_list_tasks)
]