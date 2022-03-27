import sys
import re
import csv
import json
from hw5_classes import News, PrivateAd, Joke
from datetime import datetime

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
            self.file_type = int(input("\n1-txt\n2-json\nChoose the file type and click Enter: "))
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

        self.type_news = "\n" + "News -------------------------" + "\n"
        self.dash = "-------------------------" + "\n"
        current_day = datetime.now()
        self.today = current_day.strftime("%d/%m/%Y, %H.%M") + "\n"

        self.type_ad = "\n" + "Private Ad -------------------------" + "\n"

        self.type_joke = "\n" + "Joke -------------------------" + "\n"

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


    def read_json(self):
        self.json_list = json.load(open("test.json", "r"))
        return self.json_list

    def write_json(self):
        for i, f in enumerate(self.json_list):
            for k, v in f.items():
                if k == "publication" and v == "News":
                    self.publish = f"{self.type_news}{f['news_text']}\n{f['city']}\n{self.today}{self.dash}"

                elif k == "publication" and v == "Private ad":
                    end_date = datetime.strptime(f['end_date'], '%d/%m/%Y')
                    e_date = end_date.strftime('%d/%m/%Y')
                    dates_diff = (end_date.date() - datetime.now().date()).days
                    self.publish = f"{self.type_ad}{f['ad_text']}\n{e_date}, {dates_diff} days left\n{self.dash}"

                elif k == "publication" and v == "Joke":
                    self.publish = f"{self.type_joke}{f['joke_text']}\n{self.dash}"

                with open(check_uploaded_file_data, "a") as file:
                    file.write(self.publish)
                break


try:
    while True:
        options = Options()
        if options.input_format == 2:
            if options.file_type == 1:
                options.words_info()
                options.letters_info()
            elif options.file_type == 2:
                options.read_json()
                options.write_json()
except KeyboardInterrupt:
    pass









