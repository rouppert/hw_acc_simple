""" Test 2 : Comparing two load balancing algorithms

This test runs multiple simulations, with two given load balancing algorithms.
For each algorithm, it calculates the average throughput over all the simulations.
"""

import algorithms as alg
import analysis as an
import sys
from tqdm import tqdm

dflt_context = {
    #number of tasks currently running
    "N_TASKS" : 0, 
    #number of processors
    "N_CORES" : 8, 
    #number of tasks to be created at span cycle
    "S_TASKS" : 1000,
    #total number of tasks who have been running since the start of the simulation
    "T_TASKS" : 0, #DO NOT MODIFY
    #number of tasks which have yielded
    "Y_TASKS" : 0, #DO NOT MODIFY
    #time before each task spanning
    "S_PERIOD" : 200,
    #period of the load balancing process
    "LB_PERIOD" : 1,
    #duration of the load balancing process
    "LB_DURATION" : 0,
    #minimum lifetime of one task (in number of cycles)
    "MIN_LIFE" : 1,
    #maximum lifetime of one task (in number of cycles)
    "MAX_LIFE" : 5,
    #number of cycles to be run in the simulation
    "S_CYCLES" : 20000
}
 


def main(argv):
    #-------- Parameters --------
    it = 50
    alg1 = alg.simple_load_balancer
    alg2 = alg.simple_smart_lb
    #----------------------------


    thr1 = 0
    thr2 = 0
    thr3 = 0

    for i in tqdm(range(it), desc="Testing..."):
        thr1+=an.simulate(dict(dflt_context), alg1, True)['avg_thr']/it
        thr2+=an.simulate(dict(dflt_context), alg2, True)['avg_thr']/it
        thr3+=an.simulate(dict(dflt_context), None, False)['avg_thr']/it

    print("Average throughput for algorithm 1 ("+alg1.__name__+") : "+str(thr1))
    print("Average throughput for algorithm 2 ("+alg2.__name__+") : "+str(thr2))
    print("Average throughput without load balancing : "+str(thr3))

if __name__ == "__main__":
    main(sys.argv)