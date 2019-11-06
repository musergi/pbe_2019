# Default Python imports
import urllib.request # Encapsulates communication functions


class CommunicationManager:
    """
    Given a URL, connect to that URL and extract the data from the package
    """
    def get(self, url):
        response = urllib.request.urlopen(url)
        data = response.read()
        return data.decode("utf-8")

    def get_student(self, uid):
        """Sends a request to the server with the entered uid as a parameter.
        If the response is 404 return None otherwise return a Student object
        with the id, name, surname and uid stored in it.
        Returns (Student): Student created from the info provided by the server."""
        raise Exception('Not implemented')

    def get_query(self, student, table):
        """Get request with the student id for authentication"""
        raise Exception('Not implemented')


class Student:
    """Class representing a student"""
    def __init__(self, u_id, name, surname, uid):
        self._id = u_id
        self._name = name
        self._surname = surname
        self._uid = uid

    #TODO: Getters

    def __str__(self):
        """String representation of the class."""
        raise Exception('Not implemented')


if __name__ == "__main__":
    cm = CommunicationManager()
    data = cm.get("http://10.0.30.203:8000/python/connect_server.php")
    print(data)