questions=["who is SRK?", "WWE","Actor","Plumber","Doctor",2],["What is capital of India?","MUMBAI","PUNE","BIHAR","DELHI",4],["What is the currency of India?","DOLLAR","RUPEE","POUND","EURO",2],["What is the national animal of India?","TIGER","LION","ELEPHANT","SNAIL",1],["What is the national bird of India?","PEACOCK","PARROT","CROW","PEACOCK",1],["What is the national flower of India?","LOTUS","ROSE","SUNFLOWER","LILY",1],["What is the national fruit of India?","MANGO","BANANA","APPLE","FIG",1],["What is the national tree of India?","BAOBAB TREE","MANGO TREE","BANYAN TREE","LOTUS TREE",3],["What is the national river of India?","GANGA RIVER","YAMUNA RIVER","BRAHMAPUTRA RIVER","MAHABALESHWAR RIVER",1],["What is the national sport of India?","CRICKET","HOCKEY","FOOTBALL","VOLLLY",2]

prizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
i = 0
for question in questions:
  
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    a = int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d: "))
    if(question[5] == a):
        print("Correct answer")
    else:
        print(f"Wrong answer. The correct answer is {question[5]}.")
        break
    
    print(f"You have won {prizes[i]} rupees.")
    i +=1

  
