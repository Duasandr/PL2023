from rangedist import RangedDist


class AgeDist(RangedDist):
    xLabel = "Age group"
    yLabel = "Nº of afflicted patients"
    title = "Age Distribution Of Cardiac Disease"

    def __init__(self):
        super().__init__(5)

    def get_level(self, patient):
        return patient.age//self.xStep

    def get_x_label(self):
        return AgeDist.xLabel

    def get_y_label(self):
        return AgeDist.yLabel

    def get_title(self):
        return AgeDist.title
