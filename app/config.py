# SQUIZZ Platform API Environment Variables

#Base URL for the website and calling api endpoints
BASE_URL = "https://api.squizz.com/rest/1"

#SQUIZZ UNI Melb organization ID. We need it to login to the SQUIZZ API and establish a connections
API_ORG_ID = "11EA64D91C6E8F70A23EB6800B5BCB6D"

#SQUIZZ UNI Melb organization password. We need it to login to the SQUIZZ API and establish a connection
API_ORG_PASSWORD = "Squizzunimelb!0"

#SQUIZZ UNI Melb organization key. Its needed when the session is being made with the SQUIZZ API
API_ORG_KEY = "3a62ea5aa2d8845a72dd030369dd571d5123567f70fa76b5bc3bcdf103e3307cc52b01030230c4f2807b44f88ce0052e91f3b7550341f38fe6544d02abfd7d87"

#The supplier organization ID. So far we have only organization, so we are doing it this way. If we need to have multiple organizations,
#it would be better to create a table in the database and retrieve from there.
SUPPLIER_ORG_ID = "11EAF2251136B090BB69B6800B5BCB6D"

# MySQL Environment Variables
HOST = "localhost"
USER = "root"
PASSWORD = "squizz"
DB_NAME = "squizz_app"