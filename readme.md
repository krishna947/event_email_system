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



## Dockerize setup
Move to the project folder and type the following command.

```bash
docker-compose up -d --build
```

Then, three container will be created, go inside the web container and type the following command.

```bash
docker exec -it <container_id> bash
python manage.py runserver 0.0.0.0:8000
```



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
