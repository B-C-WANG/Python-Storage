import time
import pp


ppservers = ()

job_server = pp.Server(ppservers=ppservers)

print("starting work with %d workers." % job_server.get_ncpus())

def time_cost_function():
    for _ in range(10000000):
        pass


stime = time.time()


time_cost_function()
print("Use no parallel, cost time: %.4f" % (time.time() - stime))

time.sleep(3) # to wait for show the difference in the tesk manager

work_num = 16

stime = time.time()
jobs = [job_server.submit(time_cost_function) for _ in range(work_num)]

for job in jobs:
    job()

print("Use parallel cost time: %.4f" % ((time.time() - stime)/work_num))

job_server.print_stats()


