from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model

User =get_user_model()

def search(request):
	return render(request, "search.html")

def get_search(request):
	data= {}
	input = request.GET.get("input")
	if input == '':
		data['is_exists'] = False
		return JsonResponse(data)
	users = User.objects.filter(username__contains=input)
	if users.exists():
		data['is_exists'] = True
		data['html_value'] = render_to_string("includes/users.html",{'users':users})

	else:
		data['is_exists'] = False

	return JsonResponse(data)
	