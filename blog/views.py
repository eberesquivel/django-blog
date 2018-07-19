from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django import forms
from .forms import PostFormulario
from django.shortcuts import redirect
# Create your views here.
def post_lista(request):
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
                # post.fecha_publicacion = timezone.now()
                post.save()
                return redirect('post_detalle', pk=post.pk)
        else:
            form = PostFormulario()
        return render(request, 'blog/post_editar.html', {'form': form})

def post_editar(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostFormulario(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.save()
                return redirect('post_detalle', pk=post.pk)
        else:
            form = PostFormulario(instance=post)
        return render(request, 'blog/post_editar.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(fecha_publicacion__isnull=True).order_by('fecha_creacion')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publicar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publicar()
    return redirect('post_detalle', pk=pk)

def post_remover(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_lista')