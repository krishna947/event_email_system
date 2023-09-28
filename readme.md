# Event Email System


## How to setup the Project

Create virtual environment.

```bash
virtualenv venv
```

To Activate the virtual environment run the following command.

```bash
source venv/bin/activate
```

open the terminal run the following command to install all dependencies.

```bash
 pip install -r requirements.txt
```

Now, move to the django-project run the following command.

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Run the following command to run the project.

```bash
python3 manage.py runserver
```

To Deactivate the virtual environment run the following command.

```bash
deactivate
```

After doing the above step project will run but not the celery, RMQ. To run all the services I have dockerize the project
so that it will be easier to setup all the serivces.


## Dockerize setup
Move to the project folder and type the following command.

```bash
docker-compose up -d --build
```

Then, four container will be created,
1. web container
2. celery container
3. celery beat container
4. RabbitMQ container

Go inside the web container and type the following command.


```bash
docker exec -it <container_id> bash 
python manage.py runserver 0.0.0.0:8000
```
After running the above command you can access the project by http://localhost:8000
(Note: You will get the container id by running the **docker ps** command)


## API Details

Get Employee Details.

```bash
http://localhost:8000/api/employees/
```


Get Event Details.

```bash
http://localhost:8000/api/events/
```


Get Event Templates.

```bash
http://localhost:8000/api/event-templates/
```


Get Email Logs.

```bash
http://localhost:8000/api/email-logs/
```


Important:
The project will run but email functionality will not work. To work the email functionality you have give the gmail id 
and app password in the project settings file. Below I have mention the variable which you have assign you gmail id and app password.
```bash
EMAIL_HOST_USER = 'example@gmail.com'  # Your Gmail email address
EMAIL_HOST_PASSWORD = 'abcd efgh ijkl mnop'  # Your Gmail email password or an app-specific password
```