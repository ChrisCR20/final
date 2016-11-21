from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.db.models import Q
from django.shortcuts import redirect
from django.template import RequestContext
from django.template.context_processors import csrf
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, render_to_response
from todo_list.models import tarea, proyecto

def main(request):
	if not request.user.is_staff:
		#return render_to_response(request, 'login.html')
		#status = 200
    	#return render_to_response(request, 'login.html')
		return render_to_response('login.html',request)

	# Numero de objetos
	nprojects = proyecto.objects.count()
	ntasks_todo = tarea.objects.filter(Q(user = request.user) | Q(user = None)).filter(finalization_date = None).count()
	ntasks_done = tarea.objects.filter(Q(user = request.user) | Q(user = None)).exclude(finalization_date = None).count()

	# Filtro de datos
	tasks_todo = tarea.objects.filter(Q(user = request.user) | Q(user = None)).filter(finalization_date = None).order_by("-priority", "difficulty", "creation_date")
	tasks_done = tarea.objects.filter(Q(user = request.user) | Q(user = None)).exclude(finalization_date = None).order_by("-finalization_date")
	projects = proyecto.objects.all().order_by("name")

	return render_to_response("index.html", dict(tasks_done = tasks_done, tasks_todo = tasks_todo, ntasks_todo = ntasks_todo, ntasks_done = ntasks_done, user = request.user, projects = projects, nprojects = nprojects))

def login(request):
	username = request.POST.get('username')
	password = request.POST.get('password')

	user = authenticate(username = username, password = password)

	if user is not None:
		auth_login(request, user)

	return main(request)

def logout(request):
	auth_logout(request)

	return main(request)

@staff_member_required
def set_done(request, pk):
	task = tarea.objects.get(pk = pk)
	task.set_done()
	task.save()

	return main(request)

@staff_member_required
def set_open(request, pk):
	task = tarea.objects.get(pk = pk)
	task.set_open()
	task.save()

	return main(request)

@staff_member_required
def drop(request, pk):
	task = tarea.objects.get(pk = pk)
	task.delete()

	return main(request)

@staff_member_required
def create_task(request):
	if request.method == 'POST':
		l_name = request.POST.get('name')
		l_priority = request.POST.get('priority')
		l_difficulty = request.POST.get('difficulty')
		l_project = request.POST.get('project')
		l_user = request.POST.get('user')

		if l_project != None:
			lo_project = proyecto.objects.get(pk = l_project)
			if l_user != None:
				lo_user = request.user
				l_task = tarea.objects.create(name = l_name, priority = l_priority, difficulty = l_difficulty, project = lo_project, user = lo_user)
			else:
				l_task = tarea.objects.create(name = l_name, priority = l_priority, difficulty = l_difficulty, project = lo_project)
		else:
			if l_user != None:
				lo_user = request.user
				l_task = tarea.objects.create(name = l_name, priority = l_priority, difficulty = l_difficulty, user = lo_user)
			else:
				l_task = tarea.objects.create(name = l_name, priority = l_priority, difficulty = l_difficulty)

	return main(request)

@staff_member_required
def create_project(request):
	if request.method == 'POST':
		l_name = request.POST.get('name')

		l_project = proyecto.objects.create(name = l_name)

	return main(request)
