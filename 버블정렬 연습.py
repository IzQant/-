import sys
def bubble(important):
    for i in range(len(important)):
        for j in range(len(important)-1-i):
            if important[j] > important[j+1]:
                important[j], important[j+1] = important[j+1], important[j]

