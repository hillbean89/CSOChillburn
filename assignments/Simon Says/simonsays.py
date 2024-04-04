def main():
    for i in range(int(input())):
        command = input()
        if "Simon says" in command:
            print(command[11:])
            return

main()


assert main('Simon says hi') == "hi"
assert main('Simon says hello') == "hello"
assert main('Simon says bye') == "bye"
print ("All passed")