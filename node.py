# Implement your Node class here
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# ------------------------------------------------------------                      # 
# Design Memo                                                                       #
# ------------------------------------------------------------                      #
# Stacks and queues are both ways of organizing data, but they work differently     #
# depending on the situation. A stack uses a Last-In, First-Out (LIFO) approach,    #
# meaning the most recent item added is the first one to come back out. This        #
# makes a stack a natural fit for the Undo/Redo feature because the last action     #
# someone takes should be the first one that gets undone. Having two stacks—one     #
# for undo and one for redo—lets the system move actions back and forth in the      #
# order users expect.                                                               #

# Queues, on the other hand, follow First-In, First-Out (FIFO) logic. The first     #
# item added is always the first to be removed. This approach works best for the    #
# Help Desk example since customers should be helped in the order they arrive. A    #
# queue makes sure the process is fair and predictable, which is important in       #
# real-world service situations.                                                    #

# While Python’s built-in lists could be used for stacks and queues, they are not   #
# ideal because inserting or removing from the front of a list can be slow when     #
# the list is large. By using linked nodes, our custom stack and queue              #
# implementations avoid this problem. Push, pop, enqueue, and dequeue all run in    #
# constant time, which keeps the program simple, efficient, and true to the way     #
# these structures are meant to work.                                               #

