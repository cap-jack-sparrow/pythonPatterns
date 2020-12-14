# Numbers Pattern 1: using a for loop and range function
# 1  
# 2 2  
# 3 3 3  
# 4 4 4 4  
# 5 5 5 5 5

def pattern(pat):
    for i in range(pat):
        for j in range(i):
            print(i, end=' ')
        print(' ')
# pattern(7)


# Number Pattern 2: Half pyramid pattern with numbers
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

def pyramidHalf(pat):
    for i in range(pat):
        for j in range(i + 1):
            print(j + 1, end=' ')
        print(" ")
# pyramidHalf(7)


# Numbers Pattern 3: Inverted Pyramid pattern with numbers
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5

def pyramidInverted(pat):
    for i in range(pat):
        for j in range(pat - i):
            print(i + 1, end=' ')
        print(' ')
# pyramidInverted(5)



# Numbers Pattern 4: Inverted Pyramid pattern with same number
# 5 5 5 5 5 
# 5 5 5 5 
# 5 5 5 
# 5 5 
# 5

def invertedSamePyramid(pat):
    for i in range(pat):
        for j in range(pat - i):
            print('5', end='')
        print(' ')
# invertedSamePyramid(5)



# Numbers Pattern 5: Display descending order of number
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1


def descendingPyramid(pat):
    for i in range(pat):
        for j in range(pat - i):
            print(pat - i, end=' ')
        print(' ')
# descendingPyramid(5)



# Number Pattern 6: Inverted half pyramid pattern with number
# 0 1 2 3 4 5 
# 0 1 2 3 4 
# 0 1 2 3 
# 0 1 2 
# 0 1
# 0

def invertedPatternPyramid(pat):
    for i in range(pat):
        for j in range(pat - i):
            print(j, end=' ')
        print(' ')
# invertedPatternPyramid(5)


# Number Pattern 7: Display Reverse number pattern
# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1

def reversePyramid(pat):
    for i in range(pat):
        for j in range(i + 1, 0, -1):
            print(j, end=" ")
        print(' ')
# reversePyramid(5)


# Number Pattern 8: Double the number
#    1 
#    2    1 
#    4    2    1 
#    8    4    2    1 
#   16    8    4    2    1 
#   32   16    8    4    2    1 
#   64   32   16    8    4    2    1 
#  128   64   32   16    8    4    2    1

def reverseSqPyramid(pat):
    for i in range(pat):
        for j in range(i, -1, -1):
            print(2**j, end=' ')
        print(' ')
# reverseSqPyramid(8)



# Number Pattern 9
#    1 
#    1    2    1 
#    1    2    4    2   1 
#    1    2    4    8   4    2    1 
#    1    2    4    8   16   8    4   2    1 
#    1    2    4    8   16   32   16  8    4    2    1 
#    1    2    4    8   16   32   64  32   16   8    4    2    1 
#    1    2    4    8   16   32   64  128  64   32   16   8    4    2    1

def squarePyramid(pat):
    for i in range(pat):
        for j in range(i):
            print(2**j, end=' ')
            
        for k in range(i, -1, -1):
            print(2**k, end=' ')
        print(' ')
# squarePyramid(8)



# Number Pattern 10: Display 1 to 10 number in Pattern
# Example 1:
# 1 
# 2 3 4 
# 5 6 7 8 9

def numberPattern(rows):
    printer = 1
    for i in range(1, rows, 2):
        for j in range(i):
            print(printer, end=" ")
            printer += 1
        print()
# numberPattern(10)


# Example 2:
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10

def numberpattern(rows):
    printer = 1
    for i in range(rows):
        for j in range(i + 1):
            print(printer, end=" ")
            printer += 1
        print()
# numberpattern(9)



# Numbers Pattern 11: Reverse number from 10 to 1
# 1
# 3 2
# 6 5 4
# 10 9 8 7

def numpattern(rows):
    printer = 1
    for i in range(rows):
        for j in range(i + 1):
            print(printer, end=" ")
            printer += 1
        print()
# numpattern(4)




# Numbers Pattern 12: Even number pattern
# 10 
# 10 8 
# 10 8 6 
# 10 8 6 4 
# 10 8 6 4 2

def evenPattern(rows):
    printer = 10
    for i in range(1, rows):
        for j in range(i):
            print(printer, end='')
        printer = printer -2
        print()
# evenPattern(5)



# Numbers Pattern 13
#  This is produced by the -1.
# 1 
# 1 2 1 
# 1 2 3 2 1 
# 1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1

# 1 1 
# 1 2 2 1 
# 1 2 3 3 2 1
# 1 2 3 4 4 3 2 1
# 1 2 3 4 5 5 4 3 2 1

def somePattern(pat):
    for i in range(1, pat):
        for j in range(1, i + 1):
            print(j, end=' ')
    
        for k in range(i - 1, 0, -1):
            print(k, end=' ')
        print()
# somePattern(6)



# Numbers Pattern 14: Reverse number pattern
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

def reversePattern(pat):
    for i in range(1, pat):
        for j in range(pat - i, 0, -1):
            print(j, end=' ')
        print()
# reversePattern(5)



# Numbers Pattern 15
# 0  
# 0  1  
# 0  2  4  
# 0  3  6   9  
# 0  4  8   12  16  
# 0  5  10  15  20  25  
# 0  6  12  18  24  30  36

def squarePattern(pat):
    for i in range(0, pat):
        for j in range(0, i + 1):
            print(i * j, end=' ')
        print()
# squarePattern(7)



# NumBer pattern 16
# 1 2 3 4 5 
# 2 3 4 5 
# 3 4 5 
# 4 5 
# 5

def reverseNumPattern(pat):
    for i in range(pat, 0, -1):
        for j in range(1, i):
            print(j, end='')
        print()
# reverseNumPattern(5)



# Number pattern 17: Display men’s pant style pattern with numbers
# 5 4 3 2 1 1 2 3 4 5 

# 5 4 3 2     2 3 4 5 

# 5 4 3         3 4 5 

# 5 4             4 5 

# 5                 5

def manPantpattern(pat):
    for i in range(pat):
        for j in range(pat - i):
            print(j, end=' ')
        print(' ')

manPantpattern(5)


























# rows = 6
# for p in range(1):
#     for row in range(1, rows):
#         num = 1
#         for j in range(rows, 1, -1):
#             if j > row:
#                 print(" ", end=' ')
#             else:
#                 print('*', end=' ')
#                 num += 1
                
#         for k in range(10):
#             print('*', end=' ')
#         print("")

#     for s in range(1, 10):
#         print("* " * 15, end=' ')
#     print("")
    
    
    
    
#     for row in range(1, rows):
#         num = 1
#         for j in range(rows, 1, -1):
#             if j > row:
#                 print(" ", end=' ')
#             else:
#                 print('*', end=' ')
#                 num += 1
                
#         for k in range(10):
#             print('*', end=' ')
#         print("")

#     for s in range(1, 10):
#         print("* " * 15)
#     print()
        
