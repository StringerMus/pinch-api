# Pinch API

## Introduction

Pinch API serves as the backend for the Pinch app developed using Django Rest Framework. Pinch is a website is a host that allows users to list items they have available for others to borrow, interested users can search for items they need to contact the owner to arrange fees, duration of rent and pick-up/drop-off.

It solves the problem of not having to purchase expensive items, only needed for one-time use or items that are even difficult to acquire or store as after use borrowers give the item back and a fraction of a fee can be charged instead of paying full price.

API allows to hold certain data and functionality for the front-end, developed on ReactJS, to allow users to create and view profiles and posts listings, comments, likes, have edit and delete functions to make the service possible for users.

[Visit the deployed API here](https://pinch-api-f947cf5f7bdc.herokuapp.com/)<br/>
[Visit the deployed website here](https://pinch-5e6e24dd12fc.herokuapp.com/)

## API Objective
* Act as a backend to the front-end ReactJS Pinch app.
* Hold data for users to create profiles and posts, like and comment.
* Allow users to create profiles by registering a profile.
* Allows signed in user to post, like posts and comment on posts.
* Allows users, where appropriate, to perform CRUD functionality.

# UX - User Experience
* Strategy Plane
* Scope Plane
* Structure Plane
* Skeleton Plane
* Surface Plane

# Strategy Plane
A plan is needed to ensure the purpose of the website meets the needs of site users, the audience, and the site owner.

## Target Audience
The target audience can be a variety of people depending on the item they need but the age ranges will be;
* 18 - 40 year olds

And sub-categories;
* University students on limited budgets
* Homeowners to maintain their homes where one-time purchases for DIY may be a problem
* People planning events - Need extra tables, chairs, item/ clothing for weddings etc. 

## User Stories
[Link to User Stories](https://github.com/users/StringerMus/projects/7/views/1)

#### Must haves
* A user can update account details
* A user can see a list of the most popular items.
* A logged in user can create a listing to share item listing with other users.
* A user can view a navbar from every page to navigate easily between pages.
* A user can create a new account to access all the features for signed up users.
* A user can sign in to the app to access functionality for logged in users.

#### Should haves
* A user can search for items with keywords.
* A logged in user can add comments to an item.
* A user can keep scrolling through listings on the site, that are loaded automatically without pagination.
* A user can view other users profiles to see their item listings and their information.
* A user can click a listing to view more details of an item.
* A user can view other user's profile pictures.
* A user can view their logged in status.
* A logged in user can edit their profile to change their profile picture.
* A logged in user can like a post.

# Scope Plane - FRONT END
I identified 5 main pages that would be needed for the website to be able to function as required;

#### Items listings/ home page.
* This page will contain a list of items posted by users.
* Users can browse all items available.
* A search bar will be available for users to search for items based on name, category, location and owner.
* A section of the page will show popular items on the site, popular by likes.
* Logged in users can like posts.

#### Create a listing page
* A form for logged in users post a new item listing.
* Users can fill in information item information and upload an image.

#### Post page
* A page for each item listing for their details can be viewed.
* Logged in users can comment and like posts.
* Item owners can delete or edit post details.

#### Liked page
* Only available for logged in users.
* The page will only show items liked by an owner.

#### Profile page
* Users can view profile details.
* Amount of item listing and list of posts by profile owner.
* Profile owners can edit their user information.

#### Login/ register page
* Sign up page for new users to register
* Login page for existing users to login

# Structure Plane
For the website to be able to fulfil its goal of creating profiles, listing and viewing items, liking and commenting on posts;
* Profiles
* Posts
* Likes
* Comments

![db_flowchart](media/structure_pl/database_flowchart.JPG)

## Features
I have used the development browser to show and test the API functionality as the deployed API does not have the ability to demonstrate CRUD functionality as this would be for the front-end to utilise.

![api_home](media/features/home.JPG)

## Navigation
Navigation around the API is performed via url input, these pages are the following below;

## Login/ logout
There is login/ logout functionality, I will be logged in as admin user 'spock' for the walkthrough.

![api_login](media/features/login.JPG)

## Admin Page - /admin
The admin page gives superuser's/ admin backend admin access to view, create, delete data. In this case it will be pages for the profile, post, comment, and like models.

The development browser stores local data, the data that will be shown in the screenshots will be the testing data and from the deployed API. 

![api_admin](media/features/admin.JPG)

## Profiles
The profile list shows the current list of users created either as a superuser or admin. 

![api_profile](media/features/profile.JPG)

## Posts
The post list shows all posts created by all users and the details recorded for each post including the link to the image in cloudinary, the amount of likes and comments associated with the post.

It also shows the number of posts and if there are next or prev pages to navigate to.

![api_post](media/features/post.JPG)

#### Detail
It is possible to just look at individual posts by adding the post id to the url,

![api_post3](media/features/post3.JPG)

#### Form
There is a form at the bottom of the page to be able to post a new listing. Once this is filled and submitted, the post will appear in the post list above.

![api_post2](media/features/post2.JPG)

## Like
The like list shows the recorded likes on the API related and which post the like is linked to via post id, the owner of the like, the date created and gives each like an id.

The front-end will use this to allow users to like posts which is possible by recording the like data.

There is a form underneath which allows to add likes to a post by the user.

![api_like](media/features/like.JPG)
![api_like2](media/features/like2.JPG)

## Comments
The comments list shows a list of comments associated to posts. A comment id is created and it records the owner, owner profile id, owner profile image, created at, updated at, post id and the comment made.
Individual comments can also be looked at on the Comments Detail page.

There is a form at the bottom of these pages which allows you to add a comment to a chosen post.

![api_comments](media/features/comments.JPG)
![api_comments2](media/features/comments2.JPG)

## Pagination
When the list becomes long the page additional pages are created instead of added to a long list.

![api_page](media/features/page.JPG)

# Defensive Design

### Permissions
Permission classes have been added to views in detail and list to ensure the owners of profiles, posts, likes and comments will have edit and delete access otherwise it is read-only.

### 404 Page
The 404 page not found appears on the backend if an invalid url is input or reached, however on the fron-end a customer 404 page has been created to allow users to navigate back.

# Future Enhancement
There are a couple of things I would have liked to add if there was additional time;

* Saved items - Give users the ability save items they are interested in so it can be recorded as a list to refer back to when needed, at the moment users can use the liked page to be able to access items they are interested in to refer back to.
* Email request - Allow users to put in a request to borrow via a button on a post. This will prompt a form for requestees to fill out important information like date of pickup, number of days and contact email.
* A calendar - This can show interested users the days the item is available to rent to ensure items aren't being requested whilst they are unavailable.

# Testing

### Profiles
* Expected – Create a new profile user with username and password. If image field is blank the default image is used instead.
* Testing – Tested through admin access > profiles > add profile. A new user was created filling in username, password field and confirming password.
No profile image was uploaded, the default profile image was provided instead from cloudinary.
* Result – The user was created as expected. Sign-in was successful using the new user details, the new profile appears in the profile list with an id, the username as owner, date created and updated, the profile image and the profile detail can be viewed with the id in the url. The profiles 'name' and 'about' can be updated on post details and a profile image uploaded. Unable to edit profiles that do not belong to the user.

### Posts
* Expected - Create a new post by filling in the post form as the new user. Item name, location and contact email is required. Price value cannot be below ‘0’ and has to be a number value not less than 3 decimal places. If an image is not provided a default image is provided.
* Testing – The post form was tested by filling in the post form, submitting the form with invalid details and then submitting it with the correct details. 
* Result – The post was created as expected. Does not allow a blank form to be submitted, need the item name, location and email address in the correct format or price field to less than 0, more than 2 decimal places and needs to be a number value. If an image is not provided a default image is provided and does not allow images larger than 2 MB.
The post appears in the post list, with all the details provided in the form and the fields can be edited in post details and the post can be deleted. Unable to edit or delete posts that do not belong to the user.

### Comments
* Expected – Add a comment on the selected post, filling in the comment form, select a post and type the comment in the content. The comment should be assigned to a post with owner details and comment details.
* Testing – This has been tested by completing the form and submitting it.
* Result – Comment was created as expected. The comment appears on the comment list with the owner details, created/ updated information, post id and content of the comment. The comment can also be edited by the comment owner and submitted successfully and deleted. Unable to edit or delete comments that do not belong to the user.

### Likes
* Expected – To be able to add a like to a post. The like should record the owner of the like and the post the like belongs to.
* Testing – This will be tested by submitting a like form against a post.
* Result – The like has been submitted successfully. The like appears in the like listing and details with the id, created at, owner and the post the like belongs to.

### Pagination
* Expected - Lists should paginate after a list exceeds 10 entries.
* Testing - Create more than 10 posts to ensure the list paginates.
* Result - The post lists paginates. After creating 16 posts, a second page is created containing 6 posts and page 1 contains 10 posts.

## Bugs and Fixes
* Bug - Posts, comments and likes links were not appearing in the admin url of api.
* Fix - Add these models in their respective admin files. 
<hr>

* Bug - Unable to login into front end due to a newer version of django rest auth being used. 
* Fix - Update JWT REST_AUTH in settings.py for JWT to work for the new django version.
<hr>

* Bug - Post model accepted negative figures for 
* Fix - Add min value in price field.
<hr>

Bug - Liked page was not filtering liked posts by users.
Fix - Created a query set is post views to create the filter.

## Validator
All code has been put through the Python Linter Validator, all code satisfies the validator apart from the code in AUTH_PASSWORD_VALIDATOR.

![api_validator](media/validator/validator.JPG)

Unable to break the line of code.

![api_settings_val](media/validator/settings_val.JPG)

# Deployment
To prepare the API ready for deployment these are the following steps that were taken;

## Set up JWT
### DJ_Rest_Auth
* Install Django Rest Auth.
* Add 'rest_framework.authtoken' and 'dj_rest_auth' in settings.py under INSTALLED_APPS. 
* Add 'dj-rest-auth/' to the main urls.py.

### Migrate Database
* Ensure the API database is up-to-date with the command 'python manage.py migrate' in the database.

### Registration
The app needs to allow to register
* Install django all auth.
* Add the following to the apps in settings.py under INSTALLED_APPS - 'django.contrib.sites', 'allauth', 'allauth.account', 'allauth.socialaccount', 'allauth.socialaccount.providers.facebook', 'dj_rest_auth.registration'.
* In settings.py add 'SITE_ID = 1'
* Add 'dj-rest-auth/registration/' to the main urls.py

### JWT Tokens
* Install 'djangorestframework-simplejwt'.
* Set DEV = 1 in env file.
* Add the REST_FRAMEWORK and REST_AUTH code you can see in the settings.py.

### Request User details
* Create serializers.py in pinch_api folder.
* Create class for CurrentUserSerializer for front-end to request for profile id and profile image.
* Run migrations to finish setting JWT for the app.
* Update requirement.txt file.
* Push all commits.

## Heroku Deployment
* Create a PostgreSQL from Code Institute
* Create a new app in Heroku, giving the app a relevant unique name and the suitable region.
* Within the Heroku settings of the created app add DATABASE_URL with the created postgres url in Config Vars.

### Prepate API in IDE
* In the IDE install dj_database_url and psycopg2 to connect the external database.
* In settings.py file, import dj_database_url.
* Update DATABASES in the setting.py to what it is current in the current settings for DATABASES.
* In env.py add a new environment variable with DATABASE_URL key with the PostgreSQL value.
* Comment out DEV environment in env to migrate the database models to the new database.
* Install gunicorn django-cors-headers in IDE terminal and update requirements.txt.
* Create a Procfile with the release: and web: commands inside the file and save.
* In settings.py file update ALLOWED_HOSTS variable to include Heroku app’s URL.
* Add corsheaders to INSTALLED_APPS and corsheaders middleware to the top of the MIDDLEWARE.
* Set the ALLOWED_ORIGINS for CLIENT_ORIGIN, CLIENT_ORIGIN_DEV, CORS_ALLOW_CREDENTIALS and CORS_ALLOWED_ORIGINS  you can see in the settings.py.
* Ensure the secret key is in not in settings.py but in the env.py file with a key that was not used in seytings.
* Set the DEBUG value to be True only if the DEV environment variable exists and Comment DEV back in env.py.
* Ensure requirements.txt file is up to date and git push code to repository.

### Heroku
* Add SECRET_KEY and CLOUDINARY_URL to Heroku APP Config Vars.
* Within Deploy tab select Connect to GitHub, search and connect API repo and deploy branch.

# Technologies Used
### Languages
* Python

### Tools
* Django - Framework to develop the API
* Cloudinary - Image database
* GitHub - Repository for the website and project board for User Stories
* GitPod - IDE used to create API
* Heroku - Deploy website
* CI Database - PostgreSQL database
* lucid.app - Create database model
* Django Rest Auth - Handle user authentication in Django applications
* Cors Headers - Handle permissions for web applications
* CI Python Linter - Used to check for error is python code

# Credit

* [Moneyfield](https://www.tutorialspoint.com/how-to-add-a-money-field-in-django)
* [Decimalfield](https://stackoverflow.com/questions/1139393/what-is-the-best-django-model-field-to-use-to-represent-a-us-dollar-amount)
* [EmailField](https://www.geeksforgeeks.org/emailfield-django-models/)
* [Disallow Negative Values](https://stackoverflow.com/questions/12384460/allow-only-positive-decimal-numbers)
* CI Moments walkthrough

### Media
* CI Moments Walkthrough - Default profile picture and default image picture

### Troubleshooting
* [ChatGPT](https://openai.com/index/chatgpt/)
* [Slack Code Institute Community](https://app.slack.com/client/T0L30B202/C026PTF46F5)
* [Stackoverflow](https://stackoverflow.com/)
* CI Tutor Support

### Honourable mentions
* I would like to give my mentor Richards Wells a big thanks with all the time given to help make the project better with feedback, inspiration and helpful solutions to my problems.
* Thanks to the Slack Community as the members who have been kind enough to help provide solutions to my queries.
* Thanks to Code Institute Tutors who were able to provide quick solutions to the bugs I was facing while in development.


[Link to App repository](https://github.com/StringerMus/pinch-app)