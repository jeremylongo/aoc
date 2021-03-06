import re


class node(object):
    id = None
    parents = None

    def __init__(self, id=None, parent=None):
        self.id = id
        self.parents = {}
        if parent is not None:
            parent.add(self)

    def add(self, child):
        child.parents[self.id] = self


tree = {}
elements = {}
root_node = node('root')


def add_dependency(parent, child):
    if parent not in elements:
        element = node(parent, None)
        elements[element.id] = element
        root_node.add(element)

    parent_node = elements[parent]

    if child not in elements:
        child_node = node(child, parent_node)
        elements[child] = child_node
    else:
        child_node = elements[child]
        parent_node.add(child_node)


data = """
Step Q must be finished before step I can begin.
Step B must be finished before step M can begin.
Step R must be finished before step F can begin.
Step G must be finished before step S can begin.
Step M must be finished before step A can begin.
Step Z must be finished before step W can begin.
Step J must be finished before step C can begin.
Step K must be finished before step O can begin.
Step C must be finished before step I can begin.
Step Y must be finished before step L can begin.
Step N must be finished before step P can begin.
Step S must be finished before step X can begin.
Step E must be finished before step U can begin.
Step U must be finished before step V can begin.
Step D must be finished before step F can begin.
Step W must be finished before step H can begin.
Step T must be finished before step I can begin.
Step H must be finished before step V can begin.
Step L must be finished before step O can begin.
Step P must be finished before step A can begin.
Step A must be finished before step I can begin.
Step F must be finished before step O can begin.
Step V must be finished before step X can begin.
Step I must be finished before step O can begin.
Step X must be finished before step O can begin.
Step F must be finished before step V can begin.
Step L must be finished before step P can begin.
Step Y must be finished before step P can begin.
Step Y must be finished before step X can begin.
Step Y must be finished before step O can begin.
Step D must be finished before step A can begin.
Step T must be finished before step F can begin.
Step W must be finished before step X can begin.
Step R must be finished before step A can begin.
Step E must be finished before step F can begin.
Step H must be finished before step I can begin.
Step K must be finished before step Y can begin.
Step W must be finished before step P can begin.
Step V must be finished before step O can begin.
Step N must be finished before step E can begin.
Step L must be finished before step I can begin.
Step B must be finished before step G can begin.
Step D must be finished before step T can begin.
Step J must be finished before step L can begin.
Step M must be finished before step Y can begin.
Step T must be finished before step A can begin.
Step K must be finished before step D can begin.
Step H must be finished before step P can begin.
Step P must be finished before step I can begin.
Step T must be finished before step L can begin.
Step J must be finished before step N can begin.
Step U must be finished before step F can begin.
Step U must be finished before step I can begin.
Step A must be finished before step F can begin.
Step U must be finished before step P can begin.
Step R must be finished before step H can begin.
Step G must be finished before step V can begin.
Step P must be finished before step F can begin.
Step B must be finished before step D can begin.
Step U must be finished before step X can begin.
Step K must be finished before step A can begin.
Step G must be finished before step D can begin.
Step N must be finished before step U can begin.
Step U must be finished before step L can begin.
Step M must be finished before step J can begin.
Step I must be finished before step X can begin.
Step H must be finished before step L can begin.
Step M must be finished before step S can begin.
Step E must be finished before step O can begin.
Step Q must be finished before step F can begin.
Step A must be finished before step O can begin.
Step T must be finished before step P can begin.
Step F must be finished before step X can begin.
Step D must be finished before step P can begin.
Step A must be finished before step X can begin.
Step G must be finished before step Z can begin.
Step W must be finished before step F can begin.
Step Q must be finished before step X can begin.
Step C must be finished before step V can begin.
Step L must be finished before step V can begin.
Step E must be finished before step L can begin.
Step B must be finished before step X can begin.
Step M must be finished before step V can begin.
Step F must be finished before step I can begin.
Step P must be finished before step X can begin.
Step C must be finished before step A can begin.
Step Z must be finished before step H can begin.
Step Q must be finished before step S can begin.
Step G must be finished before step X can begin.
Step T must be finished before step O can begin.
Step P must be finished before step O can begin.
Step T must be finished before step V can begin.
Step N must be finished before step V can begin.
Step Z must be finished before step X can begin.
Step L must be finished before step X can begin.
Step Z must be finished before step Y can begin.
Step N must be finished before step T can begin.
Step S must be finished before step T can begin.
Step G must be finished before step K can begin.
Step T must be finished before step X can begin.
Step R must be finished before step X can begin.
"""

# data = """
# Step C must be finished before step A can begin.
# Step C must be finished before step F can begin.
# Step A must be finished before step B can begin.
# Step A must be finished before step D can begin.
# Step B must be finished before step E can begin.
# Step D must be finished before step E can begin.
# Step F must be finished before step E can begin.
# """

for match in re.finditer(r"(?im)^Step (?P<parent>.*?) must be finished before step (?P<child>.*?) can begin\.$", data):
    add_dependency(match.group('parent'), match.group('child'))

root_node.id = ""
result = [root_node,]
while len(elements) > 0:
    for key in sorted(elements.keys()):
        element = elements[key]
        has_parents = True
        for parent_key, parent in element.parents.items():
            has_parents = has_parents and parent in result
        if has_parents:
            del(elements[key])
            result.append(element)
            break

print(''.join([element.id for element in result]))
