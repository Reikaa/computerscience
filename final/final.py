import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    same = 0
    numDraws = 3
    bucket = ['r','r','r','r','g','g','g','g']
    for t in range(numTrials):
        copy = bucket[:]
        balls = []        
        for d in range(numDraws):         
            balls.append(random.choice(copy))
            copy.remove(balls[-1])
        if all(x == balls[0] for x in balls):
            same += 1
    return same/numTrials
    

import pylab

def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a list of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axes
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values,bins=numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title is not None:
        pylab.title(title)
    pylab.show()


def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """
    longestList = []
    for t in range(numTrials):
        values = []
        run = 0
        longest = 0
        for r in range(numRolls):
            values.append(die.roll())
            if r == 0:
                run += 1
                longest = run
            else:
                if values[-1] == values[-2]:
                    run += 1
                else:
                    if run > longest:
                        longest = run
                    run = 1
        if run > longest:
            longest = run
        longestList.append(longest)
    makeHistogram(longestList, 10, 'Number of runs', 'Number of trials', title=None)    
    return round(sum(longestList)/float(len(longestList)),3) 


import itertools as it
import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    answer = [0]*len(choices)
    closest = 0
    combos = []
    for n in range(1,len(choices)+1):
        combos.extend(list(it.combinations(enumerate(choices),n)))
    for i in combos:
        tempsum = 0
        tempans = [0]*len(choices)
        for j in i:
            tempsum += j[1]
            tempans[j[0]] = 1
        if tempsum == total:
            closest = tempsum
            answer = tempans
            #print('yes: ',str(tempsum),str(tempans))
            return np.array(answer)
        elif tempsum < total and tempsum > closest:
            closest = tempsum
            answer = tempans
            #print('no: ',str(tempsum),str(tempans))
    return np.array(answer)
