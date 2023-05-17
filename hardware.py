class Exec_queue:
    """
    Represents the execution of one core of the processor.

    ...

    Attributes
    ----------
    queue : Task[]
        the list of the tasks to be executed
        next task is the one at the end of the list
    throughput : float
        the number of tasks which finished execution
    """
    def __init__(self):
        self.queue = []
        self.throughput = 0

    def enqueue(self, task):
        """
        Adds the given task at the end of the list.
        """
        self.queue = self.queue + [task]

    def dequeue(self):
        """
        Removes the last task of the list and returns it, if possible.
        """
        if len(self.queue)>0:
            task = self.queue.pop()
            return task
    
    def rev_enqueue(self, task):
        self.queue = [task] + self.queue

    def rev_dequeue(self, task):
        if len(self.queue)>0:
            task = self.queue.pop(0)
            return task

    def roll(self, cxt):
        """
        Simulates execution of a task on a time slice by popping the last task in the queue,
        checking if it finished its execution, and, if not, sending it back at the beginning
        of the queue.
        """
        if len(self.queue)>0:
            if self.queue[0].is_expired():
                self.dequeue()
                self.throughput+=1
                cxt['N_TASKS'] -= 1
            else:
                self.queue = [self.queue[-1]]+self.queue[0:-1]

    def len(self):
        return len(self.queue)

class Task:
    def __init__(self, lifespan):
        self.executed = 0
        self.lifespan = lifespan

    def is_expired(self):
        self.executed+=1
        return self.executed>self.lifespan