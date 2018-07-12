import unittest

class Edge(object):
    """An object that holds the content of an edge"""
    def __init__(self, start, end, weight = 0):
        self.start = start
        self.end = end
        self.weight = weight
        
class NodeTest(unittest.TestCase):

    def test_constructor_no_weight(self):
        start = 2
        end = 0

        edge = Edge(start, end)

        self.assertEqual(edge.start, start)
        self.assertEqual(edge.end, end)
        self.assertEqual(edge.weight, 0)

    def test_constructor_weight(self):
        start = 5
        end = 2
        weight = 6

        edge = Edge(start, end, weight)

        self.assertEqual(edge.start, start)
        self.assertEqual(edge.end, end)
        self.assertEqual(edge.weight, 6)

if __name__ == '__main__':
    unittest.main()
