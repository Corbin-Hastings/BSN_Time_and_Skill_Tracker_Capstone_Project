# BSN Time and Skill Tracker

The new Western Colorado University BSN program is seeking an application to effectively track student’s observed skills and hours requirements to keep them on track for graduation. 
The product is a fully functioning web application that provides a space for students and faculty to easily and securely track these skills and hours. 
The system also allows for easy viewing of skills via a QR scan.


## Installation

Install Django: https://docs.djangoproject.com/en/6.0/topics/install/#installing-official-release

```bash
py -m pip install Django
```

Install Django QR Code: https://pypi.org/project/django-qr-code/

```bash
pip install django-qr-code
```

Install Django Bootstrap: https://pypi.org/project/django-bootstrap-v5/

```bash
pip install django-bootstrap-v5
```

## Usage

```python
# move to BSNTracker folder

cd BSNTracker

# start server

py manage.py runserver

# returns development server

Starting development server at http://127.0.0.1:8000/
```

## General Django File Information and Descriptions
```
Helpful Guide to Django File Structure:
  https://medium.com/django-unleashed/django-project-structure-a-comprehensive-guide-4b2ddbf2b6b8

manage.py: used to manage and run the server.

settings.py: file containing downloaded apps, database, and other general server settings.

urls.py: contains URL patterns for the website.

models.py: contains the database structure.

views.py: contains the logic to bridge the model (database) and the template.

base.html: master template document used for inheritance.

admin.py: file to configure the built in django interface.

apps.py: configuration file for applications.

forms.py: file that handles user input (skills,hours,).
```

## Resources Used
```
Definitions:

Django: Python web framework used to develop this web application.

Bootstrap: Front-end framework used to style and standardize web pages.

PythonAnywhere: Web hosting service for Python code.
```
```
General:

https://docs.djangoproject.com/en/6.0/
```
```
Intro to Django:

https://docs.djangoproject.com/en/2.2/intro/tutorial01/#creating-a-project
```
```
QR-Code:

https://django-qr-code.readthedocs.io/latest/
```
```
Static Files:

https://docs.djangoproject.com/en/6.0/howto/static-files/
```
```
Admin Page:

https://docs.djangoproject.com/en/6.0/ref/contrib/admin/
```
```
Project Structure:

https://django-project-skeleton.readthedocs.io/en/latest/structure.html
```
```
Bootstrap:

https://getbootstrap.com/docs/4.1/getting-started/introduction/
```
```
PythonAnywhere:

https://help.pythonanywhere.com/pages/
```
## Authors and acknowledgment

Co-authored-by: Corbin Hastings

Co-authored-by: Izzy Coppola

Co-authored-by: Morgan May

