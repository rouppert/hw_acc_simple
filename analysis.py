import numpy as np
import matplotlib.pyplot as plt
import hardware as hw
import random as rd
import time

def use_graph(proc_usage, context, lb_on):
    fig, axs = plt.subplots(len(proc_usage), sharex=True, sharey=True)
    xaxis = np.arange(0, context['S_CYCLES'])
    color = iter(plt.cm.rainbow(np.linspace(0, 1, len(proc_usage))))
    for i in range(len(proc_usage)):
        c = next(color)
        yaxis = np.array(proc_usage[i])
        axs[i].step(xaxis, yaxis, c=c)
        axs[i].legend('processor ' + str(i))
    lb = ''
    if lb_on: lb = 'lb'
    plt.savefig('graphs/'+lb+'_'+time.strftime("%Y%m%d-%H%M%S"))

def simulate(cxt, alg, LOAD_BALANCER_FLAG = False):
    proc_usage=[[] for i in range(cxt['N_CORES'])]
    queues = [hw.Exec_queue() for i in range(cxt['N_CORES'])]
    cur_cycle = 0
    core = 0

    while(cur_cycle<cxt['S_CYCLES']):
        if cur_cycle%cxt['S_PERIOD'] == 0:
            #new = rd.randrange(1, cxt['S_TASKS']+1)
            new = cxt['S_TASKS']
            for i in range(new):
                task = hw.Task(rd.randrange(cxt['MIN_LIFE'], cxt['MAX_LIFE']))
                cxt['N_TASKS']+=1
                cxt['T_TASKS']+=1
                queues[core].enqueue(task)
                core = (core + 1)%cxt['N_CORES']

        for i in range(len(queues)):
            if queues[i].len() == 0: proc_usage[i].append(0)
            else: proc_usage[i].append(1)
            queues[i].roll(cxt)
        if LOAD_BALANCER_FLAG and (cur_cycle+1)%cxt['LB_PERIOD']: 
            alg(queues, cxt)
            for queue in proc_usage:
                for i in range(min(cxt['LB_DURATION'],cxt['S_CYCLES']-(cur_cycle+1))): queue.append(0)
            cur_cycle+=cxt['LB_DURATION']
        cur_cycle+=1
    

    avg_thr = cxt['Y_TASKS']/cxt['T_TASKS']
    results = {
        'avg_thr' : avg_thr,
        'proc_usage' : proc_usage
    }
    return results