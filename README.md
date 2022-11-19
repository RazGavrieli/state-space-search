# state-space-search
This program uses a BFS search to find the fairest way to divided 'm' items to 'n' players, according to player's evaluation of the items. <br>
Each player has to rate each item, and all the evaluation have to be normilized between all the player. (The sum of evaluation points is the same for each player) <br>
<br>

## Examples
<br>
Example with 2 agents and 3 items <br>
Players: <br>
[Agent([11, 11, 55]),Agent([22, 22, 33])] 
 <br>
<img width="480" alt="image" src="https://user-images.githubusercontent.com/90526270/202851038-ef9ba7f1-7276-4db9-859f-27601f7e7b98.png">
<br>
Example with 3 agents and 3 items <br>
Players: <br>
[Agent([11, 11, 55]),Agent([22, 22, 33]),Agent([33, 44, 0])] 
 <br>
<img width="474" alt="image" src="https://user-images.githubusercontent.com/90526270/202851233-cd11a392-f55a-441d-8304-9aff2437d0b0.png">
<br>
Example with 3 agents and 6 items <br>
players: <br>
[Agent([11, 11, 55, 30, 42, 50]),Agent([22, 22, 33, 122, 0 ,0]),Agent([33, 44, 0, 50, 70, 2])] 
 <br>
<img width="474" alt="image" src="https://user-images.githubusercontent.com/90526270/202851344-121b415e-4aee-4662-88f7-945686c633cc.png">
<br>
Example with 6 agents and 6 items <br>
players: <br>
[Agent([11, 11, 55, 30, 42, 50]),Agent([22, 22, 33, 122, 0 ,0]),Agent([33, 44, 0, 50, 70, 2]),Agent([33, 44, 0, 50, 70, 2]),Agent([33, 44, 0, 50, 70, 2]),Agent([18, 44, 15, 50, 70, 2])]
<img width="475" alt="image" src="https://user-images.githubusercontent.com/90526270/202852881-0d65edbd-4a53-4ea8-83cf-3fea3dcd3ebb.png">
