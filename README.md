# Clinical Trial Registry Template

## Running the app locally
1. Clone this repository

	```git clone https://github.com/parhsingh/clinical-trial-registry-template.git```

2. Setup and run a virtual environment (inside the cloned repository)

	```python3 -m venv venv```

	```venv\Scripts\activate```

3. Install Django

	```pip install django```
4. Install ```django_extensions```

	```pip install django_extensions```

5. Create and run migrations

	```python manage.py makemigrations```

	```python manage.py migrate```

6. Run the server

	```python manage.py runserver```

7. Open the app in your browser at http://localhost:8000/