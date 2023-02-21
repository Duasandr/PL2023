import re


class Patient:
    # age,bloodPressure, cholesterol, and bpm exceptions not handled. An age of 999 checks true
    # delimiters are checked individually. A badly delimited string like "40,M;140,289;172,0" would check true
    pattern = "^([0-9]{1,3}[;|,][mMfF][;|,][0-9]{1,3}[;|,][0-9]{1,3}[;|,][0-9]{1,3}[;|,][1|0])$"
    delimiterPattern = "[,|;]+"

    # Token indexes
    AGE = 0
    GENDER = 1
    BLOOD_PRESSURE = 2
    CHOLESTEROL = 3
    BPM = 4
    HAS_DISEASE = 5

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
        if int(tokens[Patient.CHOLESTEROL]) > 0 and 0 < int(tokens[Patient.BPM]) < 250:
            return cls(tokens[Patient.AGE],
                       tokens[Patient.GENDER].capitalize(),
                       tokens[Patient.BLOOD_PRESSURE],
                       tokens[Patient.CHOLESTEROL],
                       tokens[Patient.BPM],
                       tokens[Patient.HAS_DISEASE])
        else:
            return None
    
    @staticmethod
    def valid_csv_string(csv_string):
        return re.match(Patient.pattern, csv_string)
