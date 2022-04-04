# Question 1
# Given two rectangles described by their top-right and bottom-left coordinates, return true if they intersect and false if they do not. Assume the inputs will always be valid

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, bottomRight: Point, topLeft: Point):
        self.topLeft = topLeft
        self.bottomRight = bottomRight
        self.topRight = Point(bottomRight.x,topLeft.y)
        self.bottomLeft = Point(topLeft.x,bottomRight.y)

def doRectanglesOverlap(rectOne: Rectangle, rectTwo: Rectangle) -> bool:
    return pointInsideRectangle(rectOne,rectTwo.bottomLeft) or pointInsideRectangle(rectOne,rectTwo.bottomRight) or pointInsideRectangle(rectOne,rectTwo.topLeft) or pointInsideRectangle(rectOne,rectTwo.topRight)

def pointInsideRectangle(rectangle, point):
    if rectangle.bottomLeft.x <= point.x and rectangle.topRight.x >= point.x :
        if rectangle.bottomLeft.y <= point.y and rectangle.topRight.y >= point.y :
            return True
    else:
        return False


rect1 = Rectangle(Point(206, 70), Point(44, 166))
rect2 = Rectangle(Point(329, 115), Point(138, 227))

overlap1 = doRectanglesOverlap(rect1, rect2)
assert(overlap1 == True), "Should overlap"

rect3 = Rectangle(Point(468, 51), Point(348, 118))
rect4 = Rectangle(Point(453, 151), Point(365, 227))
overlap2 = doRectanglesOverlap(rect3, rect4)
assert(overlap2 == False), "Should not overlap"

Question 2
Make a sorted array which is made only of prime numbers (numbers that can only be divided by 1 and itself) and print the nth number. n < 200. ex: n=0 would return 2

def getNthPrime(n: int) -> int:
    prime_numbers = [2]
    current_number = 3
    while len(prime_numbers) < n+1:
        if checkPrime(current_number) :
            prime_numbers.append(current_number)
        current_number += 1
    
    return prime_numbers[n] 

def checkPrime(n):
    for i in range(2,int((n/2)+1)):
        if n % i == 0:
            return False
    return True

prime1 = getNthPrime(8)
assert(prime1 == 23), "Should equal 23"

prime2 = getNthPrime(24)
assert(prime2 == 97), "Should equal 97"

Question 3
Get the third largest element from an array

def thirdLargestElement(elements: list[float]) -> float:
    elements.sort()
    return elements[-3]

list1 = [32, 44, 12, 38, 1, 0, -5, 12.0, 44]
thirdLargest1 = thirdLargestElement(list1)
assert(thirdLargest1 == 38), "Should equal 38"

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
thirdLargest2 = thirdLargestElement(list2)
assert(thirdLargest2 == 9), "Should equal 9"

# Question 4
# Get the frequency of each character in a string
# The return should be a string with the character followed by the number.
# For example the string `apple` should return ['a:1', 'p:2', 'l:1', 'e:1'], the order does not matter

def characterFrequency(someString: str) -> list:
    characters = {}
    expectedFrequency = []
    
    for i in someString:
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1
    
    for char, count in characters.items():
        answer = str(char)+':'+str(count)
        expectedFrequency.append(answer)

    return expectedFrequency


strChar1 = "apple"
charFreq1 = characterFrequency(strChar1)
expectedCharFreq1 = ['a:1', 'p:2', 'l:1', 'e:1']
assert(all(elem in charFreq1 for elem in expectedCharFreq1) and all(elem in expectedCharFreq1  for elem in charFreq1)), "Expected result should contain [" + ','.join(expectedCharFreq1) + "]"

strChar2 = "Hey whaddup!!!e!H!!h!"
charFreq2 = characterFrequency(strChar2)
expectedCharFreq2 = ['H:2', 'e:2', 'y:1',' :1', 'w:1', 'h:1', 'a:1', 'd:2', 'u:1', 'p:1', '!:7', 'h:1']
assert(all(elem in strChar2 for elem in expectedCharFreq2) and all(elem in expectedCharFreq2  for elem in strChar2)), "Expected result should contain [" + ','.join(expectedCharFreq2) + "]"