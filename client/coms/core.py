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

        request_response = urllib.request.Request(uid)

        if request_response.get_header == "HTTP/1.0 404 Not Found":
            return None
           
        elif Student.uid == uid:
            return Student

        raise Exception('Not implemented')

    def get_query(self, student, table):
        """Get request with the student id for authentication"""
        
        query = self.student.get_id
        

        raise Exception('Not implemented')


class Student:
    """Class representing a student"""
    def __init__(self, u_id, name, surname, uid):
        self._id = u_id
        self._name = name
        self._surname = surname
        self._uid = uid

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_uid(self):
        return self._uid


    def __str__(self):
        """String representation of the class."""

        return 'u_id, name, surname, uid'   # o hacer con gets? toString
        


if __name__ == "__main__":
    cm = CommunicationManager()
    data = cm.get("http://10.0.30.203:8000/python/connect_server.php")
    print(data)