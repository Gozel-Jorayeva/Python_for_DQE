# Input text is written to "Publication.txt"
# the same file "Publication.txt" can be loaded to see its statistics 
# if you want to see the statistics of the other file, just change the file name in "check_uploaded_file_data" variable

import sys
from hw5_class import News, PrivateAd, Joke
import re
import csv

check_uploaded_file_data = "Publication.txt"

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


        self.word_count_dict = {}
        self.word_count_csv_header = ["word", "count"]
        self.word_count_csv = "word_count.csv"

        self.letter_count_dict = {}
        self.letter_count_csv_header = ["letter", "count_all", "count_uppercase", "percentage"]
        self.letter_count_csv = "letter_count.csv"


    def words_info(self):
        with open(check_uploaded_file_data, "r") as text_file:
            read_word_file = re.findall(r"[\w']+", text_file.read().lower())
            for i in read_word_file:
                if i not in self.word_count_dict.keys():
                    self.word_count_dict[i] = 1
                elif i in self.word_count_dict.keys():
                    self.word_count_dict[i] += 1

        with open(self.word_count_csv, "w", newline="") as word_csv:
            writer = csv.DictWriter(word_csv, fieldnames=self.word_count_csv_header)
            writer.writeheader()
            for k, v in self.word_count_dict.items():
                writer.writerow({"word": k, "count": v})

    def letters_info(self):
        with open(check_uploaded_file_data, "r") as text_file:
            read_letter_file = re.findall("[a-zA-Z]", text_file.read())

        with open(self.letter_count_csv, "w", newline="") as letter_csv:
            writer = csv.DictWriter(letter_csv, fieldnames=self.letter_count_csv_header)
            writer.writeheader()
            check_file = []
            for i in read_letter_file:
                if i.lower() not in check_file:
                    self.letter_count_dict["letter"] = i.lower()
                    self.letter_count_dict["count_all"] = read_letter_file.count(i.upper()) + read_letter_file.count(i.lower())
                    self.letter_count_dict["count_uppercase"] = read_letter_file.count(i.upper())
                    self.letter_count_dict["percentage"] = round(self.letter_count_dict["count_all"] / len(read_letter_file) * 100, 2)
                    writer.writerow(self.letter_count_dict)
                    check_file.append(i.lower())


try:
    while True:
        options = Options()
        if options.input_format == 2:
            options.words_info()
            options.letters_info()
except KeyboardInterrupt:
    pass

