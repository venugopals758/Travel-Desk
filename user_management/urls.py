from django.urls import path,include
from . import views,login_views
urlpatterns=[

    path('', login_views.signin_with_google, name='signin_with_google'),
    path('', include('social_django.urls', namespace='social')),
    path('dashboard',  views.index, name='index'),
    path('after_signin_with_google', login_views.after_signin_with_google, name='after_signin_with_google'),
    path('error_page', login_views.error_page, name="error-page"),
]
