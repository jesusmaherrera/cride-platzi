"""CIrcles views. """

# Django
from django.http import HttpResponse, JsonResponse

# Models
from cride.circles.models import Circle


def list_circles(request):
	"""List circles. """
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

	return JsonResponse(data, safe=False)