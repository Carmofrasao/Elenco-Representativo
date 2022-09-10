#!/usr/bin/python3

from random import randint

l, m, n = input().split(" ")

print(f"{l} {m} {n}")
for i in range(0, int(m)):
    gNum = randint(1, int(l))

    value = randint(9, gNum*10)
    groups = set()

    while len(groups) != gNum:
        groups.add(randint(1, int(l)))
    
    print(f"{value} {gNum}")
    for group in groups:
        print(group)