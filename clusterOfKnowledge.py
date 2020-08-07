import pickle
import numpy as np
import random

from highwayEnv.Vars_and_Methods import variables
import pandas as pd

pickle_in = open(variables.path + "/Archives/0.05_0.05_0.05_0.05.pkl", "rb")
example_dict = pickle.load(pickle_in)



def findCenter(id):
    sumHyperVolume = 0
    sumFirstRisk = 0
    count = 0
    for i in range(0, len(example_dict['id'])):
        if int(example_dict['id'][i]) == id:
            sumHyperVolume += float(example_dict['hypervolume'][i])
            sumFirstRisk += float(example_dict['first_risk'][i])
            count += 1
    centerFirstRisk = sumFirstRisk / count
    centerHyperVolume = sumHyperVolume / count
    center = [centerHyperVolume, centerFirstRisk]
    return center


def findFardest(id1, id2):
    "exchange from the id2 to the id1"
    center = findCenter(id1)
    stateList = []
    distanceList = []
    index = 0
    for i in range(0, len(example_dict['id'])):
        if int(example_dict['id'][i]) == id2:
            distance = np.sqrt((center[1] - example_dict['first_risk'][i])**2+(center[0] - example_dict['hypervolume'][i])**2)
            stateList.append([distance,
                              example_dict['hypervolume'][i],
                              example_dict['first_risk'][i],
                              example_dict['counter'][i],
                              example_dict['threshold'][i],
                              example_dict['cumWaitTime'][i],
                              example_dict['cumCrashes'][i],
                              example_dict['avgFitness'][i],
                              example_dict['time_nd'][i],
                              example_dict['risk_nd'][i],
                              example_dict['case'][i],
                              example_dict['id'][i]])
    for i in range(0, len(stateList), 1):
        distanceList.append(stateList[i][0])
        index = distanceList.index(max(distanceList))
        fardestState = stateList[index]
        print(distanceList)
    return fardestState


def findClosest(id):
    "Distances between each and every point inside a cluster. Returns matrix of distances"
    array3D = []
    distanceList = []
    newDictionary = statesById2(id=id, dictionary=example_dict)
    for i in range(0, len(newDictionary['id'])):
        distanceCompareList = []
        for j in range(0, len(newDictionary['id'])):
            dataList = []
            if newDictionary['first_risk'][i] == newDictionary['first_risk'][j] and newDictionary['hypervolume'][i] == newDictionary['hypervolume'][j]:
                distance = 1000
            else:
                distance = np.sqrt((newDictionary['first_risk'][i] - newDictionary['first_risk'][j])**2+(newDictionary['hypervolume'][i] - newDictionary['hypervolume'][j])**2)

            dataList = [distance, newDictionary['hypervolume'][i], newDictionary['first_risk'][i], newDictionary['hypervolume'][j], newDictionary['first_risk'][j]]
            distanceList.append(distance)
            distanceCompareList.append(dataList)

        array3D.append(distanceCompareList)

    print(distanceList)
    minDistance = min(distanceList)

    for i in range(0, len(newDictionary['id'])):
        for j in range(0, len(newDictionary['id'])):
            if minDistance == array3D[i][j][0]:
                hypervolume1 = array3D[i][j][1]
                first_risk1 = array3D[i][j][2]
                hypervolume2 = array3D[i][j][3]
                first_risk2 = array3D[i][j][4]
                break

    state1 = findBy(hypervolume1, first_risk1, newDictionary)
    state2 = findBy(hypervolume2, first_risk2, newDictionary)
   

    return state1


