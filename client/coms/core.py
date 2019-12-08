import threading

# Default Python imports
import csv
import urllib.request # Contains communication functions
from urllib.error import HTTPError
from io import StringIO

# Module imports
from .parse import parse_csv_to_dict, parse_csv_to_list
from .student import Student

URL ='http://10.0.30.203:8000/python/'


def get_request(url, params=None):
    """Performs a http GET request to the given url with the given parameters."""
    if params is not None:
        args = urllib.parse.urlencode(params)
        url = url + '?' + args
    http_response = urllib.request.urlopen(url)
    return http_response.read().decode("utf-8")


def login(url, credentials, handle):
    task = lambda: get_student(url, credentials, handle)
    threading.Thread(target=task, daemon=True).start()


def get_student(url, credentials, handle):
    response = get_request(url, credentials)
    student_info = next(parse_csv_to_dict(response))
    student = Student(
        student_info['id'],
        student_info['name'],
        student_info['surname'],
        student_info['uid'])
    handle(student)

def query(url, args, handle):
    task = lambda: get_query(url, args, handle)
    threading.Thread(target=task, daemon=True).start()

def get_query(url, args, handle):
    response = get_request(url, args)
    csv_list = parse_csv_to_list(response)
    handle(csv_list)
