#!/usr/bin/python
"""
@Author  :  Lijiawei
@Date    :  2023/5/16 3:20 下午
@Desc    :  test_persistent_lifo_queue line.
"""
import tempfile

import pytest

from diskq.dqueue import PersistentLifoQueue


@pytest.fixture
def persistent_lifo_queue():
    # 创建一个临时文件作为测试的持久化LIFO队列文件
    temp_dir = tempfile.TemporaryDirectory()
    queue = PersistentLifoQueue(f"{temp_dir.name}.pkl")
    yield queue
    # 清理临时文件
    temp_dir.cleanup()


def test_put_and_get(persistent_lifo_queue):
    # 测试LIFO队列的放入和取出操作
    persistent_lifo_queue.put(1)
    persistent_lifo_queue.put(2)
    persistent_lifo_queue.put(3)

    item1 = persistent_lifo_queue.get()
    item2 = persistent_lifo_queue.get()
    item3 = persistent_lifo_queue.get()

    assert item1 == 3
    assert item2 == 2
    assert item3 == 1


def test_empty(persistent_lifo_queue):
    # 测试LIFO队列是否为空
    assert persistent_lifo_queue.empty()

    persistent_lifo_queue.put(1)
    assert not persistent_lifo_queue.empty()

    persistent_lifo_queue.get()
    assert persistent_lifo_queue.empty()


def test_size(persistent_lifo_queue):
    # 测试LIFO队列的大小
    assert persistent_lifo_queue.size() == 0

    persistent_lifo_queue.put(1)
    persistent_lifo_queue.put(2)
    persistent_lifo_queue.put(3)

    assert persistent_lifo_queue.size() == 3

    persistent_lifo_queue.get()
    assert persistent_lifo_queue.size() == 2
