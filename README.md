# Casting Agency API
This project can store movies and actor details. it Provides REST based API endpoints to manage Actor and Movies. It can perfrom CRUD operations on Actor and Movie

## Project Dependencies
* The Project required many packages to start like Flask, python-dateutil etc. All of these dependencies are mentioned
in the requirements.txt file.

* Python Version to use: 3.11

The project depends upon the following environment variable. all of these are given in the setup.sh file
* DATABASE_URL_PRD : the database URL for production
* DATABASE_URL_Test: the database URL for test database
* AUTH0_DOMAIN : Auth0 Domain name
* API_AUDIENCE : Api audience of your domain
* CLIENT_ID : Auth0 Client id
* CLIENT_SECRET : Auth0 Client Secret
* USERNAME_CASTINGASSISTANT : username of user having castingAssistant Role
* PASSWORD_CASTINGASSISTANT : passwrod of user having casting assistant Role
* USERNAME_CASTINGDIRECTOR : username of user having castingDirector Role
* PASSWORD_CASTINGDIRECTOR : password of user having castingDirector Role
* USERNAME_EXECUTIVEPRODUCER :username of user having executiveProducer Role
* PASSWORD_EXECUTIVEPRODUCER : password of user having executiveProducer Role

## Local Development, Installing Project dependencies and Hosting
1. Clone the project using git on your local drive.
2. Install Python version 3.11 and PIP if not installed.
3. Create virtual environment either using  or virtualenv.
   1. Windows : py -m venv <DIR>
   2. Unix : python3 -m venv <DIR>
4. Install the dependencies mentioned in the requirements.txt
   1. Windows :py -m pip install -r requirements.txt
   2. Unix : python3 -m pip install -r requirements.txt
5. Run the setup.sh file provided in Unix/Windows(Use Bash). This will set the environment variables for the current sessions.
   1. Make adjustment to your environment variable mentioned in the setup.sh file like
   database_url_prod etc
   2. source ./setup.sh
6. To run the application run command : python -m flask run

## set up an Authentication
This application use Auth0 for the authentication. Although environment variable required to run the app are provided in the setup.sh but you can 
set up your own Auth0 authentication to work with.
1. Create your auth0 Tenent
2. Create one Regular web application
3. Crate one API
4. Create 3 roles having the following permissions
   1. CastingAssistant : read:actor, read:movie
   2. CastingDirector : read:actor, delete:actor, edit:actor, edit:movie, read:actor, read:movie
   3. ExecutiveProducer : read:actor, delete:actor, edit:actor, edit:movie, read:actor, read:movie, add:movie, delete:movie
5. Set the appropriate value of the folloiwng environment variable in setup.sh
   1. AUTH0_DOMAIN
   2. API_AUDIENCE
   3. CLIENT_ID
   4. CLIENT_SECRET
6. Create 3 user having role of CastingAssistant, CastingDirector and ExecutiveProducer and set
their credentials  for the following env variable. these are used to run unit test
   1. USERNAME_CASTINGASSISTANT
   2. PASSWORD_CASTINGASSISTANT
   3. USERNAME_CASTINGDIRECTOR
   4. PASSWORD_CASTINGDIRECTOR
   5. USERNAME_EXECUTIVEPRODUCER
   6. PASSWORD_EXECUTIVEPRODUCER


## Run Unit Test
1. Execute the following command to run the unit test : python test_app.py

