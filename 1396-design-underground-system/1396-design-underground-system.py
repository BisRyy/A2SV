class UndergroundSystem:

    def __init__(self):
        self.openTrips = {} #id: station, time
        self.completedtrips = {} # station: [trip, trip]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.openTrips[id] = (stationName, t) 
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, timeStart = self.openTrips[id]
        del self.openTrips[id]

        if startStation + "-"+ stationName in self.completedtrips:
            self.completedtrips[startStation + "-"+ stationName].append(t-timeStart)
        else:
            self.completedtrips[startStation + "-"+ stationName] = [t-timeStart]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trips = self.completedtrips[startStation + "-"+ endStation]
        return sum(trips)/len(trips)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)