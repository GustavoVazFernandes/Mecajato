from django.http import HttpResponseRedirect

class RedirectToHTTPSMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Defina as rotas que devem ser redirecionadas para HTTPS
        https_routes = ['/login', '/clientes']  # Adicione outras rotas conforme necessário

        # Se a rota atual estiver na lista de rotas HTTPS e não for segura, redirecione para HTTPS
        for route in https_routes:
            if request.path.startswith(route) and not request.is_secure():
                host = request.get_host().split(':')[0]  # Obtém o nome do host sem a porta
                new_url = f"https://{host}:8443{request.get_full_path()}"
                return HttpResponseRedirect(new_url)

        # Defina as rotas que devem ser redirecionadas para HTTP
        http_routes = ['/servicos']  # Adicione outras rotas conforme necessário

        # Se a rota atual estiver na lista de rotas HTTP e for segura, redirecione para HTTP
        for route in http_routes:
            if request.path.startswith(route) and request.is_secure():
                host = request.get_host().split(':')[0]
                new_url = f"http://{host}:8000{request.get_full_path()}"
                return HttpResponseRedirect(new_url)

        response = self.get_response(request)
        return response