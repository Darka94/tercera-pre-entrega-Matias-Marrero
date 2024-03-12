from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, DetailView
from .models import Categoria, Producto, Cliente
from django.shortcuts import redirect
from django.urls import reverse
from django.urls import reverse_lazy



#-------------------Funciones--------------------------#

def home(request):
    return render(request, "appWeb/home.html") 

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'appWeb/productos.html', {'productos': productos})
def categoria(request):
    categoria = Categoria.objects.all()
    return render(request, 'appWeb/categoria.html', {'categoria':categoria})
def cliente(request):
    cliente = Cliente.objects.all()
    return render(request, 'appWeb/cliente.html', {'cliente':cliente})


#--------------------Formularios de producto-----------------------#
# Vista para crear un producto
class ProductoCreate(CreateView):
    model = Producto
    fields = ["nombre", "precio", "imagen", "categoria"]
    success_url = reverse_lazy("productos")
    
    
# Vista para eliminar un producto
class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos')  # Redirige a la lista de productos
    template_name = 'appWeb/producto_confirmar_eliminar.html'  # Template para confirmar la eliminación

# Vista para buscar  productos

class ProductoList(ListView):
    model = Producto
    template_name = 'appWeb/producto_list.html'
    context_object_name = 'productos'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk:
            return Producto.objects.get(pk=pk)
        query = self.request.GET.get('q')
        if query:
            return Producto.objects.filter(nombre__icontains=query)
  #   return Producto.objects.all()

    
    
class DetalleProductoView(DetailView):
    model = Producto
    template_name = 'appWeb/detalle_producto.html'  # El nombre del template donde se muestran los detalles del producto
    context_object_name = 'producto'  # El nombre del objeto que se pasará al template


class ProductoList(ListView):
    model = Producto
    template_name = 'appWeb/producto_buscar.html'
    context_object_name = 'productos'
    
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        if query:
            productos = Producto.objects.filter(nombre__icontains=query)
            # Redirigir al resultado de la búsqueda
            return redirect(reverse('producto_list') + f'?q={query}')
        return super().get(request, *args, **kwargs)
    
#---------------------Formularios de Categorias--------------------#
class CategoriaCreate(CreateView):
    model = Categoria  # Define el modelo
    fields = ['nombre']  # Define los campos del formulario
    success_url = reverse_lazy("categoria")  # Define la URL de éxito después de crear una categoría
   

#-----------------------Formularios de Clientes----------------------------------------
        
class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nombre', 'email']
    success_url = reverse_lazy("cliente") 
    

