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



