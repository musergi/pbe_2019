import logging

# Default Python imports
import csv
import urllib.request # Contains communication functions
from urllib.error import HTTPError
from io import StringIO

# Module imports
from .student import Student

URL ='http://192.168.1.134:8000/python/' 

def get_request(url, params):
    """Performs a get request to the given url with the given parameters.
    The function encodes the parameters into url format. Then creates the
    url by apending the url to the parameters using '?'. It then performs
    the request, if it fails this function will raise an HTTPError. Then 
    it decodes the response and returns it."""
    # Parse url
    param_str = urllib.parse.urlencode(params)
    get_url = f'{url}?{param_str}'

    # Request
    logging.debug(f'Resquesting: {get_url}')
    http_response = urllib.request.urlopen(get_url)

    # Read bytes and decode response
    data = http_response.read()
    return data.decode("utf-8")


def get_student(uid):
    """Returns the Student object with corresponding uid.
    Creates the proper url to perform the get request to. Performs
    the request specifying the uid if the request recives a 404 then
    it retuns None. Finally the funtion parses the received csv and
    returns a new Student object with the received data."""
    url = f'{URL}request_id.php'
    csv_str = ''

    try:
        csv_str = get_request(url, {'uid': uid})
    except HTTPError as e:
        if '404' in str(e):
            logging.debug('User with uid {uid} not found')
            return None

    csv_dict = csv.DictReader(StringIO(csv_str), delimiter=',')
    student_info = next(csv_dict) # Equivalent to csv_dict[0] but does not generate list
    return Student(student_info['id'], student_info['name'], student_info['surname'], student_info['uid'])

    
def get_query(student, table, params):
    """Returns the csv data contained in the given table.
    Creates the proper url to perform the get request to. Prepares
    the parameter dictionary and finally returns the received csv 
    string."""
    url = f'{URL}request_query.php'
    query_params = {
        'student_id': student.get_id(),
        'table_name': table,
        **params}

    csv_data = get_request(url, query_params)
    return csv_data