# Sample Bearer Token for Reviewer
* Role Casting Assistant : ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFJRzRJV0lsZHpaU1Z6WEMza1lQdSJ9.eyJpc3MiOiJodHRwczovL2Rldi1obGh6MWxqMGVka3Q4ejMzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDUxMjJmMTlhYmQwMzg2NGJmZTA3MjgiLCJhdWQiOlsiQ2FwZXN0b25lRmluYWwiLCJodHRwczovL2Rldi1obGh6MWxqMGVka3Q4ejMzLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2ODM0NTg3OTMsImV4cCI6MTY4MzU0NTE5MywiYXpwIjoiSUFpUVhKRTkyeUhvREJmRUFZTlJJNlNqcW1qZDhJNGwiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIGFkZHJlc3MgcGhvbmUiLCJndHkiOiJwYXNzd29yZCIsInBlcm1pc3Npb25zIjpbInJlYWQ6YWN0b3IiLCJyZWFkOm1vdmllIl19.hiYTczjQiFGoDT4KpASw_fS_U3hFJUMMQpHaX2D2A1ScH_m8IrRDB5MZH4GCISAi4V9amWBfbYtJPJPiEazFIC2kcWgJu-lZE79APFZj8rNbAhGDn8LSCxM3tbOW50PFSrKGPXd10NRgIzkOHHJUNGckTNhoyYzSeTfXvsLWo0-zMgo1nMzuPGAiSrh8_uwHyUa6jMqzWPvb8vfuiySUN8afRPSC64NCdewNs5UoPFA9TC0yzoK0hIdyTjo3aUra0Y_mXf5PcH7hb-JLsRstQOcnky00zFJACo4r5dAWSibnyKJhD1wc2QyAibVQGHdNLmaMIWwkPRpk0I62vOOhhA```
* Role Casting Director : ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFJRzRJV0lsZHpaU1Z6WEMza1lQdSJ9.eyJpc3MiOiJodHRwczovL2Rldi1obGh6MWxqMGVka3Q4ejMzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDUwZjcwNzQ0YTljMmYzNTQyM2M0MmQiLCJhdWQiOlsiQ2FwZXN0b25lRmluYWwiLCJodHRwczovL2Rldi1obGh6MWxqMGVka3Q4ejMzLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2ODM0NTg3OTQsImV4cCI6MTY4MzU0NTE5NCwiYXpwIjoiSUFpUVhKRTkyeUhvREJmRUFZTlJJNlNqcW1qZDhJNGwiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIGFkZHJlc3MgcGhvbmUiLCJndHkiOiJwYXNzd29yZCIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImRlbGV0ZTphY3RvciIsImVkaXQ6YWN0b3IiLCJlZGl0Om1vdmllIiwicmVhZDphY3RvciIsInJlYWQ6bW92aWUiXX0.eIEei20jTIEZCreCO676_iyJ4wwX-wIquMZna8yqFuxBtXqUpXOxeaDX5sR4hFAzeObDQZDIaKVom_0Z_HIbssSVswZcF-84b0ftjv7X9J5DH4pJ-egUTbqI3R0WEGy0S9OpxU9SheEKR71AEl-toT7m--_o7Kq--aKOYeUR0J_U0W-f4jnCJkpaRvNPlC8nd0fmo3YheDL-Zko7UrHp1jxXcwW2xJnQyHWg5AnvsLsDu43RfiD0NLZCF8p5utk0NEudELvyjfFkmIzczY16ODmWzXXWKUL6VNh4Prl1913hBt8eftBpEDHa9sye03VJK9LUgklxLgc8xCaQNdPtdg```
* Role Executive Producer : ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFJRzRJV0lsZHpaU1Z6WEMza1lQdSJ9.eyJpc3MiOiJodHRwczovL2Rldi1obGh6MWxqMGVka3Q4ejMzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDUxMjMxZTQ0YTljMmYzNTQyM2NiNDMiLCJhdWQiOlsiQ2FwZXN0b25lRmluYWwiLCJodHRwczovL2Rldi1obGh6MWxqMGVka3Q4ejMzLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2ODM0NTg3OTUsImV4cCI6MTY4MzU0NTE5NSwiYXpwIjoiSUFpUVhKRTkyeUhvREJmRUFZTlJJNlNqcW1qZDhJNGwiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIGFkZHJlc3MgcGhvbmUiLCJndHkiOiJwYXNzd29yZCIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImFkZDptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImVkaXQ6YWN0b3IiLCJlZGl0Om1vdmllIiwicmVhZDphY3RvciIsInJlYWQ6bW92aWUiXX0.b-q7eOb8HTu7R4JPnE5var8rRRS7wTK4c-wNMX5ij6MwBtUlbujHrCllHspgTqn8ZJmf3s-UqpZC_UFCfXK5Tn7OpNVuCtehXWPuVYIUWu8zFF_Oo6z6MhcxWfs1LxKPC-Xg4MORP5AU-9bMJRMD5OMhUR0kvN-76jsLjKfq9sAbrhFcCtwNDcm9lbmih0R0xRxSojXy2Iuhc-fW3J6mO1uXFP-41obmMbIGR1YuTP9-yRbvChXh4U7OLQq88DLxXhtUDfxSKtNJS08NMolJPDYg-CJL_3r8ERnOiOG2ha0CXxTgrsZ1Um6pFlNOc9-40Wwx7vfBTNo9jehtGSiKnA```

## Getting Started

* **Base URL:**  default, `https://capstone-d1ly.onrender.com/`
* **Authentication:** You need to provide Bearer token to access the application.

