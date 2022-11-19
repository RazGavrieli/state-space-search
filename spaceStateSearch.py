from agent import Agent
from bfs import breadth_first_search
players = [Agent([11, 11, 55]),Agent([22, 22, 33]),Agent([33, 44, 0])]
results = []
iterations = 0
numOfItems = 3
def n_func(node):
    global iterations
    iterations += 1
    if node[0] == players[0].len():
        return ["end"]
    currItemIndex = node[0]

    listOfNeighnors = []
    for playerIndex, player in enumerate(players):
        currNei = [currItemIndex+1]
        for nodeIndex, i in enumerate(node[1:]):
            if playerIndex == nodeIndex:
                currNei.append(i+player.value(currItemIndex))
            else:
                currNei.append(i)
        listOfNeighnors.append(currNei)

    for i in listOfNeighnors:
        if i not in results:
            results.append(i)


    return listOfNeighnors

if __name__ == "__main__":
    res = breadth_first_search(start=[0,  0, 0, 0], end="end", neighbor_function=n_func)

    count = 0
    z=0
    maxMin = -1
    for i in results:
        currMin = 9999999
        if i[0] == numOfItems:
            count+=1
            print(i)
            for j in i[1:]:
                if j < currMin:
                    currMin = j
            if currMin > maxMin:
                maxMin = currMin
                z = i
                

    print(iterations, count, z)