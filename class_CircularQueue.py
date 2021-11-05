class CircularQueue:
    def __init__(self, max_=32):
        if not str(max_).isdigit():
            raise Exception('Using NOT int type in max size')
        self.__max = int(max_)
        self.__queue = []
        if self.__max <= 0:
            raise Exception('Empty queue!')

    def __str__(self):
        if self.length() == 0:
            return f'Queue is empty!'
        return f'{self.__queue}'

    def is_empty(self):
        if self.length() > 0:
            return False
        else:
            return True

    def add_item(self, item):
        if self.length() == self.__max:
            self.__queue.pop(0)
            self.__queue.append(item)
        else:
            self.__queue.append(item)

    def add_items(self, *items):
        if self.length() + len(items) > self.__max:
            for i in items:
                if len(self.__queue) < self.__max:
                    self.__queue.append(i)
                else:
                    self.__queue.pop(0)
                    self.__queue.append(i)
        else:
            for i in items:
                self.__queue.append(i)

    def del_item(self):
        if self.length() < 1:
            raise Exception('Queue is empty')
        else:
            el = self.__queue.pop(0)
            self.__queue.append(el)
            return el

    def length(self):
        return len(self.__queue)

    def get_queue(self):
        if len(self.__queue) > 0:
            return self.__queue
        else:
            return None

    def get_item(self):
        if len(self.__queue) == 0:
            raise Exception('Queue is empty!')
        else:
            return self.__queue[0]
