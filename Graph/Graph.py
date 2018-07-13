
import unittest
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
        """Function that determines if every node is connected to at least one other node"""
        connected_ids = self.get_connected_nodes()

        return len(connected_ids) == len(self.nodes)


    def get_connected_nodes(self):
        """Function that returns list of nodes that are connected to at least on other node"""
        #Create list of ids
        connected_ids = []

        for node_id in self.nodes.keys():
            node = self.nodes[node_id]

            #Get end ids for all connections since start will always be node.id
            connection_ids = [n.end for n in node.connections]

            #Remove own id since nodes can loop back to itself
            connection_ids.remove(node.id)

            #If the length of connection ids is 0, then node is not connected
            if len(connected_ids) > 0:
                connected_ids.append(node.id)

        return connected_ids
        