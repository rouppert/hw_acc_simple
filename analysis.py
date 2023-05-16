import numpy as np
import matplotlib.pyplot as plt

def use_graph(proc_usage, context):
    fig, axs = plt.subplots(len(proc_usage), sharex=True, sharey=True)
    xaxis = np.arange(0, context['S_CYCLES'])
    for i in range(len(proc_usage)):
        yaxis = np.array(proc_usage[i])
        axs[i].step(xaxis, yaxis)
        axs[i].legend('processor ' + str(i))
    plt.show()

def avg_throughput(queues, context):
    avg_thr = 0
    for queue in queues:
        avg_thr+=queue.throughput/context['N_CORES']
    return avg_thr