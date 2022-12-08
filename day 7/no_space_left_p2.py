import os
from pprint import pprint

class Dir():
    def __init__(self, name):
        self.name = name
        self.children = []

    def insert(self, node):
        self.children.append(node)

    def get_size(self):
        sum = 0
        for node in self.children:
            sum += node.get_size()

        return sum

    def __str__(self):
        contents = ''
        for node in self.children:
            contents += '\n  ' + str(node).replace('\n', '\n  ')

        return 'Dir<{}>{}'.format(self.name, contents)

    def __repr__(self):
        return f'Dir<{self.name}> {len(self.children)} items'

class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size
    
    def __str__(self):
        return f'File<{self.name}> {self.size}'

    def __repr__(self):
        return str(self)

with open('input.txt') as f:
    content = f.read().splitlines()


dir_nav_stack = []
filesystem = []
for line in content:
    if line.startswith('$ cd'):
        dirname = line[5:]
        # edge case for starting with nothing
        if len(filesystem) == 0:
            root = Dir(name=dirname)
            dir_nav_stack.append(root)
            filesystem.append(root)
        else:
            if dirname == '..':
                dir_nav_stack.pop()
                continue
            
            found_dir = False
            current_dir = dir_nav_stack[-1]
            for node in current_dir.children:
                if node.name == dirname:
                    dir_nav_stack.append(node)
                    found_dir = True
                    break

            if not found_dir:
                raise Exception(f'No such directory in {current_dir.name}: {dirname}')
    elif line.startswith('$ ls'):
        continue
    else:
        # collect this ls into the current dir:
        if line.startswith('dir'):
            dirname = line[4:]
            new_node = Dir(name=dirname)
        else:
            size, name = line.split(' ', 1)
            new_node = File(name=name, size=int(size))

        current_dir = dir_nav_stack[-1]
        current_dir.insert(new_node)

# print(filesystem[0])
# print()

all_dirs = []
def total_dir_sizes(parent_dir, sum):
    for node in parent_dir.children:
        if type(node) is Dir:
            dir_size = total_dir_sizes(node, 0)
            all_dirs.append((node.name, dir_size))
            sum += dir_size
        else:
            sum += node.size
    
    return sum

used_space = total_dir_sizes(filesystem[0], 0)

TOTAL_SPACE = 70_000_000
REQUIRED_SPACE = 30_000_000

free_space = TOTAL_SPACE - used_space
space_needed_to_free = REQUIRED_SPACE - free_space

size_of_smallest_possible_dir_to_delete = TOTAL_SPACE
for dir in all_dirs:
    if dir[1] >= space_needed_to_free:
        size_of_smallest_possible_dir_to_delete = min(dir[1], size_of_smallest_possible_dir_to_delete)

print(size_of_smallest_possible_dir_to_delete)
