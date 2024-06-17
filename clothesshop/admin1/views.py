from django.shortcuts import render, get_object_or_404, redirect
from app.models import UserProfile, Category, Brand, Product, ProductImage, ProductVideo, Cart, CartProduct, Comment, LikeProduct, Dislike
from app.forms import UserProfileForm, CategoryForm, BrandForm, ProductForm, ProductImageForm, ProductVideoForm, CartForm, CartProductForm, CommentForm, LikeProductForm, DislikeForm






def dashboard(request):
    user_profile = UserProfile.objects.all()
    category = Category.objects.all()
    brand = Brand.objects.all()
    product = Product.objects.all()
    product_image = ProductImage.objects.all()
    product_video = ProductVideo.objects.all()
    cart = Cart.objects.all()
    cart_product = CartProduct.objects.all()
    comment = Comment.objects.all()
    like_product = LikeProduct.objects.all()
    dislike_product = Dislike.objects.all()
    context = {
        'user_profile': user_profile,
        'category': category,
        'brand': brand,
        'product': product,
        'product_image': product_image,
        'product_video': product_video,
        'cart': cart,
        'cart_product': cart_product,
        'comment': comment,
        'like_product': like_product,
        'dislike_product': dislike_product
        }
    return render(request, 'admin1/dashboard.html',context=context)









# UserProfile CRUD
def create_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_profile_list')
    else:
        form = UserProfileForm()
    return render(request, 'user_profile_form.html', {'form': form})

def user_profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'user_profile_list.html', {'profiles': profiles})

def user_profile_detail(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    return render(request, 'user_profile_detail.html', {'profile': profile})

def update_user_profile(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile_detail', pk=profile.pk)
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'user_profile_form.html', {'form': form})

def delete_user_profile(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('user_profile_list')
    return render(request, 'user_profile_confirm_delete.html', {'profile': profile})

# Category CRUD
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_detail.html', {'category': category})

def update_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_detail', pk=category.pk)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})

# Brand CRUD
def create_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brand_list')
    else:
        form = BrandForm()
    return render(request, 'brand_form.html', {'form': form})

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'brand_list.html', {'brands': brands})

def brand_detail(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    return render(request, 'brand_detail.html', {'brand': brand})

def update_brand(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('brand_detail', pk=brand.pk)
    else:
        form = BrandForm(instance=brand)
    return render(request, 'brand_form.html', {'form': form})


def delete_brand(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        brand.delete()
        return redirect('brand_list')
    return render(request, 'brand_confirm_delete.html', {'brand': brand})

# Product CRUD
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})

# ProductImage CRUD
def create_product_image(request):
    if request.method == 'POST':
        form = ProductImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_image_list')
    else:
        form = ProductImageForm()
    return render(request, 'product_image_form.html', {'form': form})

def product_image_list(request):
    images = ProductImage.objects.all()
    return render(request, 'product_image_list.html', {'images': images})

def product_image_detail(request, pk):
    image = get_object_or_404(ProductImage, pk=pk)
    return render(request, 'product_image_detail.html', {'image': image})

def update_product_image(request, pk):
    image = get_object_or_404(ProductImage, pk=pk)
    if request.method == 'POST':
        form = ProductImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('product_image_detail', pk=image.pk)
    else:
        form = ProductImageForm(instance=image)
    return render(request, 'product_image_form.html', {'form': form})

def delete_product_image(request, pk):
    image = get_object_or_404(ProductImage, pk=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('product_image_list')
    return render(request, 'product_image_confirm_delete.html', {'image': image})

# ProductVideo CRUD
def create_product_video(request):
    if request.method == 'POST':
        form = ProductVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_video_list')
    else:
        form = ProductVideoForm()
    return render(request, 'product_video_form.html', {'form': form})

def product_video_list(request):
    videos = ProductVideo.objects.all()
    return render(request, 'product_video_list.html', {'videos': videos})

def product_video_detail(request, pk):
    video = get_object_or_404(ProductVideo, pk=pk)
    return render(request, 'product_video_detail.html', {'video': video})

def update_product_video(request, pk):
    video = get_object_or_404(ProductVideo, pk=pk)
    if request.method == 'POST':
        form = ProductVideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return redirect('product_video_detail', pk=video.pk)
    else:
        form = ProductVideoForm(instance=video)
    return render(request, 'product_video_form.html', {'form': form})


def delete_product_video(request, pk):
    video = get_object_or_404(ProductVideo, pk=pk)
    if request.method == 'POST':
        video.delete()
        return redirect('product_video_list')
    return render(request, 'product_video_confirm_delete.html', {'video': video})

# Cart CRUD
def create_cart(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cart_list')
    else:
        form = CartForm()
    return render(request, 'cart_form.html', {'form': form})

def cart_list(request):
    carts = Cart.objects.all()
    return render(request, 'cart_list.html', {'carts': carts})

def cart_detail(request, pk):
    cart = get_object_or_404(Cart, pk=pk)
    return render(request, 'cart_detail.html', {'cart': cart})

def update_cart(request, pk):
    cart = get_object_or_404(Cart, pk=pk)
    if request.method == 'POST':
        form = CartForm(request.POST, instance=cart)
        if form.is_valid():
            form.save()
            return redirect('cart_detail', pk=cart.pk)
    else:
        form = CartForm(instance=cart)
    return render(request, 'cart_form.html', {'form': form})

def delete_cart(request, pk):
    cart = get_object_or_404(Cart, pk=pk)
    if request.method == 'POST':
        cart.delete()
        return redirect('cart_list')
    return render(request, 'cart_confirm_delete.html', {'cart': cart})

# CartProduct CRUD
def create_cart_product(request):
    if request.method == 'POST':
        form = CartProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cart_product_list')
    else:
        form = CartProductForm()
    return render(request, 'cart_product_form.html', {'form': form})

def cart_product_list(request):
    cart_products = CartProduct.objects.all()
    return render(request, 'cart_product_list.html', {'cart_products': cart_products})

def cart_product_detail(request, pk):
    cart_product = get_object_or_404(CartProduct, pk=pk)
    return render(request, 'cart_product_detail.html', {'cart_product': cart_product})

def update_cart_product(request, pk):
    cart_product = get_object_or_404(CartProduct, pk=pk)
    if request.method == 'POST':
        form = CartProductForm(request.POST, instance=cart_product)
        if form.is_valid():
            form.save()
            return redirect('cart_product_detail', pk=cart_product.pk)
    else:
        form = CartProductForm(instance=cart_product)
    return render(request, 'cart_product_form.html', {'form': form})

def delete_cart_product(request, pk):
    cart_product = get_object_or_404(CartProduct, pk=pk)
    if request.method == 'POST':
        cart_product.delete()
        return redirect('cart_product_list')
    return render(request, 'cart_product_confirm_delete.html', {'cart_product': cart_product})

# Comment CRUD
def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comment_list')
    else:
        form = CommentForm()
    return render(request, 'comment_form.html', {'form': form})

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'comment_list.html', {'comments': comments})

def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    return render(request, 'comment_detail.html', {'comment': comment})

def update_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comment_form.html', {'form': form})


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('comment_list')
    return render(request, 'comment_confirm_delete.html', {'comment': comment})

# LikeProduct CRUD
