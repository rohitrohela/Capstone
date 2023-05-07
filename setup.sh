#!/bin/bash
export DATABASE_URL_PRD=postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/postgres
export DATABASE_URL_TEST=postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/postgres
export AUTH0_DOMAIN=dev-hlhz1lj0edkt8z33.us.auth0.com
export API_AUDIENCE=CapestoneFinal
export CLIENT_ID=IAiQXJE92yHoDBfEAYNRI6Sjqmjd8I4l
export CLIENT_SECRET=9g5mAujZiyuHj3bwgypkz9kwq3deNjbwhYmv_BovWIMKd75ONaCQWl_aOtVafJjk
export USERNAME_CASTINGASSISTANT=assistant@fsnd.com
export PASSWORD_CASTINGASSISTANT=Test@fsnd123
export USERNAME_CASTINGDIRECTOR=director@fsnd.com
export PASSWORD_CASTINGDIRECTOR=Test@fsnd123
export USERNAME_EXECUTIVEPRODUCER=producer@fsnd.com
export PASSWORD_EXECUTIVEPRODUCER=Test@fsnd123

echo "setup.sh script executed successfully!"