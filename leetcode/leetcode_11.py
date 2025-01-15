def maxArea(height):
    total_set = []
    for i in range(0, len(height) - 1):
        area_set = []
        distance = 1
        for j in range(i + 1, len(height)):
            pivot = min(height[i], height[j])
            area = pivot * distance
            area_set.append(area)
            distance = distance + 1
        max_area = max(area_set)
        total_set.append(max_area)
    area = max(total_set)
    return area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))


def maxArea2(height):
    max_area = 0
    for i in range(0, len(height) - 1):
        distance = 1
        for j in range(i + 1, len(height)):
            pivot = min(height[i], height[j])
            area = pivot * distance
            if area > max_area:
                max_area = area
            distance = distance + 1
    return max_area


print(maxArea2([1, 8, 6, 2, 5, 4, 8, 3, 7]))


def maxArea3(height):
    max_area = 0
    for i in range(0, len(height) - 1):
        for j in range(len(height) - 1, i, -1):
            distance = j - i
            pivot = min(height[i], height[j])
            area = pivot * distance
            if area > max_area:
                max_area = area

            if all(element <= max(height[i], height[j]) for element in height[i:j+1]):
                break
    return max_area

print(maxArea3([1,1]))



list1 = [1, 2, 3, 4, 5, 6, 7]
print(list1[3:5])
inte = 9
result = all(element < inte for element in list1)
print(result)