>## Error Handling
Errors are returned as JSON objects in the following format
<br />


```json
{ 
    "Success": false,
    "error": 400,
    "message": "bad request"
}
```


The API will return the following type of errors when requests fail
* **400:** Bad Request
* **404:** Resource Not Found
* **422:** Not Processable
* **500:** Internal Server Error

>## End Points
### `GET '/movie/{id}'`
* **General:** Return the detail of the movie having the supplied id.
* **Sample request :** 
```commandline
curl --location 'https://capstone-d1ly.onrender.com/movie/1' \
--header 'Authorization: Bearer YOUR_BEARER_TOKEN'
```
* **Sample Response**
```json
{
    "movie": {
        "id": 1,
      
        "release_date": "Thu, 12 Oct 2023 00:00:00 GMT",
        "title": "The Last Air Bender"
    },
    "success": true
}
```
---
### `POST '/movie'`
* **General:** Return newly created movie record id and success status.
* **Sample request :** 
```commandline
curl --location 'https://capstone-d1ly.onrender.com/movie' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_BEARER_TOKEN' \
--data '{
    "title": "Movie Title",
    "release_date": "23-08-2000"
}'
```

* **Sample Response**
```json
{
    "movie_id": 74,
    "success": true
}
```

---
### `DELETE '/movie/{id}'` : Delete a movie
* **General:** Return success value True or False.
* **Sample request :** 
```commandline
curl --location --request DELETE 'https://capstone-d1ly.onrender.com/movie/74' \
--header 'Authorization: Bearer YOUR_BEARER_TOKEN' \
--data ''
```
* **Sample Response**
```json
{
    "recordDeleted": 1,
    "success": true
}
```
---
### `PATCH '/movie/{id}'`: For patching already saved movie
* **General:** Return success value True or False.
* **Sample request :** 
```commandline
curl --location --request PATCH 'https://capstone-d1ly.onrender.com/movie/73' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_BEARER_TOKEN' \
--data '{
    "title": "Test Movie paching"
}'
```
* **Sample Response**
```json
{
    "recordUpdated": 1,
    "success": true
}
```
---

### `GET '/ACTOR/${id}'` : Get actor details by its id
* **Sample request :** 
```commandline
curl --location --request GET 'https://capstone-d1ly.onrender.com/actor/1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_BEARER_TOKEN' \
--data '{
    "title": "Test Movie paching"
}'
```
* **Sample Response**
```json
{
    "actor": {
        "age": 33,
        "gender": "Male",
        "id": 1,
        "name": "Rohit"
    },
    "success": true
}
```

### `POST '/actor'` Add new actor
* **General:** Return success value and newly created actor id
* **Sample request :** 
```commandline
curl --location 'https://capstone-d1ly.onrender.com/actor' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_BEARER_TOKEN' \
--data '{
    "name": "Test Actor",
    "age": "33",
    "gender": "Male"
}'
```
* **Sample Response :**
```json
{
    "actor_id": 73,
    "success": true
}
```
---
### `DELETE '/actor/{id}':` delete a actor
* **General:** Return success value true or false and no of record deleted
* **Sample request :** 
```commandline
curl --location --request DELETE 'https://capstone-d1ly.onrender.com/actor/73' \
--header 'Authorization: YOUR_BEARER_TOKEN' \
--data ''
```
* **Sample Response :** 
```json
{
    "recordDeleted": 1,
    "success": true
}
```
---
### `PATCH '/actor/{id}':` delete a actor
* **General:** Return success value true or false and no of record patched
* **Sample request :** 
```commandline
curl --location --request PATCH 'https://capstone-d1ly.onrender.com/actor/72' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_BEARER_TOKEN' \
--data '{
    "name": "Test NEW Actor"
}'
```
* **Sample Response :** 
```json
{
    "recordPatched": 1,
    "success": true
}
```