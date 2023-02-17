from myheartdist import MyHeartDist, plt


class RangedDist(MyHeartDist):
    def __init__(self, x_step):
        self.dict = {}
        self.xStep = x_step
        self.isSorted = False

    @classmethod
    def get_level(cls, patient) -> int:
        pass

    def get_key(self, patient):
        return f"[{self.get_level(patient)*self.xStep}-{self.get_level(patient)*self.xStep+self.xStep-1}]"

    def plot_graph(self):
        if not self.isSorted:
            self.dict = dict(sorted(self.dict.items()))
            self.isSorted = True

        if len(self.dict) > 10:
            plt.xlabel(self.get_y_label())
            plt.ylabel(self.get_x_label())
            plt.barh(list(self.dict.keys()), list(self.dict.values()), color=['blue', 'red'])
        else:
            plt.bar(list(self.dict.keys()), list(self.dict.values()), color=['blue', 'red'])

    def add(self, patient):
        key = self.get_key(patient)
        if key in self.dict:
            self.dict[key] += 1
        else:
            self.dict[key] = 1

    def __repr__(self):
        ret = "{:<8} {:<15}\n".format('Range', 'Value')
        for k, v in self.dict.items():
            ret += "{:<8} {:<15}\n".format(k, v)
        return ret
