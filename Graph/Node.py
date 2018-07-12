import unittest
from Edge import Edge

class Node(object):
    """An object that holds the content of a node in a graph"""
    def __init__(self, id, connections = [], weights = []):
        self.id = id
        self.connections = []

        if len(connections) > 0 or len(weights) > 0:
            self.add_connections(connections, weights)

        return

    
    def add_connections(self, connections, weights):
        """Function to populate the connections as edge objects"""

        if len(connections) != len(weights):
            raise TypeError("Connection and weight arrays must be the same length.")

        for index in xrange(len(connections)):
            self.add_connection(connections[index], weights[index])

        return

    def add_connection(self, end_id, weight = 0):
        """Function to add one connection as edge object"""
        new_edge = Edge(self.id, end_id, weight)
        self.connections.append(new_edge)

        return


class NodeTest(unittest.TestCase):

    def test_constructor_no_connections(self):
        id = 2

        node = Node(id)

        self.assertEqual(node.id, id)
        self.assertEqual(len(node.connections), 0)

    def test_constructor_connections(self):
        id = 2
        connections = [4,2]
        weights = [0,1]

        node = Node(id, connections, weights)

        self.assertEqual(node.id, id)
        self.assertEqual(len(node.connections), 2)
        self.assertEqual(node.connections[0].start,2)
        self.assertEqual(node.connections[0].end,4)
        self.assertEqual(node.connections[0].weight,0)
        self.assertEqual(node.connections[1].start,2)
        self.assertEqual(node.connections[1].end,2)
        self.assertEqual(node.connections[1].weight,1)

    def test_constructor_error(self):
        id = 2
        connections = [4,2]
        weights = [0]

        with self.assertRaises(TypeError):
            node = Node(id, connections, weights)


if __name__ == '__main__':
    unittest.main()
