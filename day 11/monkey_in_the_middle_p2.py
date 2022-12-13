from __future__ import annotations
import re
from typing import Literal

ROUNDS = 10_000
OP_REGEX = r"new\s=\sold\s([\*\+\-\/])\s(old|\d+)"

class Monkey:
    id: int
    items: list[int]
    operation: str
    operation_arg: Literal['old']|int
    divisor: int
    false_destination: int
    true_destination: int
    _inspection_counter = 0
    
    def __init__(self, id: int):
        self.id = id

    def apply_operation(self, item: int, all_devisors: int) -> int:
        arg = item if self.operation_arg == 'old' else self.operation_arg
        if self.operation == '+':
            result = item + arg
        elif self.operation == '*':
            result = item * arg
        else:
            raise TypeError(f'unknown operator: {self.operation}')

        return result % all_devisors

    def test(self, item: int) -> bool:
        return item % self.divisor == 0

    def catch_item(self, item: int):
        self.items.append(item)

    def inspect(self, all_monkeys: dict[int, Monkey], all_devisors: int):
        while (len(self.items)):
            self._inspection_counter += 1
            new_item = self.apply_operation(self.items.pop(0), all_devisors)
            if self.test(new_item):
                all_monkeys[self.true_destination].catch_item(new_item)
            else:
                all_monkeys[self.false_destination].catch_item(new_item)


monkeys: dict[int, Monkey] = {}

with open('input.txt') as f:
    monkey_notes = f.read().splitlines()
monkey_notes.append('') 

current_monkey = None
for note in monkey_notes:
    if note == '':
        note = ':'

    key, value = [n.strip() for n in note.split(':')]
    if key.startswith('Monkey'):
        # monkey ID
        _, monkey_id = key.split(' ')
        current_monkey = Monkey(id=int(monkey_id))
        continue
    else:
        assert current_monkey is not None

    if key == 'Starting items':
        items = [int(item) for item in value.split(', ')]
        current_monkey.items = items
    elif key == 'Operation':
        operation_match = re.finditer(OP_REGEX, value)
        op, val = next(operation_match).group(1,2)
        current_monkey.operation = op
        current_monkey.operation_arg = val if val == 'old' else int(val)
    elif key == 'Test':
        _, _, divsor = value.split(' ')
        current_monkey.divisor = int(divsor)
    elif key == 'If true':
        _, _, _, monkey_id = value.split(' ')
        current_monkey.true_destination = int(monkey_id)
    elif key == 'If false':
        _, _, _, monkey_id = value.split(' ')
        current_monkey.false_destination = int(monkey_id)
    else:
        # end of this monkey's notes
        monkeys[current_monkey.id] = current_monkey
        current_monkey = None

all_devisors = 1
for _, monkey in monkeys.items():
    all_devisors *= monkey.divisor

for _ in range(ROUNDS):
    for _, monkey in monkeys.items():
        monkey.inspect(all_monkeys=monkeys, all_devisors=all_devisors)

all_inspection_counts: list[int] = []
for _, monkey in monkeys.items():
    all_inspection_counts.append(monkey._inspection_counter)

all_inspection_counts.sort()
print(all_inspection_counts[-1] * all_inspection_counts[-2])