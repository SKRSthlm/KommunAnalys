from collections import OrderedDict
class InformationLog():
    """docstring for InformationLog."""

    def __init__(self):
        self._alertLog = OrderedDict()
        self._infoLog = OrderedDict()
        self._succeededYear = None

    def addInfo(self, prio, *messages):
        if prio == "high":
            self._alertLog[" ".join([str(x) for x in messages])] = None
        elif prio == "low":
            self._infoLog[" ".join([str(x) for x in messages])] = None

    def informUser(self):
        for message in self._alertLog.keys():
            print(message)

    def showLowPrioInfo(self):
        for message in self._infoLog.keys():
            print(message)

    def succeededYear(self, y):
        self._succeededYear = y

    def reset(self):
        self.__init__()
