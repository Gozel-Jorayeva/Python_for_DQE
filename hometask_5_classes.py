# needs improvement. Not finished 
from enum import Enum
from datetime import datetime

class PublicationType(Enum):
    NEWS = 1
    AD = 2
    JOKE = 3


class Publication():
    def __init__(self, text="", location="", publication_type=""):
        self.publication_type = publication_type
        self.text = text
        self.location = location

    def SaveDataIntoFile(self):
        with open(r"C:\PythonClassTask\Publication.txt", 'a') as file:     # w
            file.write(PublicationType(self.publication_type).name + " -------------------------" + "\n")
            file.write(self.text + "\n")
            file.write(self.location + "\n")
            today = datetime.now()
            file.write(today.strftime("%d/%m/%Y, %H:%M"))


    def InputData(self):
        self.publication_type = int(input("Choose the publication type: "))
        self.text = input("Input the publication text: ")
        self.location = input("Input the location text: ")
        self.SaveDataIntoFile()


try:
    while True:
        publication = Publication()
        publication.InputData()
        publication = input('If you input "stop" - program will stop\n')
        if publication == 'stop':
            break
        else:
            pass
except KeyboardInterrupt:
    pass





