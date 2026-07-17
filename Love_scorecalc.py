def calculate_love_score(name1, name2):
    
    name1= name1.upper()
    name2= name2.upper()
    
    length1= len(name1)
    scoreL1=0
    scoreL=0
    
    length2= len(name2)
    scoreL2=0
    scoreN=0
    
    for L1 in range(length1):
        if name1[L1]=='T' or name1[L1]=='R' or name1[L1]=='U' or name1[L1]=='E':
            scoreL1+=1

    for L2 in range(length2):
        if name2[L2]=='T' or name2[L2]=='R' or name2[L2]=='U' or name2[L2]=='E':
            scoreL2+=1

        
    score= scoreL1+scoreL2
        
    for n1 in range(length1):
        if name1[n1]=='L' or name1[n1]=='O' or name1[n1]=='V' or name1[n1]=='E':
            scoreL+=1
    
    for n2 in range(length2):
        if name2[n2]=='L' or name2[n2]=='O' or name2[n2]=='V' or name2[n2]=='E':
            scoreN+=1
    
    scoreF= scoreL+ scoreN
    
    love_score= str(score)+str(scoreF)
    print(love_score)

player1= input("Enter your name: ")
player2= input("Enter your name: ")
    
calculate_love_score(player1, player2)