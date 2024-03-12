from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('productos/', productos, name="productos"),
    path('cliente/', cliente, name="cliente"),
    path('cliente_form/', ClienteCreate.as_view(), name='cliente_form'),
    path('producto_form/', ProductoCreate.as_view(), name='producto_form'),
    path('producto/<int:pk>/eliminar/', ProductoDelete.as_view(), name='producto_eliminar'),
    path('producto/<int:pk>/', DetalleProductoView.as_view(), name='detalle_producto'),
    path('producto_list/', ProductoList.as_view(), name='producto_list'),
    path('categoria/', categoria, name="categoria"),
    path('categoria_form/', CategoriaCreate.as_view(), name='categoria_form'),



]
# Configuración para archivos multimedia
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
