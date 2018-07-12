from GraphConfig import GraphConfig
from Graph import Graph

def main():

    #Create graph config
    initial_data = []

    p1 = GraphConfig()
    p1.start = 1
    p1.end = 2
    p1.bidirectional = True
    initial_data.append(p1)

    p2 = GraphConfig()
    p2.start = 1
    p2.end = 3
    p2.weight = 4
    initial_data.append(p2)

    p3 = GraphConfig()
    p3.start = 3
    p3.end = 5
    p3.bidirectional = True
    initial_data.append(p3)

    #Create graph
    ids = [1,2,3,4,5]
    graph = Graph(ids, initial_data)

    #Test for fully connected
    is_connected = graph.is_connected()
    print('is_connected: ' + str(is_connected))

    return


if __name__ == "__main__":
    main()