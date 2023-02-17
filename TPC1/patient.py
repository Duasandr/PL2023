import re


class Patient:
    # age,bloodPressure, cholesterol, and bpm exceptions not handled. An age of 999 checks true
    # delimiters are checked individually. A badly delimited string like "40,M;140,289;172,0" would check true
    pattern = "^([0-9]{1,3}[;|,][mMfF][;|,][0-9]{1,3}[;|,][0-9]{1,3}[;|,][0-9]{1,3}[;|,][1|0])$"
    delimiterPattern = "[,|;]+"

    def __init__(self, age, gender, blood_pressure, cholesterol, bpm, has_disease):
        self.age = int(age)
        self.gender = gender
        self.bloodPressure = int(blood_pressure)
        self.cholesterol = int(cholesterol)
        self.bpm = int(bpm)
        self.hasDisease = bool(int(has_disease))

    @classmethod
    def from_csv_string(cls, csv_string):
        tokens = re.split(Patient.delimiterPattern, csv_string)
        if int(tokens[3]) != 0:
            return cls(tokens[0], tokens[1].capitalize(), tokens[2], tokens[3], tokens[4], tokens[5])
        else:
            return None
    
    @staticmethod
    def valid_csv_string(csv_string):
        return re.match(Patient.pattern, csv_string)

    def is_null(self):
        return False
