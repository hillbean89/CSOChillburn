"""
File I/O Lab with Dictionary

Update By: Colin Hillburn

CSCI 110
Date: 20241604

Program finds the frequency of words in a given text document and print top 10 most
common words using dictionary and tuple data structures.
"""

def readText():
    """
    opens a file reads its contnets and
    creates a histogram of words based on frequency using dictionary data structure
    """
    fileOk = False
    fin = None
    hist = {}
    # stores data in this form: hist = {'and': 10, 'python':15}
    # where 'and' appears 10 times and
    # python appears 15 times
    while not fileOk:
        fileName = input('Enter input text file => ')
        try:
            fin = open(fileName, 'r')
            fileOk = True
        except Exception as ex:
            print('Exception occured: ', ex)

    lines = fin.readlines()
    for line in lines:
        line = line.strip().lower()
        words=[]
        if line:
            words=line.split()
            # FIXME3 #fixed
            # update words; split line into list of words and store the list into words object
            #words += line.split()
            for exword in words:
                hist[exword] = hist.get(exword , 0) +1
                   
                # FIXME4 #fixed
                # if word exists as key in hist dict, increment the value by 1
                # else add word as new key with value 1 in hist dict
                pass
         
    return hist


def reverseHistogramList(histDict):
    """
    given someDict,  returns list of tuples in descending order based
    frequency of each word in histDict
    """
    reverseList = []
    for key, val in histDict.items():
        reverseList.append((val, key))
        # FIXME5 #fixed
        # append tuple with values in (val, key) order into reverseList list

    reverseList.sort(reverse=True)
    # FIXME6 #fixed
    # Sort the list reverseList in reverse order
    return reverseList


def main():
    histogram = readText()
    # FIXME7 - Comment the following statement out when done#fixed
    #print(histogram)  # see the output to understand what's going on so far

    aList = reverseHistogramList(histogram)
    print("Top 10 words with highest frequencies:")
    for i in range(10):
        frequency, word = aList[i]
        print (f"{word}:{frequency} times")
    # FIXME8 – print top 10 words with highest frequencies stored in aList#fixed


if __name__ == "__main__":
    main()