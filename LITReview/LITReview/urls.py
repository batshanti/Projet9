from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from LITReview.views import CreateUserView


urlpatterns = [
    path('admin/', admin.site.urls, name='adminn'),
    path(
        '',
        LoginView.as_view(
            template_name='index.html',
            redirect_authenticated_user=True
        ),
        name='login'
    ),
    path('create_user/', CreateUserView.as_view(), name='create'),
    path(
        'logout/',
        LogoutView.as_view(template_name='logout.html'),
        name='logout'
    ),
    path('', include('Review_Ticket.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
