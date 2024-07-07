from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, SubCategory, Rating
from .forms import RatingForm, ProductForm
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    subcategories = None
    sort = request.GET.get('sort', 'brand')  
    order = request.GET.get('order', 'asc')  

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'subcategory' in request.GET:
            subcategories = request.GET.get('subcategory').split(',')
            products = products.filter(subcategory__name__in=subcategories)
            subcategories = SubCategory.objects.filter(name__in=subcategories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "It looks like you didn't weave any search terms into the box!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

     # Add sorting
    if sort == 'brand':
        ordering = 'brand' if order == 'asc' else '-brand'
    elif sort == 'name':
        ordering = 'name' if order == 'asc' else '-name'
    elif sort == 'category':
        ordering = 'category' if order == 'asc' else '-category'
    else:
        ordering = 'brand'

    products = products.order_by(ordering)       

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_subcategories': subcategories,
        'current_sort': sort,
        'current_order': order,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show product details """

    product = get_object_or_404(Product, pk=product_id)
    user_has_rated = False
    all_options = product.all_options()

    if request.user.is_authenticated:
        user_has_rated = Rating.objects.filter(product=product, user=request.user).exists()
    rating_form = RatingForm()
    
    context = {
        'product': product,
        'all_options': all_options,
        'rating_form': rating_form,
        'user_has_rated': user_has_rated,
    }

    return render(request, 'products/product_details.html', context)


@login_required
def add_rating(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    rating = None

    if request.method == 'POST':
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.product = product
            rating.user = request.user
            rating.save()
            messages.success(request, 'Thanks for rating!')
            return redirect('product_detail', product_id=product_id)
    else:
        rating_form = RatingForm()

    context = {
        'product': product,
        'rating_form': rating_form,
    }

    return render(request, 'products/product_details.html', context)


@login_required
def edit_rating(request, rating_id):

    rating = get_object_or_404(Rating, id=rating_id)

    # Only the user who created the review can edit it
    if rating.user != request.user:
        messages.error(request, "You can only edit your own reviews.")
        return redirect('product_detail', product_id=rating.product.id)

    if request.method == 'POST':
        form = RatingForm(request.POST,  instance=rating)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your rating has been updated.')
            return redirect('product_detail', product_id=rating.product.id)
        else:
            form = RatingForm(instance=rating)

            context = {
            'product': rating.product,
            'rating_form': rating_form,
        }

    return redirect('product_detail', product_id=rating.product.id)


@login_required
def delete_rating(request, rating_id):
    rating = get_object_or_404(Rating, id=rating_id)

    # Only the user who created the review can delete it
    if rating.user != request.user:
        messages.error(request, "You can only delete your own reviews.")
        return redirect('product_detail', product_id=rating.product.id)

    if request.method == 'POST':
        rating.delete()
        messages.success(request, 'Your rating has been deleted.')

    return redirect('product_detail', product_id=rating.product.id)

    return HttpResponseNotAllowed(['POST'])


# Store owner functionalities
@login_required
def add_product(request):
    """ Add products in webshop """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to do that, only store managers do.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        add_product_form = ProductForm(request.POST, request.FILES)
        if add_product_form.is_valid():
            product = add_product_form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', product_id=product_id))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        add_product_form = ProductForm()
    
    context = {
        'add_product_form': add_product_form,
    }

    return render(request, 'products/add_product.html', context)


@login_required
def edit_product(request, product_id):
    """ Edit product in webshop """
    if not request.user.is_superuser:
            messages.error(request, 'You do not have permission to do that, only store managers do.')
            return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        edit_product_form = ProductForm(request.POST, request.FILES, instance=product)
        if edit_product_form.is_valid():
            edit_product_form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', product_id=product_id))
        else:
            messages.error(request, 'Failed to update product.')
    else:
        edit_product_form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')
        
    context = {
        'edit_product_form': edit_product_form,
        'product': product,
    }

    return render(request, 'products/edit_product.html', context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from shop """

    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to do that, only store managers do.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Successfully deleted product!')
    return redirect(reverse('products'))
