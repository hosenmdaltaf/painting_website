from .models import Services

def get_services_to_context(request):
    all_services = Services.objects.all()
    return {
        'all_services': all_services
    }