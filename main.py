# testing random, numpy for variance
import numpy as numpy
import random

# IMPORTANT: LIST STARTS FROM 0.
# if upperLimit is 100, there are 101 values
upperLimit = 99
repetition = 10000
counterList = [0]*(upperLimit+1)

# count frequency
for i in range(repetition):
    counterList[random.randint(0, upperLimit)] += 1


def printer(info, number):
    print('{:13s}'.format(info), number)


# print information
printer("Range:", str(min(counterList)) + " ~ " + str(max(counterList)))
printer("Delta:", max(counterList) - min(counterList))
printer("Theoretical:", str(sum(counterList)/len(counterList)/100)+"%")
printer("Variance:", numpy.var(counterList))
