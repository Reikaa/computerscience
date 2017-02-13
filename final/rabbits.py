import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    if CURRENTRABBITPOP > 10:    
        newrabbits = 0
        for i in range(CURRENTRABBITPOP):
            preproduce = 1.0-(CURRENTRABBITPOP/MAXRABBITPOP)
            if random.random() < preproduce:
                newrabbits +=1    
        CURRENTRABBITPOP += newrabbits
        if CURRENTRABBITPOP > MAXRABBITPOP:
            CURRENTRABBITPOP = MAXRABBITPOP
    
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    if CURRENTFOXPOP > 10:
        newfoxes = 0
        deadfoxes = 0
        for i in range(CURRENTFOXPOP):
            phunt = CURRENTRABBITPOP/MAXRABBITPOP
            if random.random() < phunt:
                if CURRENTRABBITPOP > 10: 
                    CURRENTRABBITPOP -= 1
                preproduce = 1/3
                if random.random() > preproduce:
                    newfoxes += 1
            else:
                pdie = 9/10
                if random.random() > pdie:
                    deadfoxes += 1
        CURRENTFOXPOP += newfoxes
        CURRENTFOXPOP -= deadfoxes       


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbits,foxes = [],[]
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbits.append(CURRENTRABBITPOP)
        foxes.append(CURRENTFOXPOP)
    
    pylab.plot(range(numSteps),rabbits)
    pylab.plot(range(numSteps),foxes)
    pylab.xlabel('time step')
    pylab.ylabel('population')
    pylab.legend(('rabbits','foxes'))
    pylab.show()    
    
    return (rabbits,foxes)
    
    
#results = runSimulation(200)
#coeffrabbit = pylab.polyfit(range(len(results[0])),results[0],2)
#pylab.plot(pylab.polyval(coeffrabbit, range(len(results[0]))))
#coefffox = pylab.polyfit(range(len(results[1])),results[1],2)
#pylab.plot(pylab.polyval(coefffox, range(len(results[1]))))