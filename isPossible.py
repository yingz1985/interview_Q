#find if a subset of the set adds up to a certain number
def subs(l):
    if len(l) == 1:
        return [l]
    res = []
    subsets = subs(l[0:-1])
    res = res+subsets
    res.append([l[-1]])
    for sub in subsets:
        res.append(sub+[l[-1]])
    return res

def isPossible(calCounts,requiredCals):
    subsets = subs(calCounts)
    for a_set in subsets:
        temp_sum = 0
        for cal in a_set:
            if temp_sum < requiredCals:
                temp_sum+=cal
            else:
                break

        if temp_sum==requiredCals:
            return True

    return False
        
                

print(subs([1,2,3]))
print(isPossible([1,2,3],3))
