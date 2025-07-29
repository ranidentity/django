starting python virtual env
1. python -m venv myworld
2. mac
source myworld/bin/activate
2. window
myworld\Scripts\activate.bat
3. install django
python -m pip install Django
4. validate installation
django-admin --version
5. create a django project
django-admin startproject <project-name>
6. create app
python manage.py startapp <app-name>


to run
python manage.py runserver


to clone
python -m venv env
activate
pip install -r requirements.txt