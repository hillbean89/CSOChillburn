'''
Name: Colin Hillburn    
Date: 02/15/2024
Program Description: Kattis problem bijele:
https://open.kattis.com/problems/bijele
Algorithm Steps:
    Input 6 numbers separated by a space
    Set varibles for # pieces there are supposed to be
    Write 6 line, one for each set of pieces, 
        taking the difference between actual pieces and pieces required
'''

king, queen, rooks, bishops, knights, pawns = input().split()

king=int(king)
queen=int(queen)
rooks=int(rooks)
bishops=int(bishops)
knights=int(knights)
pawns=int(pawns)

req_king = 1
req_queen = 1
req_rooks = 2
req_bishops = 2
req_knights= 2
req_pawns= 8
# FIXMEs 3,4 make varibles for remaining pieces (2 knights, 8 pawns)
#fixed

dif1 = req_king-king
dif2 = req_queen-queen
dif4 = req_bishops-bishops
dif3 = req_rooks-rooks
dif5 = req_knights-knights
dif6= req_pawns-pawns

#FIXMEs 5,6: make dif5 and dif6 
#fixed added the dif5 and dif 6

#FIXME 7: make a function that prints the solution
def solution():

    print(dif1)
    print(dif2)
    print(dif3)
    print(dif4)
    print(dif5)
    print(dif6)

solution()



