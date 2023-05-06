# Casting Agency API
This project can store movies and actor details. it Provides REST based API endpoints to manage Actor and Movies. It can perfrom CRUD operations on Actor and Movie

## Project Dependencies
The project depends upon the following environment variable
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


# Sample Bearer Token for Reviewer
* Role Casting Assistant : ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFJRzRJV0lsZHpaU1Z6WEMza1lQdSJ9.eyJpc3MiOiJodHRwczovL2Rldi1obGh6MWxqMGVka3Q4ejMzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDUxMjJmMTlhYmQwMzg2NGJmZTA3MjgiLCJhdWQiOlsiQ2FwZXN0b25lRmluYWwiLCJodHRwczovL2Rldi1obGh6MWxqMGVka3Q4ejMzLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2ODMzNzk4MjksImV4cCI6MTY4MzQ2NjIyOSwiYXpwIjoiSUFpUVhKRTkyeUhvREJmRUFZTlJJNlNqcW1qZDhJNGwiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIGFkZHJlc3MgcGhvbmUiLCJndHkiOiJwYXNzd29yZCIsInBlcm1pc3Npb25zIjpbInJlYWQ6YWN0b3IiLCJyZWFkOm1vdmllIl19.QTLcMOwpyQ92xvqEy2_OwZ3rX_cQ3BsmxMWY3vSPukR-rjUXefoWfF-QaXfLOhix9xVVqd2Lj1a6U8Ey70zHfGDrtfqeKs3xYR5TwkTGKh__ia1G8irLxbfDyWpym8C72mibnMHTuZHSR1mCQbiLYIvUq7NiiErAh8SgCxnDhuy-_Q3zTegTaXqnTsF-m2ofcYSWuqvpHL5Q8YcTJ-xORoxSBPQSSeuoY3sNZunz09zGfnYGjTdASMPszTRh3ZshUvEwnEj2wXGWzJlBRq8zcHMgDoYK_e4AfZxyxpA91JAeuy3uPWFnrbvS3D67xKimwzWhyfi1DDQuQOPxaayabA```
* Role Casting Director : ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFJRzRJV0lsZHpaU1Z6WEMza1lQdSJ9.eyJpc3MiOiJodHRwczovL2Rldi1obGh6MWxqMGVka3Q4ejMzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDUwZjcwNzQ0YTljMmYzNTQyM2M0MmQiLCJhdWQiOlsiQ2FwZXN0b25lRmluYWwiLCJodHRwczovL2Rldi1obGh6MWxqMGVka3Q4ejMzLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2ODMzNzk4MzAsImV4cCI6MTY4MzQ2NjIzMCwiYXpwIjoiSUFpUVhKRTkyeUhvREJmRUFZTlJJNlNqcW1qZDhJNGwiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIGFkZHJlc3MgcGhvbmUiLCJndHkiOiJwYXNzd29yZCIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImRlbGV0ZTphY3RvciIsImVkaXQ6YWN0b3IiLCJlZGl0Om1vdmllIiwicmVhZDphY3RvciIsInJlYWQ6bW92aWUiXX0.CGangZlr5r1lxjxBZ3WTp7l-j08b4f7Ge3M3gUFS2-gkXJTE5w6dDVrC1R7pPhAbnwGfB21tu0JPcg_nHg6om8I_3HCdWbJVxEooOcC6PNAfhryfspGQsJytSaREIy4WpViroF3DiTPP5qel8P5noPjo7Y5pbX3Nol8X67QI9xOvuY5Y7h_rPLX5J8yySnjaUjKZEL9nPjXwQ_6TWqOkCm7dNl_1qocukzjzpwBPCDrx6KFTkNo2kcgA8KQWVEqt2r5Gfh68b-PX6wbZyEWg23mPf-YW2k3BJ3LpFLtRDccXqu8yznfjMBtg2FU9RKnVeOGkB_ubBGjP5NdehPrYzA```
* Role Executive Producer : ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFJRzRJV0lsZHpaU1Z6WEMza1lQdSJ9.eyJpc3MiOiJodHRwczovL2Rldi1obGh6MWxqMGVka3Q4ejMzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDUxMjMxZTQ0YTljMmYzNTQyM2NiNDMiLCJhdWQiOlsiQ2FwZXN0b25lRmluYWwiLCJodHRwczovL2Rldi1obGh6MWxqMGVka3Q4ejMzLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2ODMzNzk4MzEsImV4cCI6MTY4MzQ2NjIzMSwiYXpwIjoiSUFpUVhKRTkyeUhvREJmRUFZTlJJNlNqcW1qZDhJNGwiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIGFkZHJlc3MgcGhvbmUiLCJndHkiOiJwYXNzd29yZCIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImFkZDptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImVkaXQ6YWN0b3IiLCJlZGl0Om1vdmllIiwicmVhZDphY3RvciIsInJlYWQ6bW92aWUiXX0.UxVsDk05sAtWYJcBegxgby9FreZrNJ2TzDxMlEBx2qRdmFwsi0m50NlPAPqh4pnwQ401aupdJrAB3zY9FMFcpCRNuGl1b6EW2rfwH9h3uNjlKhTp6OkeIRCZIum8KPLuVtl9TUufpOcpXW1Ck2RSThZqXFBOX9BNZpIfuqyEgePYIaa33WA1lPwrYL9kRu19YlT9N2KYSh084OyoieZTcrU43My6GOn1gfHqbRi-KZhmYacngHYnyVqCLVvUqjffQ1xw4_C_jDtBRTm7C3Edfqn_C4KWIKAuGJRc5WrgdK61WsVGVacbS_T7c-PGqBeGuKV4gxx56w_mcprPPPRIIA```

## Getting Started

* **Base URL:**  default, `httpp://127.0.0.1:5000/`
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
curl --location 'http://127.0.0.1:5000/movie/1' \
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
curl --location 'http://127.0.0.1:5000/movie' \
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
curl --location --request DELETE 'http://127.0.0.1:5000/movie/74' \
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
curl --location --request PATCH 'http://127.0.0.1:5000/movie/73' \
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
curl --location --request GET 'http://127.0.0.1:5000/actor/1' \
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
curl --location 'http://127.0.0.1:5000/actor' \
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
curl --location --request DELETE 'http://127.0.0.1:5000/actor/73' \
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
curl --location --request PATCH 'http://127.0.0.1:5000/actor/72' \
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