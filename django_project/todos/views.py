from http import HTTPStatus
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.http.response import JsonResponse
from django.template.response import TemplateResponse
from django.views.generic import View
from requests import Response

from django_project.todos.forms import CreateTodoForm

from .models import TodoMapper


class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = CreateTodoForm()
        todo_list = request.user.todo_set.all()
        context = {
            'todo_list': todo_list,
            'form': form,
        }
        return TemplateResponse(request, 'todos/todo_list.html', context)

    def post(self, request: HttpRequest, *args, **kwargs):
        if 'method' not in request.POST.keys():
            return self.create(request)
        elif request.POST['method'] == 'UPDATE':
            return self.update(request)
        elif request.POST['method'] == 'DELETE':
            return self.delete(request)
        else:
            raise Exception('method setできていない')

    def create(self, request,):
        form = CreateTodoForm(request.POST)

        if not form.is_valid():
            return JsonResponse({
            })

        todo = form.save(commit=False)
        todo.user_id = request.user.id
        todo.save()
        todo_dict = TodoMapper(todo).as_dict()

        return JsonResponse({
            'todo': todo_dict,
        })

    def update(self, request,):
        todo = request.user.todo_set.get(pk=request.POST['id'])
        todo.name = request.POST['name']
        print(request.POST['completed'].capitalize())
        todo.completed = request.POST['completed'].capitalize()
        todo.save()
        return JsonResponse({
            'todo': TodoMapper(todo).as_dict(),
        })

    def delete(self, request,):

        todo = request.user.todo_set.get(pk=request.POST['id'])
        todo.delete()
        return JsonResponse({
            'todo': TodoMapper(todo).as_dict(),
        })


index = IndexView.as_view()
