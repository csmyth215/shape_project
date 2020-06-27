## Practice Django project (shape metric calculator)

Simple app to experiment with Python classes, user input, Django forms and templates, and static files.

<p align="middle">
    <image src="img/user_input.png" width="40%">
    <image src="img/output.png" width="40.9%">
</p>



  
### Running locally
Create and activate a virtual env:
```
$ python -m venv venv
$ venv\Scripts\activate
```

Install dependencies from requirements.txt:
```
$ pip install -r requirements.txt
```

Set a secret key in measurement_calculator/settings.py
```
$ SECRET_KEY = '[my_chosen_key_here]'
```

Run the development server:  
```
$ python manage.py runserver
```

### Deploying on Heroku
This project contains a Procfile and is ready to run on Heroku.  Simply create your project and push to Heroku:
```
$ git push heroku master
```