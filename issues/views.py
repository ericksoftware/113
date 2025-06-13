from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Issue, Status
from accounts.models import Team

class IssueListView(LoginRequiredMixin, ListView):
    model = Issue
    template_name = 'issues/issue_list.html'
    context_object_name = 'issues'

class IssueDetailView(LoginRequiredMixin, DetailView):
    model = Issue
    template_name = 'issues/issue_detail.html'

class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    template_name = 'issues/issue_form.html'
    fields = ['title', 'summary', 'description', 'assignee', 'status', 'assigned_team']
    
    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)

class IssueUpdateView(LoginRequiredMixin, UpdateView):
    model = Issue
    template_name = 'issues/issue_form.html'
    fields = ['title', 'summary', 'description', 'assignee', 'status', 'assigned_team']

class IssueDeleteView(LoginRequiredMixin, DeleteView):
    model = Issue
    template_name = 'issues/issue_confirm_delete.html'
    success_url = reverse_lazy('issues:issue_list')

    from django.db.models import Q

class BoardView(LoginRequiredMixin, ListView):
    template_name = 'issues/board.html'
    context_object_name = 'issues'

    def get_queryset(self):
        # Obtener el nombre del equipo del parámetro GET
        team_name = self.request.GET.get('team')
        if team_name:
            # Filtrar por el nombre del equipo usando la relación assigned_team
            return Issue.objects.filter(assigned_team__name=team_name)
        return Issue.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener los estados (deberías crearlos primero en la base de datos)
        todo_status = Status.objects.get(name='To Do')
        in_progress_status = Status.objects.get(name='In Progress')
        done_status = Status.objects.get(name='Done')
        
        # Filtrar issues por estado
        queryset = self.get_queryset()
        context['todo_issues'] = queryset.filter(status=todo_status)
        context['in_progress_issues'] = queryset.filter(status=in_progress_status)
        context['done_issues'] = queryset.filter(status=done_status)
        
        # Añadir equipos para el filtro (opcional)
        context['teams'] = Team.objects.all()  # Ahora Team está importado correctamente
        return context
