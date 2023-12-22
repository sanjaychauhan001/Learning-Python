print("namskar deviyon aur sajanoo main amitabh bachhan swagat karta hu apka kon banega carodpati me")
questions = ["what is 3+4",
         "what is 12*5","what is 15/3",
         "what is capital of maharashtra",
         "highest populated state in india?",
        "smallest state in india?",
        "Chemical formula for water is",
        "Look at this series: 7, 10, 8, 11, 9, 12, ... What number should come next?",
       "Which of the following is used in pencils?",
       "The gas usually filled in the electric bulb is",
       "Which of the following gods is also known as Gauri Nandan?",
       " Which of these terms can only be used for women?",
       "In which of these two sports is the term free hit used?",
       "In a circle, which of these is half of the diameter?",
       "Which of these is not a Dravidian language?",
       "In which of the following events will the fastest person win?"]

options = [[2,9,5,7,4],[45,2,60,65,3], [4,8,5,9,3], 
      ["andheri","mumbai","thane","bandra",2],
      ["utter pradesh","maharashtra","bihar","rajasthan",1],
      ["goa","sikkim","chennai","jamu kashmir",1],["NaAlO2","H2O","Al2O3","CaSiO3",2],
      [7,10,12,13,2],["Graphite","silicon","charcoal","phosphorous",1],
      ["carbon dioxide","oxygen","hydrogen","nitrogen",4],["Agni","Hanuman","Ganesha","shiv",3],
      ["Dirghaayu","Suhagan","Chiranjeevi","Sushil",2],
       ["Football, Squash","Badminton, Tennis","Badminton, Cricket","Hockey, Cricket",4],
      ["Area","Circumference","center","Radius",4],["Tamil","Karnataka", "Malyalam", "Assamese",4],
     ["Marathon","Diving","Weightlifting","Shot Put",1]]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,
         320000,640000,1250000,2500000,5000000,"1 Crore","7 Crore"]
money =0
for i in range(0, len(options)):
    question = options[i]
    print(f"\nquestion for RS. {levels[i]} on your screen")
    print(questions[i])
    print(f"a.  {question[0]}       b.  {question[1]}")
    print(f"c.  {question[2]}       d.  {question[3]}")
    reply = int(input("enter your ans (1-4) or 0 to quit :"))
    if(reply == 0):
        money = levels[i-1]
        break
    elif(reply == question[-1]):
        print(f"correct answer you have won {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000              
    else:
        print("wrong answer!")     
        break

print(f"you can go home with the money of {levels[i]}")
if(money >=320000):
  dhanRashi = input("kya kroge itni dhanrashi ka :")
  print("achha hai jao maje karo")