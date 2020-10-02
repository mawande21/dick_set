#converting num into number word
num = int(input("Please enter any number: "))
#own dict numbers because keys , words become values
num_words = {0:'zero',1:'one', 2:'two', 3:"three", 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight',9:'nine' }

for num in str(num): #how you change the num to a str 
    print(num_words[int(num)], end=" ") #end makes spaces in between

