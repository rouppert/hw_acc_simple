import hardware as hw
import algorithms as alg

def balancing_is_fair(alg):
    context = {
        'N_CORES' : 4,
        'N_TASKS' : 8
    }
    queues = [hw.Exec_queue() for i in range(context['N_CORES'])]
    core = 0
    for i in range(context['N_TASKS']):
        task = hw.Task(1)
        queues[core].enqueue(task)
        core = (core + 1)%context['N_CORES']
    alg(queues, context)
    succeeded = True
    for queue in queues:
        print(queue.len())
        if queue.len() != 2: 
            succeeded = False
    return succeeded

print(balancing_is_fair(alg.simple_load_balancer))