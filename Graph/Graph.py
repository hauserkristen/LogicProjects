from Edge import Edge
from Node import Node

class Graph(object):
    """An object that holds the content of an graph"""
    def __init__(self, node_ids, config):
        self.nodes = {}

        #Create node objects
        for node_id in node_ids:
            node = Node(node_id)
            self.nodes[node_id] = node

        #Add connections
        for connect in config:
            self.nodes[connect.start].add_connection(connect.end, connect.weight)
            if connect.bidirectional:
                self.nodes[connect.end].add_connection(connect.start, connect.weight)
        
        return


    def is_connected(self):
        connected = False

        return connected
        