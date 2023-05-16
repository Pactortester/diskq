# DiskQ

![PyPI](https://img.shields.io/pypi/v/diskq) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/diskq) [![Downloads](https://static.pepy.tech/personalized-badge/diskq?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=downloads/total)](https://pepy.tech/project/diskq) ![GitHub top language](https://img.shields.io/github/languages/top/opendiskq/diskq) ![GitHub stars](https://img.shields.io/github/stars/opendiskq/diskq?style=social) ![https://blog.csdn.net/flower_drop](https://img.shields.io/badge/csdn-%40flower__drop-orange) [![autofix enabled](https://shields.io/badge/autofix.ci-yes-success?logo=data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjZmZmIiB2aWV3Qm94PSIwIDAgMTI4IDEyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCB0cmFuc2Zvcm09InNjYWxlKDAuMDYxLC0wLjA2MSkgdHJhbnNsYXRlKC0yNTAsLTE3NTApIiBkPSJNMTMyNSAtMzQwcS0xMTUgMCAtMTY0LjUgMzIuNXQtNDkuNSAxMTQuNXEwIDMyIDUgNzAuNXQxMC41IDcyLjV0NS41IDU0djIyMHEtMzQgLTkgLTY5LjUgLTE0dC03MS41IC01cS0xMzYgMCAtMjUxLjUgNjJ0LTE5MSAxNjl0LTkyLjUgMjQxcS05MCAxMjAgLTkwIDI2NnEwIDEwOCA0OC41IDIwMC41dDEzMiAxNTUuNXQxODguNSA4MXExNSA5OSAxMDAuNSAxODAuNXQyMTcgMTMwLjV0MjgyLjUgNDlxMTM2IDAgMjU2LjUgLTQ2IHQyMDkgLTEyNy41dDEyOC41IC0xODkuNXExNDkgLTgyIDIyNyAtMjEzLjV0NzggLTI5OS41cTAgLTEzNiAtNTggLTI0NnQtMTY1LjUgLTE4NC41dC0yNTYuNSAtMTAzLjVsLTI0MyAtMzAwdi01MnEwIC0yNyAzLjUgLTU2LjV0Ni41IC01Ny41dDMgLTUycTAgLTg1IC00MS41IC0xMTguNXQtMTU3LjUgLTMzLjV6TTEzMjUgLTI2MHE3NyAwIDk4IDE0LjV0MjEgNTcuNXEwIDI5IC0zIDY4dC02LjUgNzN0LTMuNSA0OHY2NGwyMDcgMjQ5IHEtMzEgMCAtNjAgNS41dC01NCAxMi41bC0xMDQgLTEyM3EtMSAzNCAtMiA2My41dC0xIDU0LjVxMCA2OSA5IDEyM2wzMSAyMDBsLTExNSAtMjhsLTQ2IC0yNzFsLTIwNSAyMjZxLTE5IC0xNSAtNDMgLTI4LjV0LTU1IC0yNi41bDIxOSAtMjQydi0yNzZxMCAtMjAgLTUuNSAtNjB0LTEwLjUgLTc5dC01IC01OHEwIC00MCAzMCAtNTMuNXQxMDQgLTEzLjV6TTEyNjIgNjE2cS0xMTkgMCAtMjI5LjUgMzQuNXQtMTkzLjUgOTYuNWw0OCA2NCBxNzMgLTU1IDE3MC41IC04NXQyMDQuNSAtMzBxMTM3IDAgMjQ5IDQ1LjV0MTc5IDEyMXQ2NyAxNjUuNWg4MHEwIC0xMTQgLTc3LjUgLTIwNy41dC0yMDggLTE0OXQtMjg5LjUgLTU1LjV6TTgwMyA1OTVxODAgMCAxNDkgMjkuNXQxMDggNzIuNWwyMjEgLTY3bDMwOSA4NnE0NyAtMzIgMTA0LjUgLTUwdDExNy41IC0xOHE5MSAwIDE2NSAzOHQxMTguNSAxMDMuNXQ0NC41IDE0Ni41cTAgNzYgLTM0LjUgMTQ5dC05NS41IDEzNHQtMTQzIDk5IHEtMzcgMTA3IC0xMTUuNSAxODMuNXQtMTg2IDExNy41dC0yMzAuNSA0MXEtMTAzIDAgLTE5Ny41IC0yNnQtMTY5IC03Mi41dC0xMTcuNSAtMTA4dC00MyAtMTMxLjVxMCAtMzQgMTQuNSAtNjIuNXQ0MC41IC01MC41bC01NSAtNTlxLTM0IDI5IC01NCA2NS41dC0yNSA4MS41cS04MSAtMTggLTE0NSAtNzB0LTEwMSAtMTI1LjV0LTM3IC0xNTguNXEwIC0xMDIgNDguNSAtMTgwLjV0MTI5LjUgLTEyM3QxNzkgLTQ0LjV6Ii8+PC9zdmc+)](https://autofix.ci)

DiskQ is a Python library for persistent queue management. It allows you to store queue data on disk, making it easier
to manage your data and prevent data loss in the event of system crashes or power outages.

# Installation

You can install DiskQ using pip:

```shell
pip install diskq
```

# Usage

## PersistentQueue

The PersistentQueue class is used to create a persistent queue. Here's an example:

```python
from diskq import PersistentQueue

# create a new persistent queue
queue = PersistentQueue('my_queue.pkl')

# add items to the queue
queue.put('item1')
queue.put('item2')
queue.put('item3')

# get items from the queue
item1 = queue.get()
item2 = queue.get()
item3 = queue.get()

```

## PersistentPriorityQueue

The PersistentPriorityQueue class is used to create a persistent priority queue. Here's an example:

```python
from diskq import PersistentPriorityQueue

# create a new persistent priority queue
queue = PersistentPriorityQueue('my_priority_queue.pkl')

# add items to the queue with priorities
queue.put((1, 'item1'))
queue.put((2, 'item2'))
queue.put((3, 'item3'))

# get items from the queue in order of priority
item1 = queue.get()
item2 = queue.get()
item3 = queue.get()

```

## PersistentLifoQueue

The PersistentLifoQueue class is used to create a persistent last-in, first-out (LIFO) queue. Here's an example:

```python
from diskq import PersistentLifoQueue

# create a new persistent LIFO queue
queue = PersistentLifoQueue('my_lifo_queue.pkl')

# add items to the queue
queue.put('item1')
queue.put('item2')
queue.put('item3')

# get items from the queue in reverse order
item3 = queue.get()
item2 = queue.get()
item1 = queue.get()

```

# License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.


