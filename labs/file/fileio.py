"""
File I/O Lab
By: Colin Hillburn


CSCI 110
Date: 4/9/2024


Program prompts user to enter name of the file that contains 10 integers.
It opens, reads and stores the numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
Program will then print the sorted lists to an output file along with the 
largest and smallest values in the list.


NOTE: All fixme's are each worth 10 points except for the FIXME1 which is worth 20 points
"""
import pathlib
my_path=pathlib.Path(__file__).parent.resolve()
#filename = f"{my_path}/numbers.txt"


totalInts = 10




def readData():
    intList = []
    filename=input("Enter Input Filename: ")
    filename=f"{my_path}/{filename}"
    with open (filename) as fin:
        
        while(True):
            line = (fin.readline())
            line = line.strip()


            if line == '':
                break
            
            intList.append(int(line))


        
    return intList


        
    # FIXME1 (20 points):
    # Prompt user to input file name
    # open the file; read each number one line at a time;
    # and store it into intList list
    # close the file
    # return the intList




def sortListInAscendingOrder(lstInts):
    # FIXME2
    # sort lstInts list in ascending order
    lstInts.sort()


    return lstInts




def sortListInDescendingOrder(lstInts):
    lstInts.sort(reverse=True)
    #lstInts.append()
    # FIXME3
    # sort lstInts in descending order
    return lstInts




def printList(printFile, lstInts):
    for i in lstInts:
        # FIXME4
        # write each value one line at a time to file
        # handled by printFile object.
        printFile.write(f"{i}\n")
    printFile.write('\n')


def main():
    
    integers = []  # list to store integers
    integers = readData()
    outputFileName = input('Enter a file to write output to: ')
    printFile = open(outputFileName, 'w')
    printFile.write("Numbers entered:\n")
    printList(printFile, integers)
    # sort numbers
    sortListInAscendingOrder(integers)
    printFile.write("Numbers sorted in ascending order:\n")
    printList(printFile, integers)


    # FIXME5
    # Call sortListInDescendingOrder function
    
    sortListInDescendingOrder(integers)
    printFile.write("Numbers in Decending order:\n")
    printList(printFile, integers)


    # FIXME6
    # Write the sorted list in descending order to the output file


    # FIXME7
    printFile.write(f"largest number of inputed set: {max(integers)}\n")
    
    # Print the largest number to the output file
    


    # FIXME8
    # Print the smallest number to the output file
    printFile.write(f"smallest number of inputed set: {min(integers)}\n" )



    printFile.close()
    print('Done executing the program! Check the output file for results.')




# FIXME9
# Call main function if this module is run as the main module
if __name__ == "__main__":
    main()
    