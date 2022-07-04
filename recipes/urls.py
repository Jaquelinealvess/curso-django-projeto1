# from django.contrib import admin
from django.urls import path

from recipes.views import home

# dominio/recipes
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home),  # Home

]
