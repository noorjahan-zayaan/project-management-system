from django.shortcuts import render, redirect
from .models import User, Project, Task


# LOGIN
def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email, password=password)

            request.session['user_id'] = user.id
            request.session['role'] = user.role

            if user.role == 'admin':
                return redirect('admin_dashboard')
            else:
                return redirect('developer_dashboard')

        except:
            return render(request, 'login.html', {'error': 'Invalid login'})

    return render(request, 'login.html')


# LOGOUT
def logout_view(request):
    request.session.flush()
    return redirect('login')


# ADMIN
def admin_dashboard(request):

    if request.session.get('role') != 'admin':
        return redirect('login')

    projects = Project.objects.all()
    developers = User.objects.filter(role='developer')
    tasks = Task.objects.all()

    # ADD DEV
    if 'add_dev' in request.POST:
        User.objects.create(
            emp_id=request.POST['empid'],
            name=request.POST['name'],
            email=request.POST['email'],
            username=request.POST['username'],
            password=request.POST['password'],
            role='developer'
        )

    # ADD PROJECT
    if 'add_project' in request.POST:
        Project.objects.create(
            name=request.POST['pname'],
            description=request.POST['desc'],
            start_date=request.POST['start'],
            end_date=request.POST['end'],
            status=request.POST['status']
        )

    # ADD TASK
    if 'add_task' in request.POST:
        Task.objects.create(
            title=request.POST['title'],
            project_id=request.POST['project'],
            developer_id=request.POST['developer'],
            start_date=request.POST['start'],
            end_date=request.POST['end'],
            status=request.POST['status']
        )

    # DELETE TASK
    if 'delete_task' in request.POST:
        Task.objects.get(id=request.POST['task_id']).delete()

    # EDIT TASK
    if 'edit_task' in request.POST:
        t = Task.objects.get(id=request.POST['task_id'])
        t.title = request.POST['title']
        t.status = request.POST['status']
        t.save()

    return render(request, 'admin_dashboard.html', {
        'projects': projects,
        'developers': developers,
        'tasks': tasks
    })


# DEVELOPER
def developer_dashboard(request):

    if request.session.get('role') != 'developer':
        return redirect('login')

    user_id = request.session['user_id']
    tasks = Task.objects.filter(developer_id=user_id)

    # UPDATE STATUS
    if request.method == "POST":
        t = Task.objects.get(id=request.POST['task_id'])
        t.status = request.POST['status']
        t.save()



    return render(request, 'developer_dashboard.html', {
        'tasks': tasks
    })