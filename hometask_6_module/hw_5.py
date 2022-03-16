from datetime import datetime

class Publication:
    def __init__(self):
        self.publication_text = " "

    def InputData(self):
        publication_type = int(input("1-News\n2-Private Ad\n3-Joke\nChoose the publication type and click Enter: "))
        if publication_type == 1:
            News().SaveDataIntoFile()
        elif publication_type == 2:
            PrivateAd().SaveDataIntoFile()
        elif publication_type == 3:
            Joke().SaveDataIntoFile()
        else:
            print("Please retry")

    def SaveDataIntoFile(self):
        with open(r"C:\Users\Gozel_Jorayeva\PycharmProjects\pythonProject\test1\Publication.txt", "a") as file:     # w or a
            file.write(self.publication_text)

class News(Publication):
    def __init__(self):
        super().__init__()
        self.text = input("Input the publication text: ")
        self.location = input("Input the location text: ")
        self.pub_type = "News -------------------------" + "\n"
        self.dash = "-------------------------" + "\n"
        current_day = datetime.now()
        self.publication_text = "\n" + self.pub_type + self.text + "\n" + self.location + "\n" + current_day.strftime("%d/%m/%Y, %H.%M" + "\n" + self.dash + "\n")


class PrivateAd(Publication):
    def __init__(self):
        super().__init__()
        self.pub_type = "Private Ad -------------------------" + "\n"
        self.text = input("Input the publication text: ")
        self.end_date = input("AD is actual till (dd/mm/yyyy): ")
        self.dash = "-------------------------" + "\n"
        self.date_format()
        self.publication_text = "\n" + self.pub_type + self.text + "\n" + f"Actual until: {self.end_date:%d/%m/%Y}, " + self.left_days() + " days left" + "\n" + self.dash + "\n"

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
        self.pub_type = "Joke -------------------------" + "\n"
        self.text = input("Input the publication text: ")
        self.dash = "-------------------------" + "\n"
        self.publication_text = "\n" + self.pub_type + self.text + "\n" + self.dash + "\n"
        print("Hahaha")
#
# try:
#     while True:
#         publication = Publication()
#         publication.InputData()
#         publication.SaveDataIntoFile()
#         publication = input('\nIf you input "stop" - program will stop\nIf you want to proceed just click "Enter"')
#         if publication == 'stop':
#             break
#         else:
#             pass
# except KeyboardInterrupt:
#     pass