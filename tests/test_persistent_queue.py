#!/usr/bin/python
import tempfile

import pytest

from diskq import PersistentQueue


@pytest.fixture
def persistent_queue():
    # 创建一个临时文件作为测试的持久化队列文件
    temp_dir = tempfile.TemporaryDirectory()
    queue = PersistentQueue(f"{temp_dir.name}.pkl")
    yield queue
    double_queue = PersistentQueue(f"{temp_dir.name}.pkl")
    double_queue.task_done()
    # 清理临时文件
    temp_dir.cleanup()


def test_task_done(persistent_queue):
    persistent_queue.task_done()


def test_put_and_get(persistent_queue):
    # 测试队列的放入和取出操作
    persistent_queue.put("item1")
    persistent_queue.put("item2")

    item1 = persistent_queue.get()
    item2 = persistent_queue.get()

    assert item1 == "item1"
    assert item2 == "item2"


def test_empty(persistent_queue):
    # 测试队列是否为空
    assert persistent_queue.empty()

    persistent_queue.put("item1")
    assert not persistent_queue.empty()

    persistent_queue.get()
    assert persistent_queue.empty()


def test_size(persistent_queue):
    # 测试队列的大小
    assert persistent_queue.size() == 0

    persistent_queue.put("item1")
    persistent_queue.put("item2")
    persistent_queue.put("item3")

    assert persistent_queue.size() == 3

    persistent_queue.get()
    assert persistent_queue.size() == 2
