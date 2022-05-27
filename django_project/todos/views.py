from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse
from django.template.response import TemplateResponse
from django.views.generic import View

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

    def post(self, request, *args, **kwargs):
        # if 'todo' in request.POST:
        #     return self.delete(request)

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

    # def delete(self, request,):
    #     todo = request.POST['todo']
    #     request.user.city_set.filter(name=todo).delete()
    #     messages.error(request, f"{todo}の登録を解除しました")
    #     return HttpResponseRedirect(reverse('todos:index'))


index = IndexView.as_view()
