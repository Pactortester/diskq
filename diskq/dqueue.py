#!/usr/bin/python
# encoding=utf-8
"""
DiskQ is a Python package that provides persistent queues using disk storage.
"""
import os
import pickle
import queue
import threading
from queue import Empty

import dill


class PersistentQueue:
    """
    q = PersistentQueue('Queue.pkl')
    q.put(1)
    q.put(2)
    assert q.get() == 1
    assert q.get() == 2
    """

    def __init__(self, filename):
        self.filename = os.path.join(filename)
        self.task_queue = self._read_queue_from_file()
        self.lock = threading.Lock()

    def _read_queue_from_file(self):
        try:
            with open(self.filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return []

    def _write_queue_to_file(self):
        with threading.Lock():
            with open(self.filename, "wb") as f:
                pickle.dump(self.task_queue, f)

    def put(self, item):
        with threading.Lock():
            self.task_queue.append(item)
            self._write_queue_to_file()

    def get(self):
        with threading.Lock():
            item = self.task_queue.pop(0)
            self._write_queue_to_file()
            return item

    def empty(self):
        with threading.Lock():
            return len(self.task_queue) == 0

    def task_done(self):
        pass

    def size(self):
        with threading.Lock():
            return len(self.task_queue)


class PersistentPriorityQueue:
    """
    q = PersistentPriorityQueue('PriorityQueue.pkl')
    q.put((2, 'b'))
    q.put((1, 'a'))
    q.put((3, 'c'))
    assert q.get() == (1, 'a')
    assert q.get() == (2, 'b')
    assert q.get() == (3, 'c')
    """

    def __init__(self, filename):
        self.lock = threading.Lock()
        self.filename = os.path.join(filename)
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                self.queue = dill.load(f)
        else:
            self.queue = queue.PriorityQueue()

    def put(self, item):
        with self.lock:
            self.queue.put(item)
            self._write_queue_to_file()

    def get(self):
        with self.lock:
            item = self.queue.get()
            self._write_queue_to_file()
            return item

    def empty(self):
        with self.lock:
            return self.queue.empty()

    def size(self):
        with self.lock:
            return self.queue.qsize()

    def _write_queue_to_file(self):
        with open(self.filename, "wb") as f:
            dill.dump(self.queue, f)


class PersistentLifoQueue:
    """
    q = PersistentLifoQueue('LifoQueue.pkl')
    q.put(1)
    q.put(2)
    assert q.get() == 2
    assert q.get() == 1
    """

    def __init__(self, filename):
        self.lock = threading.Lock()
        self.filename = os.path.join(filename)
        self.stack = self._load_stack_from_file()

    def _load_stack_from_file(self):
        try:
            with open(self.filename, "rb") as f:
                stack = pickle.load(f)
        except FileNotFoundError:
            stack = []
        return stack

    def _write_stack_to_file(self):
        with threading.Lock():
            with open(self.filename, "wb") as f:
                pickle.dump(self.stack, f)

    def put(self, item):
        with threading.Lock():
            self.stack.append(item)
            self._write_stack_to_file()

    def get(self, block=True, timeout=None):
        with threading.Lock():
            if block:
                while not self.stack:
                    self.lock.release()
                    try:
                        self.lock.acquire(timeout=timeout)
                    except Exception:
                        raise Empty
                    else:
                        self.lock.acquire()
            elif not self.stack:
                raise Empty

            item = self.stack.pop()
            self._write_stack_to_file()
            return item

    def empty(self):
        with threading.Lock():
            return len(self.stack) == 0

    def size(self):
        return len(self.stack)
