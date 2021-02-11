from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Category, Product


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    categories = Category.objects.all()
    query = None
    item_category = 'All'

    if request.GET:
            
        if 'category' in request.GET:
            item_category = request.GET['category']
            products = products.filter(category__name=item_category)
            # Sorting functionality for all items and each category
            if 'sort' in request.GET:
                sort_by = request.GET['sort']
                if item_category == 'All':
                    products = Product.objects.order_by(sort_by)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'categories': categories,
        'active_category': item_category,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
