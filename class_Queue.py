# 3. Создать класс "очередь".

class Queue:
    def __init__(self, max_=32):
        if not str(max_).isdigit():
            raise Exception('Using NOT int type in max size')
        self.__max = int(max_)
        self.__queue = []
        if self.__max <= 0:
            raise Exception('Empty queue!')

    def __str__(self):
        if len(self.__queue) == 0:
            return f'Queue is empty!'
        return f'{self.__queue}'

    def __iter__(self):
        return iter(self.__queue)

    def is_empty(self):
        if len(self.__queue) > 0:
            return False
        else:
            return True

    def add_item(self, item):
        if self.length() == self.__max:
            raise Exception('Queue is full!')
        else:
            self.__queue.append(item)

    def add_items(self, *items):
        if len(items) > self.__max:
            raise Exception('Length of adding stack is MORE than max stack len!')
        elif len(self.__queue) + len(items) > self.__max:
            raise Exception(f'This adding will overflow stack! {self.__max - len(self.__queue)} positions left.')
        else:
            for i in items:
                self.__queue.append(i)

    def del_item(self):
        if self.length() < 1:
            raise Exception('Stack is empty')
        else:
            return self.__queue.pop(0)

    def length(self):
        return len(self.__queue)

    def show_queue(self):
        if len(self.__queue) > 0:
            print(self.__queue)
        else:
            print('Queue is empty!')

    def get_item(self):
        if len(self.__queue) == 0:
            raise Exception('Stack is empty!')
        else:
            return self.__queue[0]
