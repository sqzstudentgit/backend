import logging
from typing import Tuple
from werkzeug.security import generate_password_hash, check_password_hash
from .DatabaseBase import DatabaseBase

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class UserResource(DatabaseBase):
    """
    A subclass of DatabaseBase, responsible for handling database
    operations regarding users
    
    These operations include:
        - User authentication
        - User creation
    """

    def __init__(self):
        super().__init__()


    def validate_username_password(self, username: str, password: str) -> str:
        """
        Validates the user's identity by checking the username and password.
        If their username and password are correct, then returns the customer's
        organisation ID

        Args:
            username: username (taken from user input)
            password: password (taken from user input)
        """
        query = "SELECT OrganizationId, Password FROM users WHERE Username = %s"
        values = [username]
        try:
            result = self.run_query(query, values, False)
            if result:
                user = result[0]
                hashed_password = user['Password']
                if check_password_hash(hashed_password, password):
                    logger.info("Logged in successfully")
                    return user['OrganizationId']
                else:
                    logger.info("Incorrect username or password entered")
            else:
                logger.info(f"Could not find user '{username}'")


    def create_user(self, username: str, password: str, org_id: str):
        """
        Creates a new user in the database

        Args:
            username: username
            password: password (raw password string)
            org_id: SQUIZZ organisation ID
        """
        hashed_password = generate_password_hash(password)
        query = "INSERT INTO users(Username, Password, OrganizationId) VALUES (%s, %s, %s)"
        values = [username, hashed_password, org_id]
        try:
            self.run_query(query, values, True)
            logger.info(f"Successfully created new user '{username}' with organization ID '{org_id}'")
        except:
            logger.error(f"Could not insert a new record for user '{username}'")
