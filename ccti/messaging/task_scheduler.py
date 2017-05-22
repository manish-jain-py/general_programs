import time
from multiprocessing import Pool
from trees_and_graphs.graph import Graph


def get_dependencies(task):
    for t in tasks:
        if t[0] == task:
            return t[1]


def build_graph(tasks):
    g = Graph()
    for task_dep in tasks:
        v = g.add_vertex(task_dep[0])
        v.color = 'white'
    for task_dep in tasks:
        main_task = g.get_vertex(task_dep[0])
        for dependee_task in task_dep[1]:
            node = g.get_vertex(dependee_task)
            g.add_edge(node, main_task)

    return g


def get_starting_points(g):
    all_tasks = [v.id for v in g.get_all_vertices()]
    dependent_tasks = set()
    for v in all_tasks:
        vertex = g.get_vertex(v)
        for neighbor in vertex.get_all_neighbors():
            dependent_tasks.add(neighbor)
    independent_tasks = set(all_tasks).difference(dependent_tasks)
    return independent_tasks


def build_order(start, g, ordered_list):
    start.color = 'grey'
    for neighbor in start.get_all_neighbors():
        neighbor = g.get_vertex(neighbor)
        if neighbor.color == 'white':
            ordered_list = build_order(neighbor, g, ordered_list)
    ordered_list.append(start.id)
    return ordered_list


def submit_task(task):
    running_queue.add(task)
    print "Processing task: " + str(task)
    time.sleep(1)
    print "Finished task: " + str(task)


def on_task_done(task):
    running_queue.remove(task)
    done_queue.add(task)


def schedule_next():
    runnable = True
    next_task = ordered_tasks[-1]
    dependencies = get_dependencies(next_task)

    for d in dependencies:
        if d not in done_queue:
            runnable = False
            print "Waiting for " + str(d) + " to complete.."
            return runnable

    if runnable:
        ordered_tasks.remove(next_task)
        submit_task(next_task)
        pool.apply_async(submit_task, next_task, on_task_done(next_task))
        return runnable


tasks = [
    (1, ()),
    (2, (1, )),
    (3, ()),
    (4, (1, 3, 5, 6)),
    (5, ()),
    (6, ()),
    (7, (2,)),
    (8, (7, 4)),
    (9, (8, )),
    (10, (5, 13)),
    (11, (10, )),
    (12, (6, )),
    (13, (12, )),
]

tasks = [
    (1, (2, 5)),
    (2, ()),
    (3, (2,)),
    (4, (1,)),
    (5, (3,))
]

g = build_graph(tasks)
starting_points = get_starting_points(g)
ordered_tasks = []
for start in starting_points:
    start = g.get_vertex(start)
    start.color = 'grey'
    ordered_tasks = build_order(start, g, ordered_tasks)

running_queue = set()
done_queue = set()
executor_capacity = 5
pool = Pool(processes=executor_capacity)

while ordered_tasks:
    if len(running_queue) < executor_capacity:
        if not schedule_next():
            time.sleep(1)
    else:
        print "Executor is full. Waiting for it to get free"
