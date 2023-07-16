# Pythonista DRF API

The Pythonista DRF API is a back-end API created using Django Rest Framework that is create to serve the Pythonista React app. It handles all backend functionality including user Profiles, Posts, Comments, Likes, Events, Conversation on an event's post, Join, Following and Followers feature.

## Database Designs
The following Entity Relationship Diagram was created to show the models used. The in-built Django User model was used for this project, and the following custom models were created:

1. Profiles (Slightly customized from the Django standard User model)
2. Posts (Text-base post publishing )
3. Comments (To make comment on a post to interact in community)
4. Likes (Show intersting content)
5. Events (A post publicising a future event)
6. Conversations (All user discussions related an event while it's being promoted)
7. Join (To indicate if the user plans to attend the event)


    Note: I was planning to have a job feature in my app where users could post a job or apply for a job, and I created a data model for that. Unfortunately, due to some unexpected issues, I wasn't able to implement this feature. A clarification can be found at the end of the document.


### _Database Schema_

The relationships between all of these models is summarized in the followed entity relationship diagram:

![Database Schema](../pythonista_api/docs/images/DB%20schema.jpg)


## Technologies Used

**_Languages_**

Python - Provides the functionality for the DRF backend framework.

**_Frameworks, Libraries & Programs Used_**

1. **Django:** Django was used to create the web application

2. **Django Rest Framework:** The Django rest framework was used to simplify the process between the back and front ends.

3. **PostgreSQL:** PostgreSQL was used as the object-relational database system.

4. **ElephantSQL:** ElephantSQL was used to host the database.

5. **Cloudinary:** A service that hosts image files in the project.

6. **Git:** Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

7. **GitHub:** GitHub is used to store the projects code after being pushed from Git.

8. **PEP8 Validation:** pep8 is a tool to check your Python code against some of the style conventions in PEP 8.

9. **Heroku:** Heroku was used for the deployed application.

10.  **DrawSQLapp:** Development of database schema.
11. **Django CORS:** This Django app adds Cross-Origin-Resource Sharing (CORS) headers to responses, to enable the API to respond to requests from origins other than its own host.

12. **Django Filter:** The django-filter is used to implement ISO datetime filtering functionality.

13. **DRF Simplejwt:** Provides JSON web token authentication.
14. **dj-database-url:** Creates an environment variable to configure the connection to the database.

15. **dj-rest-auth:** Provides REST API endpoints for login and logout.


## Deployment

### _A. Set up JSON Web Tokens_

1. Install JSON Web Token authentication run terminal command `pip install dj-rest-auth`
2. Add `rest_framework.authtoken` and 'dj_rest_auth' to the list of INSTALLED_APPS in settings.py.
3. Add the dj-rest-auth urls paths to the main urls.py file.
```
urlpatterns = [
    
    ...
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    ]
```
4. Migrate the database with terminal command `python manage.py migrate`
5. For users to be able to register, install Django AllAuth with terminal command pip install `dj-rest-auth[with_social]`
6. Add the following INSTALLED_APPS to settings.py:
```
INSTALLED_APPS = [

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
]
```
7. Set `SITE_ID = 1` in settings.py.
8. Add the registration urls to the main urls.py file:
```
path(
    'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
),
```
9. To install the JSON tokens, run terminal command `pip install djangoframework-simplejwt`
10. Set `os.environ['DEV'] = '1'` in the env.py file.
11. This value can be used to check if project is in development or production. Add the following _if / else_  statement to settings.py:
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
}
```
12. To enable token authentication, set REST_USE_JWT to True. To ensure tokens are sent over HTTPS only, set JWT_AUTH_SECURE to True. Cookie names must also be declared. To do all of this, add the following code below the if/else statement just added to settings.py:

```
REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
```

13. Create serializers.py file in the _pythonista_api_ directory, and copy `UserDetailsSerializer` code from Django documentation as follows:

```
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """Serializer for Current User"""
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        """Meta class to to specify fields"""
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
```

14. Overwrite the default user detail serializer in settings.py.
```
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'pythonista_api.serializers.CurrentUserSerializer'
}
```

15. Migrate the database again with terminal command `python3 manage.py migrate`.
16. Update requirements.txt file with new dependencies by running terminal command `pip3 freeze > requirements.txt`.

----    

### _B. Prepare API for deployment to Heroku_

1. Create a views.py file in `pythonista_api` directory, it will create a welcome message view for API.
```
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to The Pythonista django-rest-freamwork API!"
    })
```

2. Import to the main urls.py file, and add to the top of the urlpatterns list.

```
from .views import root_route

urlpatterns = [
    path('', root_route),

    ...
]
```
3. Add the following to settings.py (inside REST_FRAMEWORK), to set up page pagination.

```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

4. Set the default renderer to JSON for the production environment in settings.py:

```
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
```

5. Add the following to settings.py (inside REST_FRAMEWORK, under DEFAULT_PAGINATION_CLASS), to set up DATETIME_FORMAT, :

```
'DATETIME_FORMAT': '%d %b %y',
```

6. Set DATETIME format to show how long ago a comment / conversation was created and updated. To do this, add the following code to any serializers.py files within comment apps:

```
from django.contrib.humanize.templatetags.humanize import naturaltime

created_on = serializers.SerializerMethodField()
updated_on = serializers.SerializerMethodField()

    def get_created_on(self, obj):
        """Method to display when comment/conversation was posted"""
        return naturaltime(obj.created_at)

    def get_updated_on(self, obj):
        """Method to display when comment/conversation was updated"""
        return naturaltime(obj.updated_at)

```

### _C. Create a Database_

These steps will create a PostgreSQL database:

1. Log in to ElephantSQL.com to access your dashboard.
2. Click `"Create New Instance"`.
3. Set up your plan.
4. Select `"Select Region"`.
5. Select a data center near you.
6. Then click `"Review"`.
7. Check your details are correct and then click `"Create instance"`.
8. Return to the ElephantSQL **dashboard** and click on the database instance .name for this project
9. In the URL section, click the copy icon to copy the database URL