from django.shortcuts import render

# Create your views here.
def inicio(request):

	a = 5
	b = 5
	c = a + b

	context = {
		"suma": c,
 }
	return render(request, "inicio.html", context)