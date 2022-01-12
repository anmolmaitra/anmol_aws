from django import forms

from .models import TaskStatus, Tasks, TaskCategory

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = [
            'taskName',
            'category',
            'entryDt',
            'completionDt',
            'taskStatus'
        ]
        widgets = {
            'entryDt': forms.DateInput(attrs={'type': 'date'}),
            'completionDt': forms.DateInput(attrs={'type':'date'})
        }