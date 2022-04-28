from django.urls import path
from todolist_app import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('todolist/',views.todolist, name="todolist"),
    path('done_task/<task_id>', views.done_task, name="done_task"),
    path('pending_task/<task_id>', views.pending_task, name='pending_task'),
    path('delete_task/<task_id>', views.delete_task, name="delete_task"),
    path('edit_task/<task_id>',views.edit_task, name='edit_task')
]
