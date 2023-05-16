#!/usr/bin/python
import tempfile

import pytest

from diskq import PersistentPriorityQueue


@pytest.fixture
def persistent_priority_queue():
    # 创建一个临时文件作为测试的持久化优先级队列文件
    temp_dir = tempfile.TemporaryDirectory()
    queue = PersistentPriorityQueue(f"{temp_dir.name}.pkl")
    yield queue
    # 清理临时文件
    temp_dir.cleanup()


def test_put_and_get(persistent_priority_queue):
    # 测试优先级队列的放入和取出操作
    persistent_priority_queue.put((2, "item2"))
    persistent_priority_queue.put((1, "item1"))
    persistent_priority_queue.put((3, "item3"))

    item1 = persistent_priority_queue.get()
    item2 = persistent_priority_queue.get()
    item3 = persistent_priority_queue.get()

    assert item1 == (1, "item1")
    assert item2 == (2, "item2")
    assert item3 == (3, "item3")


def test_empty(persistent_priority_queue):
    # 测试优先级队列是否为空
    assert persistent_priority_queue.empty()

    persistent_priority_queue.put((1, "item1"))
    assert not persistent_priority_queue.empty()

    persistent_priority_queue.get()
    assert persistent_priority_queue.empty()


def test_size(persistent_priority_queue):
    # 测试优先级队列的大小
    assert persistent_priority_queue.size() == 0

    persistent_priority_queue.put((2, "item2"))
    persistent_priority_queue.put((1, "item1"))
    persistent_priority_queue.put((3, "item3"))

    assert persistent_priority_queue.size() == 3

    persistent_priority_queue.get()
    assert persistent_priority_queue.size() == 2
