
import sys

def solution(command):
  if "Simon says" in command:
        results=(command[11:])
  else:
     results=""
  return results

def the_game():
 n=int(input())
 for i in range(n):
    command = input()
    print(solution(command))
        



def main():
 #bossy=input()
 the_game()

main()

assert solution("Simon says hi") == "hi"
assert solution('Simon says hello') == "hello"
assert solution('Simon says bye') == "bye"
print ("All passed", file=sys.stderr)