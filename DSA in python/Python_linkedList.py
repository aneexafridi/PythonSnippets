class LinkedList:
    def __init__(self):
        self.head=None
    
    def __repr__(self):
        node=self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        node.append("None")
        return " -> ".join(nodes)        
        
        
        
        
class Node:
    def __init__(self,data):
        self.data=data
        self.Next=None
    
    def __repr__(self):
        return self.data