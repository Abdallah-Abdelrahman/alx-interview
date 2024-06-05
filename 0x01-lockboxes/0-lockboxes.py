#!/usr/bin/python3
'''Module defines `Node`, `LinkedList`, `Queue` classes
and `canUnlockAll` function
'''


class Node:
    '''define a node in the singly linked list'''
    def __init__(self, value: int):
        '''initialize the instance'''
        self.value: int = value
        self.next: Node | None = None


class LinkedList:
    '''define a singly linked list'''
    def __init__(self):
        '''initialize the instance'''
        self.head = None
        self.tail = None

    def append(self, value: int):
        '''append a value at the end of the list'''
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        elif self.tail:
            self.tail.next = node
            self.tail = node

    def prepend(self, value: int):
        '''prepend a value in the list'''
        node = Node(value)
        if self.head:
            node.next = self.head.next
        self.head = node

    def remove_start(self):
        '''remove from the beginning of a linked list'''
        if self.head:
            tmp = self.head
            val = tmp.value
            self.head = tmp.next
            if not self.head:
                self.tail = self.head
            tmp = None
            return val
        raise IndexError('Removing from an empty linkedlist')


class Queue:
    '''Define a queue data structure'''
    def __init__(self):
        '''initialize the instance'''
        self.rear = 0
        self.front = 0
        self.singly_list = LinkedList()

    def enqueue(self, val):
        '''append a value at the end'''
        self.rear += 1
        self.singly_list.append(val)

    def dequeue(self) -> int:
        '''remove a value from the front.

        Returns:
            removed value
        '''
        if self.front < self.rear:
            self.front += 1
            return self.singly_list.remove_start()
        raise IndexError('dequeue from an empty queue')


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened.
    Args:
        boxes(List[List[int]]): list of lists of integers
    Returns:
        bool: True if all boxes can be opened, else return False
    '''
    if not isinstance(boxes, list):
        return False

    len_ = len(boxes)
    unlocked = set([0])
    q = Queue()
    q.enqueue(0)

    while q.front != q.rear:
        if q.front >= len_:
            break
        for key in boxes[q.dequeue()]:
            if key not in unlocked and key < len_:
                unlocked.add(key)
                q.enqueue(key)

    return len_ == len(unlocked)
