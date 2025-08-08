from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View

from django.views.generic.edit import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


from .models import Task

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')  # Redirect to the task list after login
    
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')  # Redirect to login after registration
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    
        
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/task_list.html'

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            queryset = queryset.filter(title__icontains=search_input)
        # Order by completed status (False first) then by created date
        return queryset.order_by('completed', '-created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = context['tasks'].filter(completed=False).count()
        context['search_input'] = self.request.GET.get('search-area') or ''
        # Get user's first name or username if first name is not set
        context['user_name'] = self.request.user.first_name or self.request.user.username
        return context
        

class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description']  # Remove 'completed' from fields
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title', 'description']
    success_url = reverse_lazy('tasks')  # Redirect to the task list after update
  
class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    template_name = 'base/task_confirm_delete.html'
    success_url = reverse_lazy('tasks')  # Redirect to the task list after deletion
    context_object_name = 'tasks'


# Custom logout view to allow GET requests
class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class TaskToggleComplete(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = Task.objects.get(id=pk, user=request.user)
        task.completed = not task.completed
        task.save()
        return HttpResponseRedirect(reverse_lazy('tasks'))