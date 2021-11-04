# 2. Создать класс "стек".

class Stack:
    def __init__(self, max_=32):
        if not str(max_).isdigit():
            raise Exception('Using NOT int type in size or max size')
        self.__max = int(max_)
        self.__stack = []
        if self.__max <= 0:
            raise Exception('Empty stack!')

    def __str__(self):
        return f'{self.__stack}'

    def __iter__(self):
        iterator = self.__stack
        iterator.reverse()
        return iter(iterator)

    def is_empty(self):
        if len(self.__stack) > 0:
            return False
        else:
            return True

    def add_item(self, item):
        if self.length() == self.__max:
            raise Exception('Stack is full!')
        else:
            self.__stack.append(item)

    def add_items(self, *items):
        if len(items) > self.__max:
            raise Exception('Length of adding stack is MORE than max stack len!')
        elif len(self.__stack) + len(items) > self.__max:
            raise Exception(f'This adding will overflow stack! {self.__max - len(self.__stack)} positions left.')
        else:
            for i in items:
                self.__stack.append(i)

    def length(self):
        return len(self.__stack)

    def del_item(self):
        if self.length() < 1:
            raise Exception('Stack is empty')
        else:
            i = self.__stack[-1]
            del self.__stack[-1]
            return i

    def show_stack(self):
        if len(self.__stack) > 0:
            print(self.__stack)
        else:
            print('Stack is empty!')

    def get_item(self):
        if len(self.__stack) == 0:
            raise Exception('Stack is empty!')
        else:
            return self.__stack[-1]
