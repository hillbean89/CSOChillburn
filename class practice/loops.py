def main():
    again='y'
    i=0
    while(True):
        for i in range(10):
            print(f"You are on game # (i)")
            print("would you like to pay again or skip the rest")
            again=input()
            i%=2
            if (again== 'y'):
        
        else:
            print("exiting")
            break
    else:
        print("youve played all 10 games")


()