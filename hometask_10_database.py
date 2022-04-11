
import sys
import re
import csv
import json
from datetime import datetime
import xml.etree.ElementTree as Et
import os
import sqlite3

check_uploaded_file_data = "Publication.txt"


class Publication:
    def __init__(self):
        self.publication_text = " "
        self.word_count_dict = {}
        self.word_count_csv_header = ["word", "count"]
        self.word_count_csv = "word_count.csv"

        self.letter_count_dict = {}
        self.letter_count_csv_header = ["letter", "count_all", "count_uppercase", "percentage"]
        self.letter_count_csv = "letter_count.csv"

    def InputData(self):
        self.input_format = int(input(
            "\n1-Writing for publication\n2-Upload data from file\n3-Stop the program\nDefine your input format and click Enter: "))
        if self.input_format == 1:
            self.publication_type = int(
                input("1-News\n2-Private Ad\n3-Joke\nChoose the publication type and click Enter: "))
            if self.publication_type == 1:
                News().SaveDataIntoFile()
            elif self.publication_type == 2:
                PrivateAd().SaveDataIntoFile()
            elif self.publication_type == 3:
                Joke().SaveDataIntoFile()
            else:
                print("Please retry")

        elif self.input_format == 2:
            self.file_choose = int(input(f"\n1-Default Folder\n2-Provided file path\nChoosing: "))
            self.file_type = int(input("\n1-txt\n2-json\n3-xml\nChoose the file type and click Enter: "))
            if self.file_choose == 1:
                self.file_path = sys.path[1]
            elif self.file_choose == 2:
                self.file_path = input(r"Input file path (ex. C:\): ")
            self.file_name = input("Input file name: ")

        elif self.input_format == 3:
            sys.exit()

    def create_db_table(self):
        with sqlite3.connect('abc.db') as self.connection:
            with self.connection as conn:
                self.cursor = conn.cursor()
                self.cursor.execute("DROP TABLE IF EXISTS news")
                self.cursor.execute("DROP TABLE IF EXISTS ad")
                self.cursor.execute("DROP TABLE IF EXISTS joke")
                # id INTEGER PRIMARY KEY AUTOINCREMENT,
                self.cursor.execute("CREATE TABLE IF NOT EXISTS news (type varchar, text varchar (255) UNIQUE, city varchar, current_date varchar)")
                self.cursor.execute("CREATE TABLE IF NOT EXISTS ad (type varchar, text varchar (255) UNIQUE, end_date varchar, left_days varchar)")
                self.cursor.execute("CREATE TABLE IF NOT EXISTS joke (type varchar, text varchar (255) UNIQUE)")


    def insert_to_table(self):
        if self.publication_type == 1:
            # self.cursor.execute("INSERT INTO news VALUES (?,?,?)", (self.news_text, self.location, self.today))
            self.cursor.execute("INSERT INTO news VALUES (?,?,?,?)", ('news', News().news_text, News().location, News().today))
            self.cursor.execute(f"SELECT * FROM news")

        elif self.publication_type == 2:
            self.cursor.execute(f"INSERT INTO ad VALUES (?,?,?,?)", ('private ad', PrivateAd().ad_text, PrivateAd().end_date, PrivateAd().left_days))
            self.cursor.execute(f"SELECT * FROM ad")

        elif self.publication_type == 3:
            self.cursor.execute(f"INSERT INTO joke VALUES (?,?)", ('joke', Joke().joke_text))
            self.cursor.execute(f"SELECT * FROM joke")
        #
        # self.cursor.execute(f"SELECT * FROM news")
        # self.cursor.execute(f"SELECT * FROM ad")
        # self.cursor.execute(f"SELECT * FROM joke")

        gg = self.cursor.fetchall()
        print(gg)
        self.cursor.close()


    def SaveDataIntoFile(self):
        with open(r"C:\Users\Gozel_Jorayeva\PycharmProjects\pythonProject\test1\Publication.txt", 'a') as file:
            file.write(self.publication_text)

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
                    self.letter_count_dict["count_all"] = read_letter_file.count(i.upper()) + read_letter_file.count(
                        i.lower())
                    self.letter_count_dict["count_uppercase"] = read_letter_file.count(i.upper())
                    self.letter_count_dict["percentage"] = round(
                        self.letter_count_dict["count_all"] / len(read_letter_file) * 100, 2)
                    writer.writerow(self.letter_count_dict)
                    check_file.append(i.lower())

    def read_json(self):
        self.json_list = json.load(open("test.json", "r"))
        return self.json_list

    def write_json(self):
        for i, f in enumerate(self.json_list):
            for k, v in f.items():
                if k == "publication" and v == "News":
                    self.publish = f"{News().type_news}{f['news_text']}\n{f['city']}\n{News().today}{News().dash}"

                elif k == "publication" and v == "Private ad":
                    end_date = datetime.strptime(f['end_date'], '%d/%m/%Y')
                    e_date = end_date.strftime('%d/%m/%Y')
                    dates_diff = (end_date.date() - datetime.now().date()).days
                    self.publish = f"{PrivateAd().type_ad}{f['ad_text']}\n{e_date}, {dates_diff} days left\n{PrivateAd().dash}"

                elif k == "publication" and v == "Joke":
                    self.publish = f"{Joke().type_joke}{f['joke_text']}\n{Joke().dash}"

                with open(check_uploaded_file_data, "a") as file:
                    file.write(self.publish)
                break

    def read_xml(self):
        tree = Et.parse(open("test.xml", "r"))
        self.root = tree.getroot()
        return self.root

    def write_xml(self):
        for e in self.root.findall('publication'):
            for pub in e:
                if pub.text == "News":
                    self.publish = f"{News().type_news}{pub.attrib['text']}\n{pub.attrib['city']}\n{News().today}{News().dash}"

                elif pub.text == "Private Ad":
                    end_date = datetime.strptime(pub.attrib['end_date'], '%d/%m/%Y')
                    e_date = end_date.strftime('%d/%m/%Y')
                    dates_diff = (end_date.date() - datetime.now().date()).days
                    self.publish = f"{PrivateAd().type_ad}{pub.attrib['text']}\n{e_date}, {dates_diff} days left\n{PrivateAd().dash}"

                elif pub.text == "Joke":
                    self.publish = f"{Joke().type_joke}{pub.attrib['text']}\n{Joke().dash}"

                with open(check_uploaded_file_data, "a") as file:
                    file.write(self.publish)
        os.remove("test.xml")

