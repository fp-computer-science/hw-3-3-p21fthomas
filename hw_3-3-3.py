numOfFreeThrows = input("Number of 1 point Baskets? ")
numOf2PointBaskets = input("Number of 2 point Baskets? ")
numOf3PointBaskets = input("Number of 3 point Basskets? ")

totalFreeThrow = float(numOfFreeThrows) * 1
totalBasket3pointLine = float(numOf2PointBaskets) * 2
totalBasketOver3PointLine = float(numOf3PointBaskets) * 3

finalplayerScore = totalFreeThrow + totalBasket3pointLine + totalBasketOver3PointLine
print("The player scored" ,finalScore, "points in the game.")