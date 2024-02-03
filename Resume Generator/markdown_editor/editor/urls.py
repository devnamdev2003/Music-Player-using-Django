from django.urls import path
from .views import editor_view, create_document, render_markdown

app_name = 'editor'

urlpatterns = [
    path('', editor_view, name='editor_view'),
    path('create/', create_document, name='create_document'),
    path('render/', render_markdown, name='render_markdown'),
]
