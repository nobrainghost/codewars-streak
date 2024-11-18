'''
Description:
Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
Note: your solution must not modify the input list.
'''



def score(dice):
    #count each number 
    score_dict={}
    points=[]
    for i in dice:
        if i in score_dict:
            score_dict[i]+=1
        else:
            score_dict[i]=1
    for key,value in score_dict.items():
        if value>=3 and key==1:
            points.append(1000)
            value=value-3
            if value>=0:
                points.append(100*value)
        elif value<3 and key==1:
            points.append(100*value)
        if value>=3 and key==6:
            points.append(600)
            value=value-3
            if value>3:
                points.append(600)
        if value>=3 and key==5:
            points.append(500)
            value=value-3
            if value>0:
                points.append(50*value)
        elif value<3 and key==5:
            points.append(50*value)
        if value>=3 and key==4:
            points.append(400)
            value=value-3
            if value>3:
                points.append(400)
        if value>=3 and key==3:
            points.append(300)
            value=value-3
            if value>3:
                points.append(300)
        if value>=3 and key==2:
            points.append(200)
            value=value-3
            if value>3:
                points.append(200)
    return sum(points)
