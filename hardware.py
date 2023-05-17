class Exec_queue:
    def __init__(self):
        self.queue = []
        self.throughput = 0

    def enqueue(self, task):
        self.queue = self.queue + [task]

    def dequeue(self):
        if len(self.queue)>0:
            task = self.queue.pop()
            return task
    
    def rev_enqueue(self, task):
        self.queue = [task] + self.queue

    def rev_dequeue(self, task):
        if len(self.queue)>0:
            task = self.queue.pop(0)
            return task

    def roll(self, cur_cycle, cxt):
        if len(self.queue)>0:
            if self.queue[0].is_expired():
                self.dequeue()
                self.throughput+=1/(cur_cycle+1)
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