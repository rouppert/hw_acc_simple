""" Test 0 : Runs a simple simulation

This test runs one simulation, with or without load balancing.
Returns the final throughput.
Saves the utilization graph of each processor.
"""
import algorithms as alg
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
    "S_PERIOD" : 20000,
    #period of the load balancing process
    "LB_PERIOD" : 1,
    #duration of the load balancing process
    "LB_DURATION" : 0,
    #minimum lifetime of one task (in number of cycles)
    "MIN_LIFE" : 1,
    #maximum lifetime of one task (in number of cycles)
    "MAX_LIFE" : 500,
    #number of cycles to be run in the simulation
    "S_CYCLES" : 20000
}
 


def main(argv):
    parser = argparse.ArgumentParser(
        prog='LoadBalancingSim',
        description='Simulating load balancing using an hardware accelerator'
    )

    parser.add_argument('-c', '--cycles', dest='s_cycles', type=int, help='Number of simulation cycles')
    parser.add_argument('-p', '--procs', dest='procs', type=int, help='Number of processors')
    parser.add_argument('-lb', '--load_balancing', dest='lb', action='store_true')
    parser.add_argument('-lbd', '--lb_duration', dest='lb_duration', type=int, help='Duration of the load balancing process')
    parser.add_argument('-lbp', '--lb_period', dest='lb_period', type=int, help='Period of the load balancing process')
    parser.add_argument('-g', '--graphs', dest='graphs', action='store_true')
    args = parser.parse_args()
    s_cycles = args.s_cycles
    procs = args.procs
    lb_duration = args.lb_duration
    lb_period = args.lb_period
    context = dflt_context
    if s_cycles!=None:
        context['S_CYCLES'] = s_cycles
    if procs!=None:
        context['N_CORES'] = procs
    if lb_duration!=None:
        context['LB_DURATION'] = lb_duration
    if lb_period!=None:
        context['LB_PERIOD'] = lb_period
    proc_usage = an.simulate(context, alg.simple_smart_lb, args.lb)['proc_usage']
    an.use_graph(proc_usage, context, args.lb)

if __name__ == "__main__":
    main(sys.argv)

