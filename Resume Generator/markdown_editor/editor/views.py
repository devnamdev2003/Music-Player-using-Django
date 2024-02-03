from django.shortcuts import render
from .models import MarkdownDocument
from .forms import MarkdownForm
import markdown

def editor_view(request):
    documents = MarkdownDocument.objects.all()
    return render(request, 'editor/editor.html', {'documents': documents})

def create_document(request):
    if request.method == 'POST':
        form = MarkdownForm(request.POST)
        if form.is_valid():
            form.save()
            return render_markdown(request, form.instance.content)
    else:
        form = MarkdownForm()
    return render(request, 'editor/create_document.html', {'form': form})

def render_markdown(request, content):
    import markdown
    markdown = markdown.markdown(content)
    return render(request, 'editor/render_markdown.html', {'content': content, 'markdown': markdown})
