print("Welcome to ASCII Art Program...\n")
name = input("what is your name ")
print("Nice Meeting you %s!" %name )
semester: str= input ("What semester is this [Fall/Spring]? ")
print ("this is "  +semester+  " semester.\n ")
year: str = input ("what year is it? ")
print(" this is %s" %year)
print ("Hope you like my ASCII art... \n\n")
line1: str = "   |\_/|       *****************************     (\_/)\n"
print (line1)
line2: str = "  / @ @ \      *         ASCII Lab         S*    (='.'=)\n"
print (line2)
name= name.center(27)

line3: str = " ( > 0 < )     *%s*  "'( " )_( " )'"\n" %name 
print (line3)
syear= semester+" "+year
syear= syear.center(27)
line4: str = "   >>x<<       *%s*\n"%syear 
print (line4)
line5: str = "  /  O  \      *          CSCI 111         *\n"
print (line5)
line6: str = "               *****************************\n"
print (line6)
