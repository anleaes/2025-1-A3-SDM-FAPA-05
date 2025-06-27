# from django.contrib import admin
# from django.urls import path, include
# from django.conf.urls.static import static
# from django.conf import settings



# urlpatterns = [
#    # path("", home, name="home"), 
#     path("admin/", admin.site.urls),
#     path('categorias/', include('categories.urls', namespace='categories')),    
#     path('impressoras/', include('printers.urls', namespace='printers') ),
#     path('documentos/', include('documents.urls', namespace='documents')), 
#     path('clientes/', include('clients.urls', namespace='clients')),
#     path('fornecedores/', include('fornecedores.urls', namespace='fornecedores')),
#     path('pedidos/', include('orders.urls', namespace='orders')),
#     path('itens_pedido/', include('orderitems.urls', namespace='orderitems')),

# ]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse

def home(request):
    html = """
    <h1>Bem-vindo ao Sistema!</h1>
    <p>Escolha uma das opções abaixo:</p>
    <ul>
        <li><a href="/admin/">Admin</a></li>
        <li><a href="/categorias/">Categorias</a></li>
        <li><a href="/impressoras/">Impressoras</a></li>
        <li><a href="/documentos/">Documentos</a></li>
        <li><a href="/clientes/">Clientes</a></li>
        <li><a href="/fornecedores/">Fornecedores</a></li>
        <li><a href="/pedidos/">Pedidos</a></li>
        <li><a href="/itens_pedido/">Itens do Pedido</a></li>
    </ul>
    """
    return HttpResponse(html)

urlpatterns = [
    path("", home, name="home"), 
    path("admin/", admin.site.urls),
    path('categorias/', include('categories.urls', namespace='categories')),    
    path('impressoras/', include('printers.urls', namespace='printers')),
    path('documentos/', include('documents.urls', namespace='documents')), 
    path('clientes/', include('clients.urls', namespace='clients')),
    path('fornecedores/', include('fornecedores.urls', namespace='fornecedores')),
    path('pedidos/', include('orders.urls', namespace='orders')),
    path('itens_pedido/', include('orderitems.urls', namespace='orderitems')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
