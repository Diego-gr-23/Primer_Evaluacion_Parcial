from node import Node


class MyList:
    def __init__(self):
        self.size = 0
        self.head: Node | None = None
        self.tail: Node | None = None

    def prepend(self, data: int):
        while True:
            if self.is_empty():
                new_node = Node(data)
                self.head = new_node
                self.tail = new_node
                self.size += 1
            else:
                new_node = Node(data)
                new_node.next = self.head
                self.head = new_node
                self.size += 1
            break

    def append(self, data: str):
        if self.is_empty():
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def search_by_value(self, data: str):
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            else:
                current = current.next
        raise Exception('Element not found')

    def search_by_index(self, index: int):
        current = self.head
        current_index = 0
        while current is not None:
            if current_index == index:
                return current
            else:
                current = current.next
                current_index += 1
        raise Exception("The position doesn't exist")

    def is_empty(self) -> bool:
        return self.head is None and self.tail is None

    def transversal(self):
        current = self.head
        result = ''
        while current is not None:
            result += str(current)
            current = current.next
            if current is not None:
                result += ''
                
        return result

    def insert_at(self, data: str, index: int):
        if index == 0:
            self.prepend(data)
        elif index == self.size:
            self.append(data)
        elif 0 < index < self.size:
            new_node = Node(data)
            previous = self.search_by_index(index - 1)
            new_node.next = previous.next
            previous.next = new_node
            self.size += 1
        else:
            raise Exception("The pos doesn't")

    def shift(self) -> int:
        if self.is_empty():
            raise Exception('Pile sub-overflow')
        elif self.head is self.tail:
            current = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return current.data
        else:
            current = self.head
            self.head = current.next
            current.next = None
            self.size -= 1
            return current.data

    def pop(self) -> int:
        if self.is_empty():
            raise Exception('Sub-overflow')
        elif self.head is self.tail:
            current = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return current.data
        else:
            current = self.tail
            previous = self.search_by_index(self.size - 2)
            self.tail = previous
            previous.next = None
            self.size -= 1

            return current.data

    def remove_at(self, index: int):
        if index == 0:
            return self.shift()
        elif index == self.size - 1:
            return self.pop()
        elif 0 < index < self.size - 1:
            current = self.search_by_index(index)
            previous = self.search_by_index(index - 1)
            previous.next = current.next
            current.next = None
            self.size -= 1
        else:
            raise Exception("The position doesn't exist\n")

    def search_position(self, ref: str)-> int:
        current = self.head
        index = 0
        while current is not None:
            if current.data is ref:
                return index
            else:
                current = current.next
                index += 1
        raise Exception("That ref doesn't exist \n")

    def remove_by_value(self, data: str)-> int:
        current = self.search_by_value(data)

        if current is self.head:
            self.shift()
            return 0
        elif current is self.tail:
            self.pop()
            return self.size
        else:
            pos = self.search_position(current)
            previous = self.search_by_index(pos - 1)
            previous.next = current.next
            current.next = None
            self.size -= 1

            return pos
        
    def count_elements(self):
        if self.size == 0:
            return "#0"
        else:
            return self.size