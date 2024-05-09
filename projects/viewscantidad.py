from django.http import JsonResponse
from django.views import View

from supabase_py import create_client, Client

# Configura tu URL y clave de Supabase
supabase_url = 'https://yorojvyqcvqcrdldenbr.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inlvcm9qdnlxY3ZxY3JkbGRlbmJyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTI3ODU1NTcsImV4cCI6MjAyODM2MTU1N30.icOBsA7CL5upAW1AbKUYgk4Tkb-cRKz0BvxB5lvCnOs'

# Crea un cliente de Supabase
supabase: Client = create_client(supabase_url, supabase_key)

class CantidadProductosView(View):
    def get(self, request, product_name):
        
        query = supabase.table("Productos").select("cantidad").filter("nombre", 'eq', product_name)

        response = query.execute()
        print("Respuesta de Supabase:", response)

        if response['status_code'] == 200:
            if response['data']:
                
                cantidad = response['data'][0]['cantidad']
                return JsonResponse({"cantidad_productos": cantidad})
            else:
                return JsonResponse({"error": "No se encontraron productos con el nombre especificado."}, status=404)
        else:
            return JsonResponse({"error": "Ocurrió un error al consultar la base de datos de Supabase."}, status=500)



