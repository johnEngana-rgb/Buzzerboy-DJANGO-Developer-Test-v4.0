# Seeded Users and Passwords

## User 1
- **Username:** john_doe
- **Email:** john.doe@example.com
- **Password:** P@$$w0rd

## User 2
- **Username:** jane_doe
- **Email:** jane.doe@example.com
- **Password:** P@$$w0rd

## User 3
- **Username:** system
- **Email:** system@example.com
- **Password:** P@$$w0rd

## Additional Information
- Each user has multiple profiles with different languages (English and French).
- The profiles are associated with the "HelloWorld Company".

STEPS FOR LOCAL SETUP(RUN IN COMMAND LINE):

1. git clone <repository_url>

2. Navigate to: cd Buzzerboy-DJANGO-Developer-Test-v4.0/submission-lab2.1/lab2

3. Activate env 
    Windows: venv\Scripts\activate
    Linux: source venv/bin/activate

4. pip install -r requirements.txt

5. python manage.py migrate

6. python manage.py createsuperuser

7. python manage.py seed_data



screenshots
404.html
![alt text](img/image-3.png)

about-us
![alt text](img/image-4.png)

base.html
![alt text](img/image-5.png)

index 1
![alt text](img/image.png)

index 2
![alt text](img/image-1.png)

creative-agency
![alt text](img/image-2.png)


french sample(img/about-us)
![alt text](img/image-6.png) ![alt text](img/image-7.png)

french sample(index.html)
![alt text](img/image-8.png) ![alt text](img/image-9.png)


sample seeded data:
![alt text](img/image-10.png)

sqlite3 db data:
![alt text](img/image-11.png)