class News(Publication):
    def __init__(self):
        super().__init__()
        self.news_text = input("Input the publication text: ")
        self.location = input("Input the location text: ")
        self.type_news = "\n" + "News -------------------------" + "\n"
        self.dash = "-------------------------" + "\n"
        current_day = datetime.now()
        self.today = current_day.strftime("%d/%m/%Y, %H.%M")
        self.publication_text = self.type_news + self.news_text + "\n" + self.location + "\n" + self.today + "\n" + self.dash


class PrivateAd(Publication):
    def __init__(self):
        super().__init__()
        self.type_ad = "Private Ad -------------------------" + "\n"
        self.ad_text = input("Input the publication text: ")
        self.end_date = input("AD is actual till (dd/mm/yyyy): ")
        self.dash = "-------------------------"
        self.date_format()
        self.publication_text = "\n" + self.type_ad + self.ad_text + "\n" + f"Actual until: {self.end_date:%d/%m/%Y}, " + self.left_days() + " days left" + "\n" + self.dash + "\n"

    def date_format(self):
        try:
            self.end_date = datetime.strptime(self.end_date, "%d/%m/%Y")
        except:
            raise ValueError

    def left_days(self):
        today = datetime.now()
        dates_diff = self.end_date - today
        return str(dates_diff.days)


class Joke(Publication):
    def __init__(self):
        super().__init__()
        self.type_joke = "Joke -------------------------" + "\n"
        self.joke_text = input("Input the publication text: ")
        self.dash = "-------------------------"
        self.publication_text = "\n" + self.type_joke + self.joke_text + "\n" + self.dash + "\n"
        print("Hahaha")

try:
    while True:
        options = Publication()
        options.InputData()
        if options.input_format == 1:
            options.create_db_table()
            options.insert_to_table()
        elif options.input_format == 2:
            if options.file_type == 1:
                options.words_info()
                options.letters_info()
            elif options.file_type == 2:
                options.read_json()
                options.write_json()
            elif options.file_type == 3:
                options.read_xml()
                options.write_xml()
except KeyboardInterrupt:
    pass
