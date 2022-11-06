from django.urls import path


urlpatterns = [
    path('css/', views.css, name='hello_css-css'),
    path('noCss/', views.noCss, name='hello_css-noCss')
]