from agent import Agent
from bfs import breadth_first_search

#players = [Agent([11, 11, 55, 30, 42, 50]),Agent([22, 22, 33, 122, 0 ,0]),Agent([33, 44, 0, 50, 70, 2]),Agent([33, 44, 0, 50, 70, 2]),Agent([33, 44, 0, 50, 70, 2]),Agent([18, 44, 15, 50, 70, 2])]
players = [Agent([11, 11, 55]),Agent([22, 22, 33]),Agent([33, 44, 0])]
results = {}
iterations = 0
numOfItems = players[0].len()

def n_func(node):
    global iterations
    iterations += 1
    if node[0] == players[0].len():
        return ["end"]
    currItemIndex = node[0]

    listOfNeighnors = []
    for playerIndex, player in enumerate(players):
        currNeighbor = [currItemIndex+1]
        for nodeIndex, i in enumerate(node[1:]):
            if playerIndex == nodeIndex:
                currNeighbor.append(i+player.value(currItemIndex))
            else:
                currNeighbor.append(i)
        listOfNeighnors.append(currNeighbor)

    for currNeighbor in listOfNeighnors:
        results[tuple(currNeighbor)] = currNeighbor
        #results.append(currNeighbor)


    return listOfNeighnors

if __name__ == "__main__":
    import timeit
    startTime = timeit.default_timer()

    start = [0]*(len(players)+1)
    res = breadth_first_search(start=start, end="end", neighbor_function=n_func)

    count = 0
    z=0
    maxMin = -1
    for i in results:
        currMin = 9999999
        if i[0] == numOfItems:
            count+=1
            for j in i[1:]:
                if j < currMin:
                    currMin = j
            if currMin > maxMin:
                maxMin = currMin
                z = i
    print("# of BFS | # of results | best result")
    print(iterations, "\t\t",count, "\t",z)

    stop = timeit.default_timer()

    print('Time: ', stop - startTime) 