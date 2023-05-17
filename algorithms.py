import numpy as np

def simple_load_balancer(queues, cxt):
    lqueues = [queue.len() for queue in queues]
    min_load = np.min(lqueues)
    min_id = np.argmin(lqueues)
    max_load = np.max(lqueues)
    max_id = np.argmax(lqueues)
    i=0
    while max_load-min_load>min(cxt['N_TASKS']%cxt['N_CORES'], 1):
        task = queues[max_id].dequeue()
        queues[min_id].enqueue(task)
        lqueues = [queue.len() for queue in queues]
        min_load = np.min(lqueues)
        min_id = np.argmin(lqueues)
        max_load = np.max(lqueues)
        max_id = np.argmax(lqueues)

def simple_smart_lb(queues, cxt):
    lqueues = [queue.len() for queue in queues]
    min_load = np.min(lqueues)
    min_id = np.argmin(lqueues)
    max_load = np.max(lqueues)
    max_id = np.argmax(lqueues)
    i=0
    while max_load-min_load>min(cxt['N_TASKS']%cxt['N_CORES'], 1):
        task = queues[max_id].rev_dequeue()
        queues[min_id].rev_enqueue(task)
        lqueues = [queue.len() for queue in queues]
        min_load = np.min(lqueues)
        min_id = np.argmin(lqueues)
        max_load = np.max(lqueues)
        max_id = np.argmax(lqueues)