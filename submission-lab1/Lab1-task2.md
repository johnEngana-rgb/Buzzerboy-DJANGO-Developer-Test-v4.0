
running at 123.0.0.1:8000 (Local Host)
![alt text](/Images/L1_T2img1.png)

files are located at

GITHUB repo: https://github.com/johnEngana-rgb/Buzzerboy-DJANGO-Developer-Test-v4.0.git

DJANGO starter kit is inside App folder

![alt text](/Images/L1_T2img2.png)


The following screenshots are features of the starter kit!

Login Page:
![alt text](/Images/image.png)

DashBoard:
![alt text](/Images/image-1.png)

Users page:
![alt text](/Images/image-2.png)

Users Page(Add User)
![alt text](/Images/image-4.png)

Permissions Page:
![alt text](/Images/image-6.png)

Permissions Page(Add permission):
![alt text](/Images/image-5.png)


APP SETUP:
- Create virtual env in project folder (python -m venv env)
- Activate env command
    Windows: .\env\Scripts\activate
    Linux: source env/bin/activate
- run: pip install -r requirements.txt
- Setup DB
    $ python manage.py makemigrations
    $ python manage.py migrate
- Create Super User
    $ python manage.py createsuperuser
- Start the app
    $ python manage.py runserver
