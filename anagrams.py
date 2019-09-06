
#
# Complete the 'funWithAnagrams' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY s as parameter.
#

def funWithAnagrams(s):
    # Write your code here
    sorted_chars = []
    result = []
    ret = []
    for word in s:
        sorted_chars.append("".join(sorted(word)))
    #sorted_chars=set(sorted_chars)
    sorted_chars = list(set(sorted_chars))

    print(sorted_chars)
    if(len(sorted_chars)==1):
        print(s)
        return s[0]
    
    for i in range(len(sorted_chars)-1):
        for j in range(i+1,len(sorted_chars)):
            
            if(sorted_chars[i]==sorted_chars[j]):
                #if(s[i]<s[j]):
                result.append(i)

                #elif(s[i]>s[j]):
                 #   result.append(j)
                  #  found =1
            print("result",result)

    
    for w in result:
        ret.append(s[w])
    return sorted(ret)


r = funWithAnagrams(['code','aaagmnrs','anagrams','doce'])
#p = funWithAnagrams(['poke','pkoe','okpe','ekop'])

#print(p)
print(r)
