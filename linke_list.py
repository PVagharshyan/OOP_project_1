from typing import Any, Type

class LinkeList:
    class Node:
        def __init__(self):
            self._data = None
            self._next = None
            self._prev = None

        @property
        def data(self):
            return self._data

        @data.setter
        def data(self, data_value):
            self._data = data_value

        @property
        def next(self):
            return self._next

        @next.setter
        def next(self, next_value):
            self._next = next_value

        @property
        def prev(self):
            return self._prev

        @prev.setter
        def prev(self, prev_value):
            self._prev = prev_value

    def __init__(self):
        self._start = None
        self._end = None

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    def is_empty(self):
        return self._start == None

    def prepend(self, data):
        prepend_node = self.Node()
        prepend_node.data = data
        prepend_node.prev = None
        prepend_node.next = self._start
        if self._start != None:
            self._start.prev = prepend_node
        self._start = prepend_node
        if (self._end == None):
            self._end = prepend_node

    def append(self, data):
        append_node = self.Node()
        append_node.data = data
        append_node.prev = self._end
        append_node.next = None
        if self._end != None:
            self._end.next = append_node
        self._end = append_node
        if (self._start == None):
            self._start = append_node

    def insert_after(self, target_data, data):
        if (self._end == target_data):
            self.append(data)
            return

        new_node = self.Node()
        next_node = target_data.next
        prev_node = target_data

        new_node.data = data
        new_node.next = next_node
        new_node.prev = prev_node

        prev_node.next = next_node.prev = new_node

    def insert_before(self, target_data, data):
        if (self._start == target_data):
            self.prepend(data)
            return

        new_node = self.Node()
        next_node = target_data
        prev_node = target_data.prev

        new_node.data = data
        new_node.next = next_node
        new_node.prev = prev_node

        prev_node.next = next_node.prev = new_node

    def delete(self, data):
        tmp = self._start
        if self._start == None:
            raise ValueError("Error: list is empty!")
            return
        while tmp.next != None:
            if tmp.data == data:
                if tmp == self._start:
                    self._start = self._start.next
                    self._start.prev = None
                    return
                elif tmp == self._end:
                    self._end = self._end.prev
                    self._end.next = None
                    return
                tmp.prev.next = tmp.next
                tmp.next.prev = tmp.prev
                return
            tmp = tmp.next
        if tmp.data == data:
            if tmp == self._start:
                self._start = self._start.next
                self._start.prev = None
                return
            elif tmp == self._end:
                self._end = self._end.prev
                self._end.next = None
                return
            tmp.prev.next = tmp.next
            tmp.next.prev = tmp.prev
            return
        raise ValueError("Error: no such data exists")

    def display(self):
        tmp = self._start
        if self._start == None:
            print("[]")
            return
        result_str = "["
        while tmp.next != None:
            result_str += f" {tmp.data} "
            tmp = tmp.next
        result_str += f" {tmp.data} "
        result_str += "]"
        print(result_str)

def main():
    print("!link_list!")
    l1 = LinkeList()
    l1.display()
    l1.append(10)
    n_1 = l1.end
    l1.append(14)
    l1.append(12)
    l1.prepend(25)
    n_0 = l1.start
    l1.insert_before(n_1, "before")
    l1.insert_after(n_1, "after")
    l1.insert_before(n_0, "before")
    l1.display()
    l1.delete("before")
    l1.display()
    l1.delete(14)
    l1.delete(12)
    l1.display()

if __name__ == "__main__":
    main()


