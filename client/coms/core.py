# Default Python imports
import urllib.request # Encapsulates communication functions

#Useful information: https://docs.python.org/3.1/howto/urllib2.html

class CommunicationManager:
    
    def get(self, url):
        """ Given a URL, connect to that URL and extract the data from the package 
        Returns (String): the data in utf-8"""
        response = urllib.request.urlopen(url)
        data = response.read()
        return data.decode("utf-8")

    def get_student(self, uid):
        """Sends a request to the server with the entered uid as a parameter.
        If the response is 404 return None otherwise return a Student object
        with the id, name, surname and uid stored in it.
        Returns (Student): Student created from the info provided by the server."""
        request = urllib.request.Request('uid')
        student = urllib.request.urlopen(request)
        if (student.get_header() == "Error404"):
            return None
        return student.read()

    def get_query(self, student, table):
        """Get request with the student id for authentication
        Send table name and save the information 
        Returns (table): table is a .csv with all the table's info provided by the server"""
        data = urllib.parse.urlencode(table)
        request = urllib.request.Request(student.get_uid(), data)
        self.table = urllib.request.urlopen(request)
        return table.read()


class Student:
    """Class representing a student"""
    def __init__(self, u_id, name, surname, uid):
        self._id = u_id
        self._name = name
        self._surname = surname
        self._uid = uid

    #TODO: Getters
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
        raise Exception('Not implemented')


if __name__ == "__main__":
    cm = CommunicationManager()
    data = cm.get("http://10.0.30.203:8000/python/connect_server.php")
    print(data)