# Input data (news, ad, joke) will be written to the file "Publication.txt"
# Any file can be taken to upload the records 
# All data from deleted file will be uploaded to the "news_feed.txt" file.

import sys
import os
from hw_5 import News, PrivateAd, Joke
from hw_4 import normalize_letter_cases
import re


class Options:

    def __init__(self):
        self.input_format = int(input("\n1-Writing for publication\n2-Upload data from file\n3-Stop the program\nDefine your input format and click Enter: "))
        if self.input_format == 1:
            self.publication_type = int(input("\n1-News\n2-Private Ad\n3-Joke\nChoose the publication type and click Enter: "))
            if self.publication_type == 1:
                News().SaveDataIntoFile()
            elif self.publication_type == 2:
                PrivateAd().SaveDataIntoFile()
            elif self.publication_type == 3:
                Joke().SaveDataIntoFile()

        elif self.input_format == 2:
            self.file_choose = int(input(f"\n1-Default Folder\n2-Provided file path\nChoosing: "))
            if self.file_choose == 1:
                self.file_path = sys.path[1]
            elif self.file_choose == 2:
                self.file_path = input(r"Input file path (ex. C:\): ")
            self.file_name = input("Input file name: ")

        elif self.input_format == 3:
            sys.exit()

    def read_data(self):
        try:
            self.source_file_path = os.path.join(self.file_path, self.file_name)
            self.source_file = open(self.source_file_path, "r").read()
            self.text_from_file = re.split("\n\n", self.source_file)
            return self.text_from_file
        except OSError:
            print("File was not found!")
            sys.exit()

    def write_data(self):
        with open("news_feed.txt", "a") as file:
            for i in self.text_from_file:
                ii = normalize_letter_cases(i)
                file.write(ii + "\n\n")
            os.remove(self.source_file_path)


try:
    while True:
        options = Options()
        if options.input_format == 2:
            options.read_data()
            options.write_data()
except KeyboardInterrupt:
    pass
