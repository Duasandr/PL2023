from rangedist import RangedDist


class CholesterolDist(RangedDist):
    xLabel = "Cholesterol levels"
    yLabel = "Nº of afflicted patients"
    title = "Cholesterol Distribution Of Cardiac Disease"

    def __init__(self):
        super().__init__(10)

    def get_level(self, patient):
        return patient.cholesterol//self.xStep

    def get_x_label(self):
        return CholesterolDist.xLabel

    def get_y_label(self):
        return CholesterolDist.yLabel

    def get_title(self):
        return CholesterolDist.title
