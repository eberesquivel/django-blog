from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostFormulario
from django.shortcuts import redirect
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detalle.html', {'post': post})

def post_new(request):
        form = PostFormulario()
        return render(request, 'blog/post_editar.html', {'form': form})

def post_new(request):
        if request.method == "POST":
            form = PostFormulario(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.fecha_publicacion = timezone.now()
                post.save()
                return redirect('post_detalle', pk=post.pk)
        else:
            form = PostFormulario()
        return render(request, 'blog/post_editar.html', {'form': form})