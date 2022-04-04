# # Question 1: Rectangle Intersection

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# class Rectangle:  # 1. write out the point needed
#     def __init__(self, topRight: Point, bottomLeft: Point):
#         self.topRight = topRight
#         self.bottomLeft = bottomLeft
#         self.topLeft = Point(bottomLeft.x, topRight.y)
#         self.bottomRight = Point(topRight.x, bottomLeft.y)


# def doRectanglesOverlap(rectOne: Rectangle, rectTwo: Rectangle) -> bool:
#     return pointInsideRectangle(rectOne, rectTwo.bottomLeft) or pointInsideRectangle(rectOne, rectTwo.bottomRight) or pointInsideRectangle(rectOne, rectTwo.topLeft) or pointInsideRectangle(rectOne, rectTwo.topRight)


# # 2. write a conditional statement to check
# def pointInsideRectangle(rectangle, point):
#     if rectangle.bottomLeft.x <= point.x and rectangle.bottomRight.x >= point.x:
#         if rectangle.topLeft.y <= point.y and rectangle.bottomLeft.y >= point.y:
#             return True
#     return False


# rect1 = Rectangle(Point(206, 70), Point(44, 166))
# rect2 = Rectangle(Point(329, 115), Point(138, 227))

# overlap1 = doRectanglesOverlap(rect1, rect2)
# assert(overlap1 == True), "Should overlap"

# rect3 = Rectangle(Point(468, 51), Point(348, 118))
# rect4 = Rectangle(Point(453, 151), Point(365, 227))
# overlap2 = doRectanglesOverlap(rect3, rect4)
# assert(overlap2 == False), "Should not overlap"

# Question2: Make a sorted array which is made only of prime number and print the nth number
# number that can only be divided by 1
# n < 200


# def getNthPrime(n: int) -> int:
#     prime_numbers = [2] # add a new list
#     current_number = 3
#     while len(prime_numbers) < n + 1:
#         #check whether is prime nubmer
#         if checkPrimeNumber(current_number): # if True
#             prime_numbers.append(current_number) #append into prime_numbers
#         current_number+=1
#     return prime_numbers[n]

# # 1. check the prime number

# def checkPrimeNumber(n):#这个loop会启动很多次
#     for i in range(2, int((n/2)+1)):  # if n = 0 will return 2 so I start from 2
#         if n % i == 0:
#             return False
#     return True #only check current number


# prime1 = getNthPrime(8)
# assert(prime1 == 23), "Should equal 23"

# prime2 = getNthPrime(24)
# assert(prime2 == 97), "Should equal 97"


# Question 3 Get the third largest element for an array

# def thirdLargestElement(elements: list[float]) -> float:
#     elements.sort()
#     return elements[-3]

# list1 = [32, 44, 12, 38, 1, 0, -5, 12.0, 44]
# thirdLargest1 = thirdLargestElement(list1)
# assert(thirdLargest1 == 38), "Should equal 38"

# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# thirdLargest2 = thirdLargestElement(list2)
# assert(thirdLargest2 == 9), "Should equal 9"

# Question 4
# Get the frequency of each character in a string
# The return should be a string with the character followed by the number.
# For example the string `apple` should return ['a:1', 'p:2', 'l:1', 'e:1'], the order does not matter

def characterFrequency(someString: str) -> list:
    characters = {}
    expectedFrequency = []
    #Step 1
    for i in someString: # Take out 1 by 1
        if i in characters: # Compare whether 有出现过还是没有
            characters[i] += 1 # 那个key的value加一个
        else:
            characters[i] = 1 #if not key = 1

    for char, count in characters.items():
            answer = str(char) + ":" + str(count) #combime
            expectedFrequency.append(answer)

    return expectedFrequency 

strChar1 = "apple"
charFreq1 = characterFrequency(strChar1)
expectedCharFreq1 = ['a:1', 'p:2', 'l:1', 'e:1']
assert(all(elem in charFreq1 for elem in expectedCharFreq1) and all(elem in expectedCharFreq1 for elem in charFreq1)
       ), "Expected result should contain [" + ','.join(expectedCharFreq1) + "]"

strChar2 = "Hey whaddup!!!e!H!!h!"
charFreq2 = characterFrequency(strChar2)
expectedCharFreq2 = ['H:2', 'e:2', 'y:1', ' :1', 'w:1',
                     'h:2', 'a:1', 'd:2', 'u:1', 'p:1', '!:7']
assert(all(elem in strChar2 for elem in expectedCharFreq2) and all(elem in expectedCharFreq2 for elem in strChar2)
       ), "Expected result should contain [" + ','.join(expectedCharFreq2) + "]"
