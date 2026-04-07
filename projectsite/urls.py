from django.contrib import admin
from django.urls import path, include
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # PWA
    path('', include('pwa.urls')),
    
    # Home page  ← ADD THIS LINE
    path('', views.HomePageView.as_view(), name='home'),
    
    # AllAuth Authentication
    path('accounts/', include('allauth.urls')),

    # Task URLs
    path('task_list/', views.TaskList.as_view(), name='task-list'),
    path('task_list/add/', views.TaskCreateView.as_view(), name='task-add'),
    path('task_list/<pk>/', views.TaskUpdateView.as_view(), name='task-update'),
    path('task_list/<pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),

    # Priority URLs
    path('priority_list/', views.PriorityList.as_view(), name='priority-list'),
    path('priority_list/add/', views.PriorityCreateView.as_view(), name='priority-add'),
    path('priority_list/<pk>/', views.PriorityUpdateView.as_view(), name='priority-update'),
    path('priority_list/<pk>/delete/', views.PriorityDeleteView.as_view(), name='priority-delete'),

    # Category URLs
    path('category_list/', views.CategoryList.as_view(), name='category-list'),
    path('category_list/add/', views.CategoryCreateView.as_view(), name='category-add'),
    path('category_list/<pk>/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category_list/<pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),

    # Note URLs
    path('note_list/', views.NoteList.as_view(), name='note-list'),
    path('note_list/add/', views.NoteCreateView.as_view(), name='note-add'),
    path('note_list/<pk>/', views.NoteUpdateView.as_view(), name='note-update'),
    path('note_list/<pk>/delete/', views.NoteDeleteView.as_view(), name='note-delete'),

    # SubTask URLs
    path('subtask_list/', views.SubTaskList.as_view(), name='subtask-list'),
    path('subtask_list/add/', views.SubTaskCreateView.as_view(), name='subtask-add'),
    path('subtask_list/<pk>/', views.SubTaskUpdateView.as_view(), name='subtask-update'),
    path('subtask_list/<pk>/delete/', views.SubTaskDeleteView.as_view(), name='subtask-delete'),
]