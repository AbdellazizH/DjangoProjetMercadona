from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from django.views.generic import ListView

from .models import Product, Category, Promotion
from .forms import ProductForm, PromotionForm


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {'products': products, 'categories': categories})


@login_required
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, 'Product added successfully!')
            return redirect('home')
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
            return redirect('home')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_edit.html', {'form': form})


@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')


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
            return redirect('home')
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
            return redirect('home')
    else:
        form = PromotionForm(instance=promotion)
    return render(request, 'promotion_edit.html', {'form': form, 'promotion': promotion})


@login_required
def promotion_delete(request, pk):
    promotion = get_object_or_404(Promotion, pk=pk)
    if request.method == 'POST':
        promotion.delete()
        messages.success(request, 'Promotion deleted successfully!')
        return redirect('home')
    return render(request, 'promotion_delete.html', {'promotion': promotion})


def catalog(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    query = request.GET.get('q')
    if query:
        products = products.filter(Q(name__icontains=query) | Q(category__name__icontains=query))
    return render(request, 'catalogue.html', {'products': products, 'categories': categories})


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'


class PromotionListView(ListView):
    model = Promotion
    template_name = 'promotion_list.html'
