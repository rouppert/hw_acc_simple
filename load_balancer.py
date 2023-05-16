import numpy as np
import random as rd
import algorithms as alg
import hardware as hw
import analysis as an
import sys
import argparse

dflt_context = {
    #number of tasks currently running
    "N_TASKS" : 0,
    #number of processors
    "N_CORES" : 8, 
    #number of tasks running at start of the simulation
    "I_TASKS" : 0,
    #number of tasks to be created at span cycle
    "S_TASKS" : 5,
    #time before each task spanning
    "S_PERIOD" : 100,
    #minimum lifetime of one task (in number of cycles)
    "MIN_LIFE" : 10,
    #maximum lifetime of one task (in number of cycles)
    "MAX_LIFE" : 100,
    #number of cycles to be run in the simulation
    "S_CYCLES" : 2000
}
 
def simulate(cxt, alg, LOAD_BALANCER_FLAG = False):
    proc_usage=[[] for i in range(cxt['N_CORES'])]
    queues = [hw.Exec_queue() for i in range(cxt['N_CORES'])]
    cur_cycle = 0
    core = 0

    while(cur_cycle<cxt['S_CYCLES']):
        if (cur_cycle+1)%cxt['S_PERIOD'] == 0:
            new = rd.randrange(1, cxt['S_TASKS']+1)
            for i in range(new):
                task = hw.Task(rd.randrange(cxt['MIN_LIFE'], cxt['MAX_LIFE']))
                cxt['N_TASKS']+=1
                queues[core].enqueue(task)
                core = (core + 1)%cxt['N_CORES']

        for i in range(len(queues)):
            if queues[i].len() == 0: proc_usage[i].append(0)
            else: proc_usage[i].append(1)
            queues[i].roll(cur_cycle, cxt)
        if LOAD_BALANCER_FLAG: alg(queues, cxt)
        cur_cycle+=1

    avg_thr = an.avg_throughput(queues, cxt)
    if LOAD_BALANCER_FLAG: 
        print("With load balancing :")
    else:
        print("Without load balancing :")
    print("avg_thr = "+str(avg_thr))
    an.use_graph(proc_usage, cxt)

def main(argv):
    parser = argparse.ArgumentParser(
        prog='LoadBalancingSim',
        description='Simulating load balancing using an hardware accelerator'
    )

    parser.add_argument('-c', '--cycles', dest='s_cycles', type=int, help='Number of simulation cycles')
    parser.add_argument('-p', '--procs', dest='procs', type=int, help='Number of processors')
    parser.add_argument('-lb', '--load_balancing', dest='lb', action='store_true')
    parser.add_argument('-lb', '--load_balancing', dest='lb', action='store_true')
    args = parser.parse_args()
    s_cycles = args.s_cycles
    procs = args.procs
    context = dflt_context
    if s_cycles!=None:
        context['S_CYCLES'] = s_cycles
    if procs!=None:
        context['N_CORES'] = procs
    simulate(context, alg.simple_load_balancer, args.lb)

if __name__ == "__main__":
    main(sys.argv)

