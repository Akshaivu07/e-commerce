from django.shortcuts import render,redirect,get_object_or_404
from capp.models import Category,Product,Client
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Cart

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='u_a_login')
def admin_home(request):
    return render(request,'admin_home.html')
@login_required(login_url='u_a_login')
def category(request):
    return render(request,'category.html')
def add_category(request):
    if request.method == 'POST':
        category_name=request.POST.get('adcategory')
        category=Category(category=category_name)
        category.save()
        return redirect('category')
    
@login_required(login_url='u_a_login')
def add_product(request):
    categories=Category.objects.all()
    return render(request,'add_product.html',{'category':categories})
def add_productdb(request):
    if request.method == 'POST':
        p_name=request.POST.get('pname')
        description=request.POST.get('description')
        price=request.POST.get('price')
        image=request.FILES.get('file')
        sel=request.POST.get('select')
        category1=Category.objects.get(id=sel)
        product=Product(product_name=p_name,description=description,price=price,image=image,cat=category1)
        product.save()
        return redirect('add_product')
@login_required(login_url='u_a_login')   
def product_view(request):
    product=Product.objects.all()
    return render(request,'product_view.html',{'products':product})

def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})
def u_a_login(request):
    return render(request,'login.html')
@login_required(login_url='u_a_login')
def usercreate(request):
    if request.method == 'POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['uname']
        password=request.POST['upassword']
        cpassword=request.POST['cpassword']
        email=request.POST['email']
        address=request.POST['address']
        contact=request.POST['contact']
        image=request.FILES.get('file')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username already exists!!!')
                return redirect('signup')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save()
                clients=Client(u_address=address,u_contact=contact,u_image=image,user=user)
                clients.save()
                messages.info(request,'successfully completed')
        else:
            messages.info(request,'password dosent match!!')
            return redirect('signup')
        return redirect('home')
    return render(request,'sign_up.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['upassword']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if user.is_superuser:
                
                return redirect('admin_home')
            else:
                return redirect('home')
        else:
            messages.info(request, 'Invalid username or password. Try again')
            return redirect('home')
    else:
        return redirect('home')

def signup(request):
    return render(request,'sign_up.html')
@login_required(login_url='u_a_login')
def mens(request):
    return render(request,'mens.html')
@login_required(login_url='u_a_login')
def category_page(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(cat=category)
    return render(request, 'mens.html', {'category': category, 'products': products})
@login_required(login_url='u_a_login')
def user_details(request):
    client=Client.objects.all()
    user=User.objects.all()
    return render(request,'view_user.html',{'client':client,'user':user})
def delete_user(request,user_id):
    c=Client.objects.get(user=user_id)
    u=User.objects.get(id=user_id)
    c.delete()
    u.delete()
    return redirect('user_details')
def delete_product(request,product_id):
    product=Product.objects.get(id=product_id)
    category = product.cat
    product.delete()
    category.delete()
    return redirect('product_view')
@login_required(login_url='u_a_login')
def cart_details(request,id):
    product=Product.objects.get(id=id)
    cart_item, created=Cart.objects.get_or_create(user=request.user,product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')
@login_required(login_url='u_a_login')
def cart(request):
    cart_items=Cart.objects.filter(user=request.user).select_related('product')
    total_price=sum(item.total_price() for item in cart_items)
    return render(request,'cart.html',{'cartitems':cart_items,'totalprice':total_price})

def decrease_quantity(request,id):
    cart_item=Cart.objects.get(product_id=id,user=request.user)
    cart_item.quantity -= 1
    cart_item.save()
    return redirect('cart')

def increase_quantity(request,id):
    cart_item=Cart.objects.get(product_id=id,user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')
def removecart(request,id):
    product=Product.objects.get(id=id)
    cart_item=Cart.objects.filter(user=request.user,product=product).first()
    if cart_item:
        cart_item.delete()
    return redirect('cart')



    







