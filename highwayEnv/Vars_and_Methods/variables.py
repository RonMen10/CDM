import random

""" 
    Variables of the environment:
"""
# Simulation Frequency Hz
SIMULATION_FREQUENCY = 15

# inter arrival time of ego vehicles
time_difference = 40

# number of other cars in roundabout north
num_other_cars_north = 10

# number of cars in roundabout south
num_other_cars_south = 10

# number of ego vehicles
num_ego_vehicles = 10

# roundabout radius
raradius = 30

# roundabout centers
center_south = [0, 0]
center_north = [0, -210]

""" 
    Variables of the agents:
"""
# GLobal Counter
globalCounter = 0

# Starting position
START_POS = ("start", "east", 0)  # ("mid", "nxr",0)
X = random.randint(0, 50)       # 50
Y = random.randint(-35, 35)        # 0
#generates a pseudo random number,, where is this being used the X and Y?

# Actions of the vehicles
ACTIONS = {0: 'IDLE',
           1: 'FASTER',
           2: 'SLOWER',
           3: 'STOP'}

# communication radius
com_radius = 70

# Vehicles Max Velocity
MAX_VELOCITY = 16
""" Maximum reachable velocity [m/s] """


# Exchange probability
exchange_probability = 1

# Mutation probability and relevant distribution variance
mutation_probability = 0.5
sigma = 0.1

# tolerances for PO fronts
risk_tol = 0.1
threshold_tol = 0.05
hv_tol = 0.1

# risk mutation bounds
upper_risk_bound = 1
lower_risk_bound = 0.0000001 #1x10^-(7)

# UCB variables
UCB_FACTOR = 60

# Crash penalty
CRASH_PENALTY = 100

# Termination criterion: Number of entries in the roundabout
test_terminal = 50
training_terminal = 50

# Path for storing results
path = '/Users/ronald/Documents/MASTER_DE/3th_Semester/ArtificialDecisionMaking /CDM-master/cdm_project/test'