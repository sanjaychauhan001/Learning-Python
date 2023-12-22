# Python Quiz 
# Write a simple quiz in Python 

print("Let's take a quiz!\n") 
  
# dictionary containing question-answer 
quizdict = { "Q1: Which of the following is an example of a mutable datatype?" : ["A. List", "B. Tuple", "C. Integer", "D. Dictionary"], 
             "Q2: What type of loop is used when the number of iterations is known?" : ["A. While loop","B. For loop","C. Do-while loop","D. Nested loop"], 
             "Q3: Databases are used for which of the following purposes?" : ["A. Data storage and retrieval","B. Producing Output Reports","C. Preparing Graphs and Charts","D. All of the above"]}  
  
# list to store all correct choices   
anskey = ["A. List", 1, "B. For loop", 2, "D. All of the Above", 3] 
score = 0       # variable to store score  

     # iteration to print all questions one by one                                                        # option with respect to its position in dictionary's value list 
for ques, options in quizdict.items():        # four it will iterate 4 times as our dict contains 4 key-value pairs  
    print(ques,"\n")                      # print current question             
       # iteration to get options on current question one by one   
    for index, opt in enumerate(options):               # this will iterate four times (len(options))                    
        print(index + 1, opt)                    # here 'index' represent position of each option           

       # input from user depend upon number of option available with respect to its position
    ans = int(input("Choose correct answer (1/2/3/4):"))
    if [options[ans - 1], ans] in anskey:
        score += 1
        print("\nRight Answer :) \n\n")
    else:
        print("\nWrong Answer :( \n\n")
        print("Your Score is ", score)