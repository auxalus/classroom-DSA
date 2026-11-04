class Node:
  def __init__(self,val):
    self.data = val
    self.next = None
class LQueue:
  def __init__(self):
    self.front=self.rear=None
  def enqueue(self,new_node):
    if self.rear:
      self.rear.next = new_node
      self.rear = new_node
    else:
      self.front = self.rear = new_node