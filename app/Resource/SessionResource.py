import datetime
import logging
from .DatabaseBase import DatabaseBase

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class SessionResource(DatabaseBase):
    """
    A subclass of DatabaseBase, responsible for handling database
    operations regarding sessions
    
    These operations include:
        - Session storage
        - Session validation
        - Session deletion
    """

    def __init__(self):
        super().__init__()


    def store_session(self, username: str, session_id: str, org_id: str):
        """
        Inserts a new session record within the database

        Args:
            username: username
            session_id: a SQUIZZ session ID string
            org_id: the organisation ID of the user
        """
        # Retrieve user ID for current user from database
        userId = None
        query = "SELECT Id from users WHERE Username = %s"
        values = [username]
        try:
            result = self.run_query(query, values, False)
            if result:
                userId = result[0]['Id']

        # Insert new session record in 'sessions' table
        query = "INSERT INTO sessions(SessionKey, DateTime, UserId, OrganizationId) VALUES (%s, %s, %s, %s)"
        values = [
            session_id,
            datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S"),
            userId,
            org_id
        ]
        try:
            self.run_query(query, values, True)
        except:
            logger.error("Could not store session in database")


    def validate_session(self, session_id: str, org_id: str):
        """
        This method validates whether session_id exists already in the database

        Args:
            session_id: a SQUIZZ session ID string
            org_id: the organisation ID of the user
        """
        query = "SELECT count(*) as num FROM sessions WHERE SessionKey = %s and OrganizationId = %s"
        values = [session_id, org_id]
        result = self.run_query(query, values, False)
        if result and result[0]['num'] > 0:
            return True
        else:
            logger.info("Could not find an existing session for the given user")
            return False


    def delete_session(self, session_id: str):
        """
        Deletes the record from the 'sessions' table corresponding
        to the given SQUIZZ session ID 

        Args:
            session_id: a SQUIZZ session ID string
        """
        query = "DELETE FROM sessions WHERE SessionKey = %s"
        values = [session_id]
        self.run_query(query, values, True)
        logger.info(f"Deleted session {session_id} from the database")