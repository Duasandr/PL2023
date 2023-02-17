from patient import Patient
from genderdist import GenderDist
from cholesteroldist import CholesterolDist
from agedist import AgeDist


class MyHeart:
    def __init__(self, path_to_file):
        self.patients = []
        self.genderDist = GenderDist()
        self.ageDist = AgeDist()
        self.cholesterolDist = CholesterolDist()

        file = open(path_to_file, 'r')
        rows = file.readlines()

        for row in rows:
            if Patient.valid_csv_string(row):
                patient = Patient.from_csv_string(row)

                if patient is not None and patient.hasDisease:
                    self.patients.append(patient)
                    self.genderDist.add(patient)
                    self.ageDist.add(patient)
                    self.cholesterolDist.add(patient)
