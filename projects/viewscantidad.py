from django.http import JsonResponse
from django.views import View

from supabase_py import create_client, Client

# Configura tu URL y clave de Supabase
supabase_url = 'https://yorojvyqcvqcrdldenbr.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inlvcm9qdnlxY3ZxY3JkbGRlbmJyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTI3ODU1NTcsImV4cCI6MjAyODM2MTU1N30.icOBsA7CL5upAW1AbKUYgk4Tkb-cRKz0BvxB5lvCnOs'

# Crea un cliente de Supabase
supabase: Client = create_client(supabase_url, supabase_key)

class CantidadProductosView(View):
    def get(self, request, category_name):
        # Consulta todos los productos de la categoría especificada
        query = supabase.table("Productos").select("nombre", "cantidad").filter("categoria_id", 'eq', category_name)

        response = query.execute()
        print("Respuesta de Supabase:", response)

        if response['status_code'] == 200:
            if response['data']:
                # Construye un diccionario con el nombre de cada producto y su cantidad
                products_quantity = {product['nombre']: product['cantidad'] for product in response['data']}
                return JsonResponse({"productos_cantidad": products_quantity})
            else:
                return JsonResponse({"error": "No se encontraron productos en la categoría especificada."}, status=404)
        else:
            return JsonResponse({"error": "Ocurrió un error al consultar la base de datos de Supabase."}, status=500)

