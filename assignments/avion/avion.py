"this program takes an 5 line input and returns if it is an FBI blimp and if so which line it is in"
def input_codes(): 
    blimps=[input() for _ in range(5)]
    return blimps







def I_AM_winning(blimps):
    fbi_blimp_indexes=[]
    for i in range(len(blimps)):
     if "FBI" in blimps[i]:
        fbi_blimp_indexes.append(str(i+1))
        if(fbi_blimp_indexes):
            ans=" ".join(fbi_blimp_indexes)
        return str(ans)

    if fbi_blimp_indexes:
        print(" ".join(fbi_blimp_indexes))
    else:
        print("HE GOT AWAY!")

def test():
    assert I_AM_winning(["A-FBI4", "9a","yhu","gh","dfasd"]) == str(1)
    assert I_AM_winning (["asdf", "adsfd", "FBI-4", "asdf", "asdfasdf"]) == str(3)
    assert I_AM_winning(['asdfasdf', 'defgasdf', 'ertgaFBI', 'asdfasd', 'sdfasdf'])== str(3)
    

def main():
   eye_in_the_skye=input_codes()
   results=I_AM_winning(eye_in_the_skye)
   print(results)

test()
main()
