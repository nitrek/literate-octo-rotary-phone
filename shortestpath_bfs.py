# Problem Name is &&& Train Map &&& PLEASE DO NOT REMOVE THIS LINE.

"""

/**
 * Instructions to candidate.
 *  1) Run this code in the REPL to observe its behaviour. The
 *     execution entry point is main().
 *  2) Consider adding some additional tests in doTestsPass().
 *  3) Implement def shortestPath(self, fromStationName, toStationName)
 *     method to find shortest path between 2 stations
 *  4) If time permits, some possible follow-ups.
 */

 /**
 *      Visual representation of the Train map used
 *  
 *      King's Cross St Pancras --- Angel ---- Old Street
 *      |                   \                            |
 *      |                    \                            |
 *      |                     \                            |
 *      Russell Square         Farringdon --- Barbican --- Moorgate
 *      |                                                  /
 *      |                                                 /
 *      |                                                /
 *      Holborn --- Chancery Lane --- St Paul's --- Bank
 */

"""

from functools import reduce
import sys
"""
/**
 * class Station
 *
 *  Respresents Station in the rail network. Each station is identified by
 *  unique name. Station is connected with other stations - this information
 *  is stored in the 'neighbours' field. Two station objects with the same name are 
 *  equal therefore they are considered to be same station.
 */
"""
stationCount = 0
global pred 
global dist
class Station:
    
    def __init__(self, name):
        global stationCount
        self._stationNumber = stationCount
        stationCount = stationCount +1
        self._name = name
        self._neighbours = []

    def getName(self):
        return self._name
    
    def getStationNumber(self):
        return self._stationNumber
    
    def addNeighbour(self, station):
        self._neighbours.append(station)

    def getNeighbours(self):
        return self._neighbours

    def __eq__(self, other):
        return isinstance(other, Station) and self._name == other.getName()

    def __hash__(self):
        return hash((self._name))

"""
 /**
 * class TrainMap
 *
 *  Respresents whole rail network - consists of number of the Station objects.
 *  Stations in the map are bi-directionally connected. Distance between any 2 stations
 *  is of same constant distance unit. This implies that shortest distance between any
 *  2 stations depends only on number of stations in between  
 */
"""
class TrainMap:

    def __init__(self):
        self._stations = {}
        self._stations1 = {}
        self.count = 0

    def addStation(self, stationName):
        self._stations[stationName] = Station(stationName)
        self._stations1[self.count] = self._stations[stationName]
        self.count = self.count + 1
        return self
    def getNumberOfStations(self):
        return self.count
    
    def getStation(self, stationName):
        return self._stations[stationName]    
    
    def getStationByNumber(self, number):
        return self._stations1[number] 
    
    def connectStations(self, fromStation, toStation):
        fromStation.addNeighbour(toStation)
        toStation.addNeighbour(fromStation)
        return self

    def convertPathToString(self, path):
        path = path[:len(path)-1]
        path = path[::-1]
        if(len(path) == 0):
            return ""
        else:    
            return reduce(lambda s1, s2: s1 + "->" + s2, map(lambda station: station.getName(), path))
    def printshortestPath(self,fromStationName, toStationName,count):
  
        pred=[0 for i in range(count)]
        dist=[0 for i in range(count)]
        if( fromStationName == toStationName):
            return []
        fromstation = self.getStation(fromStationName)
        toStation = self.getStation(toStationName)
        
        queue = []
        #for i in range(count)
        visited = [False for i in range(count)]

        dist = [sys.maxsize for i in range(count)]
        pred = [-1 for i in range(count)]

        visited[fromstation.getStationNumber()] = True
        dist[fromstation.getStationNumber()] = 0
        queue.append(fromstation)
        pathexists = False
        #BFS
        while(len(queue) > 0):
            currStation = queue.pop(0)
            currName = currStation.getName()
            for neighbour in currStation.getNeighbours():
                namen = neighbour.getName()
                if(not visited[neighbour.getStationNumber()]):
                    visited[neighbour.getStationNumber()] = True
                    dist[neighbour.getStationNumber()] = dist[currStation.getStationNumber()] + 1
                    pred[neighbour.getStationNumber()] = currStation
                    queue.append(neighbour)

                    if (neighbour.getName() == toStationName):
                        pathexists = True
                        #print("found")
        if ( not pathexists):
            print("not possible")
            return []
        path = []
        crawl = self.getStation(toStationName)
        global stn
        path.append(crawl)
        stn = crawl.getStationNumber()
        while (pred[stn] != -1):
            stn = crawl.getStationNumber()
            path.append(pred[stn])
            crawl = pred[stn]
        return path
 
