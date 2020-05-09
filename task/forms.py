from django import forms
from .models import MasterTasks

class replyToTaskForm(forms.ModelForm):
    class Meta:
        model=MasterTasks
        fields=['answer']


class rejectTaskForm(forms.ModelForm):
    approverComment = forms.CharField(widget=forms.Textarea, label='')
    class Meta:
        model = MasterTasks
        fields = ['approverComment']
