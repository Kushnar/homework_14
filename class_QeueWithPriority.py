class QueueWithPriority:
    def __init__(self, max_=32):
        if not str(max_).isdigit():
            raise Exception('Using NOT int type in max size')
        self.__max = int(max_)
        self.__queue = []
        self.__priority_list = []
        if self.__max <= 0:
            raise Exception('Empty queue!')

    def __str__(self):
        if self.is_empty():
            return f'Queue is empty!'
        else:
            return self.__queue

    def is_empty(self):
        if self.length() > 0:
            return False
        else:
            return True

    def add_item(self, item, prior=0):
        if self.length() == self.__max:
            self.__priority_list.pop(0)
            self.__priority_list.append(prior)
            self.__queue.pop(0)
            self.__queue.append(item)
        else:
            self.__priority_list.append(prior)
            self.__queue.append(item)

    def add_items(self, *items):
        if self.length() + len(items) > self.__max:
            for i in items:
                if len(self.__queue) < self.__max:
                    self.__queue.append(i)
                    self.__priority_list.append(0)
                else:
                    self.__priority_list.pop(0)
                    self.__priority_list.append(0)
                    self.__queue.pop(0)
                    self.__queue.append(i)
        else:
            for i in items:
                self.__queue.append(i)

    def del_item(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        else:
            el = 0
            for i in self.__priority_list:
                if i > el:
                    el = i
            index_of_element = self.__priority_list.index(el)
            self.__priority_list.pop(index_of_element)
            return self.__queue.pop(index_of_element)

    def del_items(self, count_of_values):
        if self.is_empty():
            raise Exception('Queue is empty')
        elif self.length() >= count_of_values > 0:
            for i in range(count_of_values):
                el = 0
                for j in self.__priority_list:
                    if j > el:
                        el = j
                index_of_element = self.__priority_list.index(el)
                self.__priority_list.pop(index_of_element)
                self.__queue.pop(index_of_element)
        else:
            raise Exception('Count of deleted items is MORE than queue length.')

    def length(self):
        return len(self.__queue)

    def get_queue(self):
        queue_copy = self.__queue.copy()
        priority_copy = self.__priority_list.copy()
        queue_to_return = []
        if self.is_empty():
            return None
        else:
            for i in range(self.length()):
                if not self.is_empty():
                    el = 0
                    for j in priority_copy:
                        if j > el:
                            el = j
                    index_of_element = priority_copy.index(el)
                    queue_to_return.append(queue_copy[index_of_element])
                    queue_copy.pop(index_of_element)
                    priority_copy.pop(index_of_element)
                else:
                    break
            return queue_to_return

    def get_item(self):
        if self.is_empty():
            raise Exception('Queue is empty!')
        else:
            el = self.__priority_list[0]
            for i in self.__priority_list:
                if i > el:
                    el = i
            return self.__queue[self.__priority_list.index(el)]
