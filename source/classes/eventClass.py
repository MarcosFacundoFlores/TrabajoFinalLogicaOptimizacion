class Event:

    def __init__(self, taskName, squad, hoursCount, isFixed, coordinates ) -> None:
        self.taskName = taskName
        self.squad = squad
        self.hoursCount = hoursCount
        self.isFixed = isFixed
        self.coordinates = coordinates