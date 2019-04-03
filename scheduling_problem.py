'''
was given as an interview question at atlassian
Given a string pattern of integers mixed with ? (if unknown)
day = max hours to work per day
hour = desired hours to work for the week
return a list of possible work assignments 
problem(8hours/day,56/week,"???8???")
   would return 88888888 as the only element in array 
'''

#My solution uses backtracking and is not optimal
answer = []
def construct_candidates(pos,partial,day,tot):
    candidates = []
    min_val = 0
    if partial[pos]=='?':
        current_sum = 0
        for i in range(pos):
            current_sum = current_sum + int(partial[i])
            if i== pos-1:
                min_val = int(partial[i])
        if tot-current_sum>day:
            n = day
        else:
            n = tot-current_sum
        for i in range(min_val,n+1):
            candidates.append(i)

    return candidates


def is_solution(a,total):
    cur_sum = 0
    if '?' in a:
        return False
    for i in a:
        cur_sum = cur_sum + int(i)
    #print(cur_sum)
    if cur_sum == total:
        return True
    else:
        return False
    
def sum_good(a,pos,day,total):
    tot = 0
    for i in range(pos+1):
        tot+= int(a[i])
        
    if tot > total:
        return False
    elif (total-tot)/(len(a)-pos+1)>day:

        return False
    return True
        
def backtrack(a,pos,day,total):
    print(a)
    if(is_solution(a,total)):
        answer.append(a)
    elif not pos==len(a):
        candidates = construct_candidates(pos,a,day,total)
        ncand = len(candidates)
        if(ncand==0):
            #kth position letter was not ?
            backtrack(a,pos+1,day,total)
        for i in range(ncand):
            m = sum_good(a,pos-1,day,total)
            if m:
                s = list(a)
                s[pos] = str(candidates[i])
                a = "".join(s)
                #print(a)
                if sum_good(a,pos,day,total):
                    backtrack(a,pos+1,day,total)
            
def problem(total,day,pattern):
    backtrack(pattern,0,day,total)
    print(answer)
    
problem(12,5,"???")
