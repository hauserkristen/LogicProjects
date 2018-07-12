class GraphConfig(object):
    """An object that holds the content required to create a graph object"""
    def __init__(self):
        self.start_id = 0
        self.end_id = 0
        self.is_bidirectional = False
        self.weight_val = 0

    @property
    def start(self):
        return self.start_id

    @start.setter
    def start(self, value):
        self.start_id = value
    
    @property
    def end(self):
        return self.end_id
    
    @end.setter
    def end(self, value):
        self.end_id = value

    @property
    def weight(self):
        return self.weight_val

    @weight.setter
    def weight(self, value):
        self.weight_val = value
    
    @property
    def bidirectional(self):
        return self.is_bidirectional

    @bidirectional.setter
    def bidirectional(self, value):
        self.is_bidirectional = value

