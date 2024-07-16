from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from users.views import Dashboard, HomePage, NewUserRegister, UserProfile

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", NewUserRegister.as_view(), name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("profile/", UserProfile.as_view(), name="profile"),
    path("", HomePage.as_view(), name="home"),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("todo/", include("todo.urls", namespace="todo")),
    path("medialibrary/", include("medialibrary.urls", namespace="medialibrary")),
    path("", include("car_maintenance.urls", namespace="cars")),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
