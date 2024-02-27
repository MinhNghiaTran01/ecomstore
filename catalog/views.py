# Create your views here.
from django.shortcuts import get_object_or_404, render
from catalog.models import Category, Product

def index(request, template_name="catalog/index.html"):
    page_title = 'Musical Instruments and Sheet Music for Musicians'
    return render(request, template_name, {'page_title': page_title})

def show_category(request, category_slug, template_name="catalog/category.html"):
    print(category_slug)
    category = get_object_or_404(Category, slug=category_slug)
    products = category.product_set.all()
    page_title = category.name
    meta_keywords = category.meta_keywords
    meta_description = category.meta_description
    return render(request, template_name, {'category': category, 'products': products, 'page_title': page_title, 'meta_keywords': meta_keywords, 'meta_description': meta_description})

from django.shortcuts import get_object_or_404, render, redirect
from cart import cart
from catalog.models import Product
from catalog.forms import ProductAddToCartForm
from django.urls import reverse
# def show_product(request, product_slug, template_name="catalog/product.html"):
#     p = get_object_or_404(Product, slug=product_slug)
#     categories = p.categories.all()
#     page_title = p.name
#     meta_keywords = p.meta_keywords
#     meta_description = p.meta_description

#     if request.method == 'POST':
#         postdata = request.POST.copy()
#         form = ProductAddToCartForm(request, postdata)

#         if form.is_valid():
#             cart.add_to_cart(request)
            
#             if request.session.test_cookie_worked():
#                 request.session.delete_test_cookie()
                
#             url = reverse('show_cart')
#             return redirect(url)
#     else:
#         form = ProductAddToCartForm(request=request, label_suffix=':')
#         form.fields['product_slug'].widget.attrs['value'] = product_slug
#         request.session.set_test_cookie()

#     return render(request, template_name, locals())

def show_product(request, product_slug, template_name="catalog/product.html"): 
    p = get_object_or_404(Product, slug=product_slug) 
    categories = p.categories.all() 
    page_title = p.name 
    meta_keywords = p.meta_keywords 
    meta_description = p.meta_description 
    # need to evaluate the HTTP method 
    if request.method == 'POST': 
        # add to cart…create the bound form 
        postdata = request.POST.copy() 
        form = ProductAddToCartForm(request, postdata) 
        #check if posted data is valid 
        if form.is_valid(): 
        #add to cart and redirect to cart page
            cart.add_to_cart(request) 
            # if test cookie worked, get rid of it 
            if request.session.test_cookie_worked(): 
                request.session.delete_test_cookie() 
            url = reverse('show_cart')
            return redirect(url)
    else: 
        # it’s a GET, create the unbound form. Note request as a kwarg 
        form = ProductAddToCartForm(request=request, label_suffix=':') 
        # assign the hidden input the product slug 
        form.fields['product_slug'].widget.attrs['value'] = product_slug 
        # set the test cookie on our first GET request 
        request.session.set_test_cookie() 
    return render(request, template_name, locals())
