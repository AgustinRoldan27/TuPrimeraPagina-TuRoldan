from django.shortcuts import render, redirect
from .models import Autor, Categoria, Post
from .forms import AutorForm, CategoriaForm, PostForm, BuscarPostForm

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'crear_autor.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'crear_categoria.html', {'form': form})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'crear_post.html', {'form': form})

def buscar_post(request):
    form = BuscarPostForm()
    posts = []
    if request.method == 'GET':
        form = BuscarPostForm(request.GET)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            posts = Post.objects.filter(titulo__icontains=titulo)
    return render(request, 'buscar_post.html', {'form': form, 'posts': posts})