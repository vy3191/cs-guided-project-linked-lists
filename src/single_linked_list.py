
class LinkedListNode:  
  def __init__(self, value, next_node=None):
    self.value = value
    self.next = None
    self.next = next_node
    
class SLL:
  def __init__(self, head=None, tail=None):
    self.head = head
    self.tail = tail
    self.length = 0
  
  def add_to_head(self, value):
    new_node = LinkedListNode(value)  
    # if there are no nodes in the list at all
    if self.head is None:
      self.head = new_node
      self.tail = new_node
      self.head.next = None
    else:      
      new_node.next = self.head
      self.head =  new_node
      
    self.length += 1
      
  def add_to_tail(self,value):
    # if there are no nodes in the list
    new_node = LinkedListNode(value)
    if self.head == None or self.tail == None:
      self.add_to_head(new_node)
    else:
      self.tail.next = new_node
      self.tail = new_node  
      
    self.length += 1
    
  def remove_head(self):
    # if there are no nodes in the list
    if self.head is None:
      return None
    # if there is only one node in the list
    if self.head == self.tail:
      del_value = self.head.value
      self.head = None
      self.tail = None
      return del_value
    # if there are more than one node in the list
    if self.length > 1:
      del_value = self.head.value
      self.head = self.head.next
      return del_value
    self.length -= 1   
  
  def remove_tail(self):
    # if there are no nodes in the list
    if self.head is None or self.tail is None:
      return None
    # if there is only one node in the list
    if self.head == self.tail:
      self.remove_head()
    # if there are more than one node in the list
    if self.length > 1:
      del_value = self.tail.value
  
  def search(self, key):
    current = self.head
    while current:
      if current.value == key:
        print(f"yes, we have the node with the value {current.value}")
        return current
      else:
        current = current.next        
    return None    
  
  def reverse(self, head):
    # assign the given head to the current node
    current_node = head;
    # declare previous node with None value
    previous_node = None;
    # have a next node
    next_node = None;
    # as long as there is current node 
    while current_node:
      # assign the next node value -> current next
      next_node = current_node.next;
      # assign previous node value to the current next
      current_node.next = previous_node;
      # now assign next node value to current node
      current_node = next_node;
      
    return current_node  
          
        
  def __repr__(self):
    current = self.head
    nodes = []
    while current:
      if current is self.head:
        nodes.append(f"[Head:{current.value}]")
        current = current.next
      elif current.next is None:
        nodes.append(f"[Tail:{current.value}]") 
        current = current.next 
      else:
        nodes.append(f"[{current.value}]")    
        current = current.next
    return '--->'.join(nodes)      
           
    
    
    

linked_list = SLL()
linked_list.add_to_head(1)    
linked_list.add_to_head(2)    
linked_list.add_to_head(3)    
linked_list.add_to_head(4)    
linked_list.add_to_head(5)    
print(linked_list)