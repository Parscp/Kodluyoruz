import math

print("Enter x1 and y1: ")
x1 = float(input())
y1 = float(input())

print("Enter x2 and y2: ")

x2 = float(input())
y2 = float(input())

first_point = [x1, y1]
second_point = [x2, y2]



def euclidean_distance(first_point, second_point):
    euclid_distance = math.sqrt((first_point[0] - second_point[0]) ** 2 + (first_point[1] - second_point[1]) ** 2)
    print("Euclidean distance is : " + str(euclid_distance))

euclidean_distance(first_point, second_point)