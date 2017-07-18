from django.http.response import JsonResponse
from django.contrib.contenttypes.models import ContentType


# Create your views here.
def get_objects(requqest, id):
    content_type = ContentType.objects.get(pk=id)

    return JsonResponse({'data': '{0}.{1}'.format(content_type.app_label, content_type.model)})
