import logging

# Default Python imports
import urllib.request # Encapsulates communication functions
from urllib.error import HTTPError
import csv
from io import StringIO

#Useful information: https://docs.python.org/3.1/howto/urllib2.html
url ='http://192.168.1.134:8000/python/' 

class CommunicationManager:

    def get(self, url):
        """ Given a URL, connect to that URL and extract the data from the package 
        Returns (String): the data in utf-8"""
        logging.debug(f'Requesting: {url}')
        response = urllib.request.urlopen(url)
        data = response.read()
        return data.decode("utf-8")

    def get_student(self, uid):
        """Sends a request to the server with the entered uid as a parameter.
        If the response is 404 return None otherwise return a Student object
        with the id, name, surname and uid stored in it.
        Returns (Student): Student created from the info provided by the server."""
        values = {
            'uid' : uid
        }

        data = urllib.parse.urlencode(values)
        url_student = url + 'request_id.php?' + data
        response_csv = ''
        try:
            response_csv = self.get(url_student)
        except HTTPError as e: 
            if '404' in str(e):
                print ("Not found")
                return None
        readCSV = csv.DictReader(StringIO(response_csv), delimiter=',')
        student_info = next(readCSV)
        student = Student(student_info['id'], student_info['name'], student_info['surname'], student_info['uid'])
        return student
        

    def get_query(self, student, table_name, params):
        """Get request with the student id for authentication
        Send table name and save the information 
        Returns (table): table is a .csv with all the table's info provided by the server"""
        values = {
            'student_id' : student.get_id(),
            'table_name' : table_name,
            **params}

        data = urllib.parse.urlencode(values)
        url_query = url + 'request_query.php?' + data
        table = self.get(url_query)

        return table
       

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
        return f'({self._id},{self._name} {self._surname},{self._uid})'


if __name__ == "__main__":
    cm = CommunicationManager()
    data = cm.get_student('87A6B812')
    print(data)