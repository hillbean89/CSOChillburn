newalpha = {
    "A": "@",
    "B": "8",
    "C": "(",
    "D": "|)",
    "E": "3",
    "F": "#",
    "G": "6",
    "H": "[-]",
    "I": "|",
    "J": "_|",
    "K": "|<",
    "L": "1",
    "M": "[]\\/[]",
    "N": "[]\\[]",
    "O": "0",
    "P": "|D",
    "Q": "(,)",
    "R": "|Z",
    "S": "$",
    "T": "']['",
    "U": "|_|",
    "V": "\\/",
    "W": "\\/\\/",
    "X": "}{",
    "Y": "`/",
    "Z": "2"
}


def alpha(select):
    o = ord(select)
    if 97 <= o <= 122:
        return newalpha[chr(o - 32)]
    if 65 <= o <= 90:
        return newalpha[select]
    return select


for i in input():
    print(alpha(i), end='')



def main():
    alpha
    test
    



def test():
    assert "A" == "@"
    assert "B" == "8"
    assert "D" == "|)"

 
 


if __name__=="__main__":
    main()