from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from .models import ModulesInfo
from .forms import OpleidingSelect


def index(request):
	form = 'main/info_folder.html'
	now = datetime.now()
	opleidingen = []
	modulesinfo = ModulesInfo.objects.filter(id_module='webklas')
	for i in modulesinfo:
		opleidingen.append(i.opleiding)

	form_opleidingselect = OpleidingSelect(request.POST)

	if request.method == "POST":
		data_request = request.POST
		if request.POST.get('opleiding_selected'):
			opleiding_selected = request.POST['opleiding_selected']

		opleiding_modules = ModulesInfo.objects.filter(opleiding=opleiding_selected)

		response = {'opleidingen':opleidingen, 'form_opleidingselect':form_opleidingselect,'data_request':data_request,
			'opleiding_selected':opleiding_selected, 'opleiding_modules':opleiding_modules,'now':now ,
			}
		return render(request, form, response)

	else:
		response = {'opleidingen':opleidingen, 'form_opleidingselect':form_opleidingselect, 'opleiding_selected':'None'
			}
		return render(request, form, response)

	# return HttpResponse("Hello, world. You're at the hookers.")