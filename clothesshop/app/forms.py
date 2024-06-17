from django import forms
from django.contrib.auth.models import User

from .models import UserProfile, Category, Brand, Product, ProductImage, ProductVideo, Cart, CartProduct, Comment, LikeProduct, Dislike

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    user = UserForm()

    class Meta:
        model = UserProfile
        fields = ['user', 'image', 'address', 'phone', 'date_of_birth', 'status']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'parent']

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'description']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'brand', 'name', 'description', 'price', 'stock', 'available']

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['product', 'image']

class ProductVideoForm(forms.ModelForm):
    class Meta:
        model = ProductVideo
        fields = ['product', 'video']

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user']

class CartProductForm(forms.ModelForm):
    class Meta:
        model = CartProduct
        fields = ['cart', 'product', 'quantity']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'product', 'parent', 'content']

class LikeProductForm(forms.ModelForm):
    class Meta:
        model = LikeProduct
        fields = ['user', 'product']

class DislikeForm(forms.ModelForm):
    class Meta:
        model = Dislike
        fields = ['user', 'product']
