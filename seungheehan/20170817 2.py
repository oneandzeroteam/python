

list = [17, 92, 18, 33, 58, 7, 33, 43]


maximum = 0
for i in list:
    if maximum <= i:
        maximum = i
    else:
        maximum = maximum
print("The biggest number in the list is %i."%maximum)
