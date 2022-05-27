from django import forms
from django_project.todos.models import Todo


class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'id': 'todo-form-name', 'class': 'form-control',  'placeholder': ' Add a new todo', }),
        }

    def clean_name(self):
        value = self.cleaned_data['name']

        # add validation
        return value
