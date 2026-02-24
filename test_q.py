from q import *

def test_empty():
    queue = Queue()
    assert queue.is_empty() == True

def test_add():
    queue = Queue()
    assert queue.head == None
    queue.add("Felicity")
    assert queue.head.data == "Felicity"
    queue.add("Robert")
    next_node = queue.head.next
    assert next_node.data == "Robert"

def test_size():
    queue = Queue()
    assert queue.size == 0
    queue.add("Felicity")
    assert queue.size == 1

def test_left():
    queue = Queue()
    queue.add("Robert")
    queue.add("Felicity")
    d = queue.pop_left()
    assert d.data == "Robert"
    assert queue.size == 1

if __name__ == "__main__":
    waitlist = Queue()
    waitlist.add("Amy")
    print(repr(waitlist))