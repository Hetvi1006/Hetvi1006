"""ecomelectronic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path 
#importing the views we created 
from users import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('auth/',include('users.urls')),
    path('register/',user_views.register, name="register"),
    path('index/',views.index, name="index"),
    path('prodadd/', views.prodadd,name="prodadd"),  
    path('show/',views.show,name="show"), 
    path('category/', views.category,name="category"),  
    path('catshow/',views.catshow,name="catshow"), 
    path('usertable/',views.usertable,name="usertable"), 
    path('profile/', user_views.profile, name='profile'),
    path('upload/', views.upload, name = 'upload'), 
    path('Cart/', views.Cart, name = 'Cart'),
    path('addtocart/<str:id>', views.addtocart, name = 'addtocart'), 
    path('profileshow/', user_views.profileshow, name='profileshow'),
    path('delete/<int:id>', views.delete,name='delete'), 
    path('udelete/<int:id>', views.udelete,name='udelete'),
    path('edit/<int:id>', views.edit,name='edit'),  
    path('update/<int:id>', views.update,name='update'),
    path('editproduct/<int:id>', views.editproduct,name='editproduct'),  
    path('updateproduct/<int:id>', views.updateproduct,name='updateproduct'),
    path('adminp/',views.adminp,name='adminp'),
    path('login/',auth_views.LoginView.as_view(template_name='auth/login.html'), name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='auth/logout.html'), name="logout"),
    path('home/',user_views.home, name="home"),
    url(r'^about/', views.about,name='about'),
    path('checkout/', views.checkout,name='checkout'),
    url(r'^feedback/',views.feedback,name='feedback'),
    url(r'^contact/', views.contact,name='contact'),
    url(r'^payment/', views.payment,name='payment'),
    url(r'^electronics/', views.electronics,name='electronics'),
    url(r'^product2/', views.product2,name='product2'),
    url(r'^single/', views.single,name='single'),
    url(r'^single2/', views.single2,name='single2'),
    url(r'^password/$', views.change_password, name='change_password'),
    # url(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
    #  url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    # url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url('^', include('django.contrib.auth.urls')),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)