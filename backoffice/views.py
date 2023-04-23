from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from django.views.generic import ListView

from .models import Product, Category, Promotion
from .forms import ProductForm, PromotionForm, LoginForm, CategoryForm


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {'products': products, 'categories': categories})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_edit.html', {'category': category})


def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect('backoffice:category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_add.html', {'form': form})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('backoffice:category_list')
    return render(request, 'category_delete.html', {'category': category})


def product_list(request):
    product = Product.objects.all()
    return render(request, 'product_list.html', {'products': product})


@login_required
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, 'Product added successfully!')
            return redirect('backoffice:product_list')
    else:
        form = ProductForm()
    return render(request, 'product_add.html', {'form': form})


@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('backoffice:home')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_edit.html', {'form': form})


@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('backoffice:product_list')


def promotion_list(request):
    promotion = Promotion.objects.all()
    return render(request, 'promotion_list.html', {'promotions': promotion})


@login_required
def promotion_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            promotion = form.save(commit=False)
            promotion.product = product
            promotion.save()
            messages.success(request, 'Promotion added successfully!')
            return redirect('backoffice:home')
    else:
        form = PromotionForm()
    return render(request, 'promotion_add.html', {'form': form, 'product': product})


@login_required
def promotion_edit(request, pk):
    promotion = get_object_or_404(Promotion, pk=pk)
    if request.method == 'POST':
        form = PromotionForm(request.POST, instance=promotion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Promotion updated successfully!')
            return redirect('backoffice:home')
    else:
        form = PromotionForm(instance=promotion)
    return render(request, 'promotion_edit.html', {'form': form, 'promotion': promotion})


@login_required
def promotion_delete(request, pk):
    promotion = get_object_or_404(Promotion, pk=pk)
    if request.method == 'POST':
        promotion.delete()
        messages.success(request, 'Promotion deleted successfully!')
        return redirect('backoffice:home')
    return render(request, 'promotion_delete.html', {'promotion': promotion})


def catalog(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    query = request.GET.get('q')
    if query:
        products = products.filter(Q(name__icontains=query) | Q(category__name__icontains=query))
    return render(request, 'catalogue.html', {'products': products, 'categories': categories})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_view(request, user)
            return redirect('backoffice:home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout_view(request)
    return redirect('home')


# class PromotionListView(ListView):
#     model = Promotion
#     template_name = 'promotion_list.html'
