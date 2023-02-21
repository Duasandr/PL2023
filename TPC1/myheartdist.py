import matplotlib.pyplot as plt
from patient import Patient


class MyHeartDist:

    def show_graph(self):
        plt.xlabel(self.get_x_label())
        plt.ylabel(self.get_y_label())
        plt.title(self.get_title())
        self.plot_graph()
        plt.show()

    @classmethod
    def plot_graph(cls) -> None:
        pass

    @classmethod
    def get_x_label(cls) -> str:
        pass

    @classmethod
    def get_y_label(cls) -> str:
        pass

    @classmethod
    def get_title(cls) -> str:
        pass

    @classmethod
    def add(cls, patient: Patient) -> None:
        """
        :param patient: Patient object. Holds information to update distribution.
        :return: None.
        :raises TypeError: Patient object is mandatory.

        Adds patient info to the distribution.

        Important:
        ---------
        Checking if a patient has the disease must be done prior method call.
        """
        pass

    @classmethod
    def __repr__(cls):
        pass
