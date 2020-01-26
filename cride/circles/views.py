"""Circles views."""

# python
import csv

# Django
from django.http import JsonResponse

# models
from cride.circles.models import Circle

def list_circles(request):
	"""List circles."""
	circles =  Circle.objects.all()
	public = circles.filter(is_public=True)
	data = []
	for circle in public:
		data.append({
			'name': circle.name,
			'slug_name': circle.slug_name,
			'is_public': circle.is_public,
			'verified': circle.is_verified,
			'is_limited': circle.is_limited,
			'members_limit': circle.members_limit,
		})
	return JsonResponse(data, safe=False)

def import_circles(request):
	"""import circles from a csv file."""
	with open('./circles.csv') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		for row in csv_reader:
			name = row['name']
			slug_name = row['slug_name']
			is_public = row['is_public']
			verified = row['verified']
			members_limit = row['members_limit']
			is_limited = int(members_limit) > 0

			Circle.objects.create(
				name=name,
				slug_name=slug_name,
				is_public=is_public,
				is_verified=verified,
				is_limited=is_limited,
				members_limit=members_limit,
			)

	return JsonResponse({})