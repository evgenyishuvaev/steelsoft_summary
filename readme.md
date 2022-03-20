## About
Forecast Weather - this is manager for forcaster and users. Forecast Weather make request to https://api.openweathermap.org/data/2.5/onecall and parse reponse
then return current weather in choosen city.

## Dependecy

- Django==4.0.3
- djangorestframework==3.13.1
- djoser==2.1.0
- environs==9.5.0

## Installation


1. Make dir for project, and change dir
```
    mkdir steelsoft
    cd steelsoft/forecast_weather
```

2. Now we need create virtual enviroment and activate it
```
    python3 -m venv env_steel
    source env_steel/bin/activate
```

3. Clone repository to your work dir, and change dir
```
    git clone git@github.com:evgenyishuvaev/steelsoft_summary.git
    cd steelsoft_summary
```

4. Install all requiremets for project from requirements.txt
```
    pip install -r requirements.txt
```
5. For start project we need migrate all migrations
```
    ./manage.py migrate
```
6. After migrations, load data from city.json, this add information to City table about cities like lat, lon, for request weather from openweathermap.org API
```
    ./manage.py loaddata city.json
```
7. Project has two .env files, that stored sensitive data like API_KEY for openweathermap.org API and SECRET_KEY from django project, we need to edit their

    1. weather/services/.env.example, add your API_KEY and rename file to .env
    ```
        API_KEY=<api_key for openweathermap.org>
        API_URL=https://api.openweathermap.org/data/2.5/onecall
    ```
    2. ./.env.example, add your SECRET_KEY and rename file to .env
    ```
        SECRET_KEY=<SECRET_KEY from project settings.py>
    ```
8. Now we can create superuser and run our web server.
```
    ./manage.py createsuperuser
    * process create superuser*

    ./managa.py runserver
```
This is all for run app for test. But if you need install app in server eou need also install nginx, gunicorn. And create systemd daemon.

## API Endpoints

* api/v1/weather - List(GET) or Create(POST) method, list can be filtered by query params "city_name".
    Create can use only Forcaster or Admin. List can be used everyone

* api/v1/weather/\<int:pk\> - Retrive(GET) method, return choosen record by `pk` - `id` in Weather model. Can be used everyone

* api/v1/weather/update\<int:pk\> - Update(PUT, PATCH), where `pk` is `id` in Weather model, can be update only by Owner or Admin

* api/v1/weather/delete/\<int:pk\> - Delete(DELETE), where `pk` is `id` in Weather model, can be deleted only by Owner or Admin

## Permissions

|     Role      | Create             | Read  | Update | Delete |
| ------------- |:------------------:|:-----:|:------:|:------:|
| Admin         |          +         |   +   |    +   |    +   |
| Forecaster    |          +         |   +   |   if owner  |    if owner   |
| Anonymous User|          -         |   +   |    -   |    -   |

Admin, Forcaster needed authenticate