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
        return f'({self._id},{self._name} {self._surname},{self._uid})'