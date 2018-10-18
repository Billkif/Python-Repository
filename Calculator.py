#this program is to design a basic calculator

#I start by writing some screen specifications for a graphical display of at the beginning of execution

sentence = "Welcome to Bill Kif's calculator!" 

screen_width = 80

text_width   = len(sentence)

box_width    = text_width + 6

left_margin  = (screen_width - box_width) // 2

#graphical display of a welcome message to the person executing
print()
print(' ' * left_margin + '*'  + '-' * (box_width-4) +   '*')
print(' ' * left_margin + '# ' + '-' * text_width    +  ' #')
print(' ' * left_margin + '# ' +       sentence      +  ' #')
print(' ' * left_margin + '# ' + '-' * text_width    +  ' #')
print(' ' * left_margin + '*'  + '-' * (box_width-4) +   '*')

#including a loop sequence so as to permit another calculation
Off = 'o'
M = 0  #initialising the memory

while Off == 'o': #begining of loop
    print("\n")

    receive = input("Enter the your mathematical operation, use M to recall your last answer: ")

    result = eval(receive) #evaluate each value entered as a string and converts it to its equivalent type

    M = result #Updating memory

    print("Ans: ",result) #printing of result

    print("\n")

    Off = input("press any key to stop the program or 'o' to continue; ")  #condition for iteration

    if Off != 'o':
        print(' '*left_margin +"****** Thanks for using Bill Kif's calculator1 ******")
#end of loop
#end of program