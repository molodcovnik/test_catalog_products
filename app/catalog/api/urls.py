from django.urls import include, path

urlpatterns = [
    path('v1/catalog/', include('catalog.api.v1.urls')),
]