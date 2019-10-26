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
- sprawdzenie hasla pod wzgledem zlozonosci(8 liter duza malalitera cyfra znak specjalny)
- sortowanie komentarzy i zagniezdzone komentarze

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

Comments module
-
- content to create (not implemented yet)

Adding memes module
-
- content to create (not implemented yet 

Statistics / rating module
-
- content to create (not implemented yet

Categories module
-
- content to create (not implemented yet

----------------  
----------------
Frontend
- 
- content to create (not implemented yet


----------
##Ma być zrobione w formie:
- Django templatki
- obok zrobione pełne restowe api (do pobrania samym jsonem)
- Dwa widoki dwa urle