from node import Node

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
    
    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.get_head_node())
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        print("hello")
        print(current_node.value)
        print("yello")
        print(current_node.next_node.value)
        while current_node:
            print("does this work?")
            print(current_node.value)
            print("and this??")
            #print(current_node.get_next_node().get_value())
            print(current_node.next_node.value)
            string_list += str(current_node.value) + "\n"
            current_node = current_node.get_next_node()
        return string_list
    
    def simple_should_work(self):
        current_node = self.head_node
        print("so does this work?")
        print(current_node.value)
        while current_node:
            print("about to do work")
            print(current_node)
            #the 'bound method' stuff at the bottom tells me that what is being saved is the act of doing the function, and not what the function returns. I've done this before though, and it's never given me issue. With and without parenthesis shit breaks. I am so mad.``
            print(current_node.value)
            print("done with that part")
            #running get_next_node and get_next_node() do the exact same thing :))))))))))
            #current_node = current_node.get_next_node()
            current_node = current_node.next_node
    
    def remove_node(self, value_to_remove):
        current_node = self.head_node
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.next_node = next_node.get_next_node()
                    current_node = None
                else:
                    current_node = next_node