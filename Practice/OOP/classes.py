import datetime
from datetime import date

class User:
    """ For now only storing basic data about a person, their name and birthday displayed
    as DDMMYYYY """

    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday
        # extract first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[1]

    def age(self):
        """ Return the age of the user """
        today = datetime.date(2023, 7, 14)
        yyyy = int(self.birthday[4:7])
        mm = int(self.birthday[2:3])
        dd = int(self.birthday[0:1])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)



