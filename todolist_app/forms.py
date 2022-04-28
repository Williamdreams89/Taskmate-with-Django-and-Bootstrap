from django import forms 
from todolist_app.models import Todolist

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['task', 'task_date','starts_from','ends_at']