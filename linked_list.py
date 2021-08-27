class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        tmp_pointer = self.head

        if tmp_pointer is None:
            self.insert_at_begining(data)
            return
        while tmp_pointer.next:
            tmp_pointer = tmp_pointer.next

        tmp_pointer.next = Node(data)

    def insert_values(self,data_list):
        for data in data_list:
            self.insert_at_end(data)

    def remove_value(self,data):
        if self.node_length() == 0:
            return
        elif self.node_length() == 1 and data == self.head.data:
            self.head = None
            return
        pre_node = self.head
        current_node = pre_node.next
        if pre_node.data == data:
            self.head = current_node
            return
        while current_node.next:
            if current_node.data == data:
                pre_node.next = current_node.next
                break
            pre_node = current_node
            current_node = current_node.next




    def node_length(self):
        tmp_node = self.head
        if tmp_node is None:
            return 0
        length = 0
        while tmp_node.next:
            length +=1
            tmp_node = tmp_node.next
        return length

    def print(self):
        if self.head is None:
            print("List is empty.")
            return

        pointer = self.head
        listr = ""

        while pointer:
            listr += str(pointer.data) + " --> "
            pointer = pointer.next
        print(listr)

if __name__ == "__main__":
    li = LinkedList()
    # li.insert_at_begining(9)
    # li.insert_at_begining(4)
    # li.insert_at_end(5)
    # li.insert_at_end(43)
    li.insert_values(["banana","zinzer"])
    li.print()
    li.remove_value("zinzer")
    li.print()