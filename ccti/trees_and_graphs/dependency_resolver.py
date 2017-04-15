from sample_graph import create_graph


def dfs(start, g, count=0):
    if not start.visited:
        curr = start
        curr.visited = True
        curr.start_time = count
        count += 1
        for child in curr.get_all_neighbors():
            if child:
                child = g.get_vertex(child)
                new_count = dfs(child, g, count)
                if new_count:
                    count = new_count
        curr.end_time = count
        count += 1
        push_to_stack(curr.id)
        return count


def push_to_stack(obj, stack=[]):
    stack.append(obj)
    print stack


g = create_graph()
print g
independent_projects_set = set()
for start in ['f', 'd']:
    independent_projects_set.add(g.get_vertex(start))

count = 0
if len(independent_projects_set) == 0:
    print "No path"
else:
    for starting_point in independent_projects_set:
        print "Beginning DFS from: ", starting_point.id
        count = dfs(starting_point, g, count)