"""
 *      Visual representation of the Train map used
 *  
 *      King's Cross St Pancras --- Angel ---- Old Street
 *      |                   \                            |
 *      |                    \                            |
 *      |                     \                            |
 *      Russell Square         Farringdon --- Barbican --- Moorgate
 *      |                                                  /
 *      |                                                 /
 *      |                                                /
 *      Holborn --- Chancery Lane --- St Paul's --- Bank--------b2------b3
 */
"""
def doTestsPass():
    # todo: implement more tests, please
    # feel free to make testing more elegant
    trainMap = TrainMap()
    trainMap.addStation("King's Cross St Pancras").addStation("Angel").addStation("Old Street").addStation("Moorgate")\
    .addStation("Farringdon").addStation("Barbican").addStation("Russel Square").addStation("Holborn")\
    .addStation("Chancery Lane").addStation("St Paul's").addStation("Bank").addStation("b2").addStation("b3")
    
    trainMap.connectStations(trainMap.getStation("King's Cross St Pancras"), trainMap.getStation("Angel"))\
    .connectStations(trainMap.getStation("King's Cross St Pancras"), trainMap.getStation("Farringdon"))\
    .connectStations(trainMap.getStation("King's Cross St Pancras"), trainMap.getStation("Russel Square"))\
    .connectStations(trainMap.getStation("Russel Square"), trainMap.getStation("Holborn"))\
    .connectStations(trainMap.getStation("Holborn"), trainMap.getStation("Chancery Lane"))\
    .connectStations(trainMap.getStation("Chancery Lane"), trainMap.getStation("St Paul's"))\
    .connectStations(trainMap.getStation("St Paul's"), trainMap.getStation("Bank"))\
    .connectStations(trainMap.getStation("Angel"), trainMap.getStation("Old Street"))\
    .connectStations(trainMap.getStation("Old Street"), trainMap.getStation("Moorgate"))\
    .connectStations(trainMap.getStation("Moorgate"), trainMap.getStation("Bank"))\
    .connectStations(trainMap.getStation("Farringdon"), trainMap.getStation("Barbican"))\
    .connectStations(trainMap.getStation("Barbican"), trainMap.getStation("Moorgate"))\
    .connectStations(trainMap.getStation("Bank"), trainMap.getStation("b2"))\
    .connectStations(trainMap.getStation("b2"), trainMap.getStation("b3"))\
      .connectStations(trainMap.getStation("Moorgate"), trainMap.getStation("b3"))

    #print(stationCount,trainMap.getNumberOfStations())
    solution = "King's Cross St Pancras->Russel Square->Holborn->Chancery Lane->St Paul's"
    print(trainMap.convertPathToString(trainMap.printshortestPath("King's Cross St Pancras", "b3",trainMap.getNumberOfStations())))
    #print(trainMap.printshortestPath("King's Cross St Pancras", "St Paul's",trainMap.getNumberOfStations()))
    return solution == trainMap.convertPathToString(trainMap.printshortestPath("King's Cross St Pancras", "Bank",trainMap.getNumberOfStations()))


if __name__ == "__main__":
    if(doTestsPass()):
        print("All Tests Pass")
    else:
        print("Some tests fail")
