from myheartdist import MyHeartDist, plt
from patient import Patient


class GenderDist(MyHeartDist):
    xLabel = "Gender"
    yLabel = "Nº of afflicted patients"
    title = "Gender Distribution Of Cardiac Disease"

    def __init__(self):
        self.dict = {
            'F': 0,
            'M': 0
        }

    def plot_graph(self):
        plt.bar(list(self.dict.keys()), list(self.dict.values()), color=['blue', 'red'])

    def get_x_label(self):
        return GenderDist.xLabel

    def get_y_label(self):
        return GenderDist.yLabel

    def get_title(self):
        return GenderDist.title

    def add(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError

        self.dict[patient.gender] += 1

    def __repr__(self):
        ret = "{:<8} {:<15}\n".format('Female', 'Male')
        ret += "{:<8} {:<15}\n".format(self.dict['F'], self.dict['M'])

        return ret
