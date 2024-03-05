from django.urls import include, path, re_path
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.views.generic.base import RedirectView

admin.site.site_header = "Rental Admin"
admin.site.site_title = "Rental Admin Portal"
admin.site.index_title = "Welcome to Rental Admin Portal"

urlpatterns = [
    path('', RedirectView.as_view(url='/index/')),
    path('index/', views.index, name='home'),
    path('recommended/', views.recommended, name='recommended'),
    path('home/', views.home),
    path('contact/', views.contact),
    path('about/', views.about),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('password_reset_request/', views.password_reset_request, name='passwordresetrequest'),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='passwordreset'),
    path('password_change/', views.password_change, name='passwordchange'),
    path('profile/', views.profile, name='profile'),
    path('post/', views.post),
    path('posth/', views.posth),
    path('logout/', views.user_logout, name='logout'),
    path('descr/', views.descr),
    path('deleter/', views.deleter),
    path('deleteh/', views.deleteh),
    path('search/', views.search),
    path('chat/', views.chat_view, name='chat'),
    path('book_house/', views.book_house, name='book_house'),
    path('book_room/', views.book_room, name='book_room'),
    path('initiate/', views.initkhalti, name='initiate'),
    path('verify/', views.verifykhalti, name='verify'),
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
