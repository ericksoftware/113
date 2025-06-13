from django.urls import path
from .views import (
    IssueListView, IssueDetailView,
    IssueCreateView, IssueUpdateView,
    IssueDeleteView, BoardView
)

app_name = 'issues'  # Esta línea es importante

urlpatterns = [
    path('', IssueListView.as_view(), name='issue_list'),
    path('<int:pk>/', IssueDetailView.as_view(), name='issue_detail'),
    path('new/', IssueCreateView.as_view(), name='issue_create'),
    path('<int:pk>/edit/', IssueUpdateView.as_view(), name='issue_update'),
    path('<int:pk>/delete/', IssueDeleteView.as_view(), name='issue_delete'),
    path('board/', BoardView.as_view(), name='board'),
]