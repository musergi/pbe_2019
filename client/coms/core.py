""" Imported libraries
    this one uses python's standards """

import urllib.request
""" Encapsulates communication functions"""
class CommunicationManager:
    """
    Given a URL, connect to that URL and extract the data from the package
    """
    def get(self, url):
        response = urllib.request.urlopen(url)
        data = response.read()
        return data.decode("utf-8")

if __name__ == "__main__":
    cm = CommunicationManager()
    data = cm.get("http://ardi.cat")
    print(data)