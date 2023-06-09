""" Test 1 : Comparing of various load_balancing frequencies

This test runs multiple simulations of executions with load balancing,
incrementing the value of the period of the load balancing process at
each simulation.
Then plots the throughput based on the load balancing period.
"""

import algorithms as alg
import analysis as an
import sys
import argparse
import matplotlib.pyplot as plt

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
    "S_PERIOD" : 1000,
    #period of the load balancing process
    "LB_PERIOD" : 1,
    #duration of the load balancing process
    "LB_DURATION" : 0,
    #minimum lifetime of one task (in number of cycles)
    "MIN_LIFE" : 200,
    #maximum lifetime of one task (in number of cycles)
    "MAX_LIFE" : 300,
    #number of cycles to be run in the simulation
    "S_CYCLES" : 20000
}
 


def main(argv):
    parser = argparse.ArgumentParser(
        prog='LoadBalancingSim',
        description='Simulating load balancing using an hardware accelerator'
    )

    parser.add_argument('-i', '--iterations', dest='it', type=int, help='Number of iterations', default = 30)
    args = parser.parse_args()
    it = args.it
    thr_ls = []
    context = dflt_context
    for i in range(it):
        print(i)
        print(context['LB_PERIOD'])
        thr_ls.append(an.simulate(context, alg.simple_load_balancer, True)['avg_thr'])
        context['LB_PERIOD']+=100
        context['N_TASKS']=0
    plt.plot(thr_ls)
    plt.show()

if __name__ == "__main__":
    main(sys.argv)