def main():
    again='y'

    for i in range(10):
        print(f"You are on game # (i)")
        print("would you like to pay again or skip the rest")
        again=input()
        if (again=='y'):
            continue
        else:
            print("exiting")


()