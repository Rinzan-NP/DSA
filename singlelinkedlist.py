class Node():
    def __init__(self,data = None, next = None) -> None:
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self) -> None:
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return
        val = self.head
        while val.next is not None:
            val = val.next
        val.next = Node(data,None)
        return

    def insert_by_list(self,list1):
        for item in list1:
            self.insert_at_end(item)

    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return
        val = self.head
        while val:
            print(val.data, end= "  ")
            val = val.next
        print()

    def get_len(self):
        count = 0
        val = self.head
        while val is not None:
            count += 1
            val = val.next
        return count
    
    def delete_at(self,index):
        position = 1
        if index < 0 or index >  self.get_len():
            print("Invalid index")
            return
        val = self.head
        while val is not None:
            if position == index - 1:
                val.next = val.next.next
                break
            position += 1
            val = val.next

    def insert_at(self, index, element):
        position = 1
        if index < 0 or index >  self.get_len():
            print("Invalid index")
            return
        val = self.head
        while val is not None:
            if position == index - 1:
                val.next = Node(element,val.next)
            position += 1
            val = val.next
           
    def remove_duplicates(self):
        if self.head is None:
            return

        val = self.head
        seen_data = set([val.data])
        while val.next:
            if val.next.data in seen_data:
                val.next = val.next.next
            else:
                seen_data.add(val.next.data)
                val = val.next

    def in_reverse_printing(self):
        val = self.head
        stack = []
        while val:
            stack.append(val.data)
            val = val.next
        while stack:
            print(stack.pop(),end="  ")

    
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

            return prev
        
        

llist = LinkedList()
llist.insert_by_list([1,2,2,4,5])
llist.revesrse()
