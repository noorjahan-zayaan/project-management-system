 Project Management System

A simple Project Management System built using Django and SQLite.

 Features

- Admin manages Developers, Projects, and Tasks
- Tasks assigned to specific Developers
- Developers can view only their tasks
- Role-based login system
- Clean pastel UI

 Tech Stack

Django | SQLite | HTML | CSS

 Usage

Admin creates and assigns tasks.
Developers log in to view their assigned tasks.

 Project Structure

project_management/
│
├── manage.py
│
├── project_management/
│   ├── _init_.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── app/
│   ├── migrations/
│   ├── _init_.py
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── templates/
│   ├── login.html
│   ├── admin_dashboard.html
│   ├── developer_dashboard.html
│
└── db.sqlite3

---

 Setup Instructions

1. Clone the repository:

git clone <your-repo-link>
cd project_management

2. Install dependencies:

pip install django

3. Apply migrations:

python manage.py makemigrations
python manage.py migrate

4. Run the server:

python manage.py runserver

5. Open in browser:

http://127.0.0.1:8000/

---

Login Details

Admin Login (default):

- Email: admin@gmail.com
- Password: admin123

Developer Login:

- Created by Admin from dashboard

---

 How It Works

- Admin logs in and creates Developers, Projects, and Tasks
- Each Task is linked to a Project and assigned to a Developer
- Developers log in and can only see their own tasks
- All updates made by Admin are reflected instantly