def statesById2(id, dictionary):
    dictionaryById = {'hypervolume': [], 'first_risk': [], 'counter': [], 'threshold': [], 'cumWaitTime': [],
           'cumCrashes': [], 'avgFitness': [], 'time_nd': [], 'risk_nd': [], 'case': [], 'id': []}

    for i in range(0, len(dictionary['id'])):
        if int(example_dict['id'][i]) == id:
            dictionaryById['hypervolume'].append(dictionary['hypervolume'][i])
            dictionaryById['first_risk'].append(dictionary['first_risk'][i])
            dictionaryById['counter'].append(dictionary['counter'][i])
            dictionaryById['threshold'].append(dictionary['threshold'][i])
            dictionaryById['cumWaitTime'].append(dictionary['cumWaitTime'][i])
            dictionaryById['cumCrashes'].append(dictionary['cumCrashes'][i])
            dictionaryById['avgFitness'].append(dictionary['avgFitness'][i])
            dictionaryById['time_nd'].append(dictionary['time_nd'][i])
            dictionaryById['risk_nd'].append(dictionary['risk_nd'][i])
            dictionaryById['case'].append(dictionary['case'][i])
            dictionaryById['id'].append(dictionary['id'][i])
    return dictionaryById



def findBy(hypervolume, first_risk, dictionary):
    itemsList = []
    for i in range(0, len(dictionary['id'])):
        if float(dictionary['hypervolume'][i]) == hypervolume and float(dictionary['first_risk'][i]) == first_risk:
            itemsList.append(dictionary['hypervolume'][i])
            itemsList.append(dictionary['first_risk'][i])
            itemsList.append(dictionary['counter'][i])
            itemsList.append(dictionary['threshold'][i])
            itemsList.append(dictionary['cumWaitTime'][i])
            itemsList.append(dictionary['cumCrashes'][i])
            itemsList.append(dictionary['avgFitness'][i])
            itemsList.append(dictionary['time_nd'][i])
            itemsList.append(dictionary['risk_nd'][i])
            itemsList.append(dictionary['case'][i])
            itemsList.append(dictionary['id'][i])
    return itemsList


def infoExchange(dictionary):
    listOfCarIDs = []
    #if car in area:
        #listOfCarIDs.append(int(example_dict['id']))
    listOfCarIDs.append(3)
    listOfCarIDs.append(9)
    listOfCarIDs.append(5)
    listOfCarIDs.append(0)

    id1 = random.choice(listOfCarIDs)
    listOfCarIDs.remove(id1)
    id2 = random.choice(listOfCarIDs)
    incomingState = findFardest(id1, id2)
    outgoingState = findClosest(id1)
    index_list = []
    for i in range(0, len(dictionary['id'])):
        if dictionary['hypervolume'][i] == outgoingState[0] and dictionary['first_risk'][i] == outgoingState[1] and dictionary['id'][i] == outgoingState[10]:
            dictionary['hypervolume'][i] = incomingState[0]
            dictionary['first_risk'][i] = incomingState[1]
            dictionary['counter'][i] = incomingState[2]
            dictionary['threshold'][i] = incomingState[3]
            dictionary['cumWaitTime'][i] = incomingState[4]
            dictionary['cumCrashes'][i] = incomingState[5]
            dictionary['avgFitness'][i] = incomingState[6]
            dictionary['time_nd'][i] = incomingState[7]
            dictionary['risk_nd'][i] = incomingState[8]
            dictionary['case'][i] = incomingState[9]
            dictionary['id'][i] = incomingState[10]
    return dictionary

def _is_terminal(self, dictionary):
     #print(self.total_attempts)
    if (self.total_attempts >= variables.training_terminal):
        pickle.dump(dictionary.get_archive(), open(variables.path + '/Archives/{0}_{1}_{2}_{3}.pkl'.format(self.risk_tol, self.threshold_tol, self.hv_tol, self.sigma), 'wb'))
        print(dictionary.get_archive())
        (pd.DataFrame(self.number_of_entries)).to_csv(variables.path + '/TrainingStatistics/convStatesOverTime_{0}_{1}_{2}_{3}.csv'.format(
            self.risk_tol, self.threshold_tol, self.hv_tol, self.sigma), index=None, header=True)
        (pd.DataFrame([self.steps])).to_csv(variables.path + '/TrainingStatistics/steps_{0}_{1}_{2}_{3}.csv'.format(
            self.risk_tol, self.threshold_tol, self.hv_tol, self.sigma), index=None, header=True)
        return True


your_list = [[[1,2,3],[4,5,6]], [[0,1,2],[3,4,5]], [[2,3,4],[5,6,7]]]
#print(min(c for (a,b,c),(d,e,f) in your_list))


print(infoExchange(example_dict))