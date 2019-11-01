Flying Monthy (flyingmonthy.com) a.k.a. Monthy Python like browsing memes
-
Meme webpage  
-
by meme_team  
Members:
- Łukasz Paciorek
- Adam Rogacewicz
- Mateusz Kluska
- Rafał Osowski
- Arkadiusz Tomalczyk

----------------
----------------
Main Features:  
-
- website similar to kwejk.pl or demotywatory.pl
- adding memes to website
- admin / moderator account
- comments (adding, editing)
- moderate contents by admin / moderator
- user can delete his meme
- users can delete their comments
- statistics / ratings for memes (+  -)
- user profile that shows what memes he posted
- creating accounts
- categories / tags

Extra Features: 
-
- account activation by email
- waiting room for memes (if meme gets n of + it gets on main page, if it gets n of - it is deleted)
- top memes subpage
- gif memes
- forgotten password restore
- censorship of profanities  
- watermark on pictures
- avatar
- side bar top users
- check password for complexity(8 letters, capital and lower  case letters, number, special characters)
- sorting comments and  and nested comments

----------------  
----------------
Modules
-

Registration / logging module
-
- register account
- registration form
- logging into webpage


User module  
-
- user must have:
    - nickname
    - password
    - OPTIONAL avatar
    - email
    - OPTIONAL list of friends (empty at initialization)
    - account creation date
    - name
    - surname
    - OPTIONAL localization
- user profile
    - check what memes he posted  

Memes module  
- 
- adding memes
    - meme must have:
        - id
        - name / title
        - date when it was added
        - tags / categories
        - statistics / ratings (+, -)
        - owner (foreign key in database)  

----------
Form of project:
- 
- Django templates
- full rest api endpoints (to download with json and test with postman)
- two views for urls

-------------
Technologies used:
- 
- Python 3.6
- Django 2.2
- Django bootstrap 11.0.0
- Django rest framework 3.10..3
- Django filter 2.2.0
- Dtabase on sqlite3 (later will probably be changed on postgresa)  

Configuration before first run:
- 
- configurue virtual environment in Python:
    - virtualenv environment_name
    - install modules from requirements.txt (pip3 install -r requirements.txt)
- download master from repo
- django migrations(python3 manage.py makemigrations, python3 manage.py migrate)
- migrate static files(python3 manage.py collectstatic)
- run django server(python3 manage.py runserver)