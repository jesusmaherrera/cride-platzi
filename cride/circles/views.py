"""CIrcles views. """

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Models
from cride.circles.models import Circle

@api_view(['GET'])
def list_circles(request):
    """List circles. """
    # import ipdb; ipdb.set_trace()
    circles = Circle.objects.all()
    public = circles.filter(is_public=True)
    data = []
    for circle in circles:
        data.append({
            'name': circle.name,
            'slug_name': circle.slug_name,
            'rides_offered': circle.rides_offered,
            'rides_taken': circle.rides_taken,
            'members_limit': circle.members_limit,
        })

    return Response(data)

@api_view(['POST'])
def create_circlce(request):
    """Create circle."""
    name = request.data['name']
    slug_name = request.data['slug_name']
    about = request.data.get('about', '')
    circle = Circle.objects.create(name=name, slug_name=slug_name, about=about)
    data =  {
        'name': circle.name,
        'slug_name': circle.slug_name,
        'rides_offered': circle.rides_offered,
        'rides_taken': circle.rides_taken,
        'members_limit': circle.members_limit,
    }
    return Response(data)