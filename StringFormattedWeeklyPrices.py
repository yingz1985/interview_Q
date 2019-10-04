
#for goldman sachs
#find two decimal average of 7 elements starting from beginning of index
#could be more efficient - rn i'm summing redundant values..
def stringFormattedWeeklyPrices(dailyPrice):
    result = []
    elements_now = dailyPrice[:7] #first 7 elements
    for index in range(6,len(dailyPrice)):
        result.append(findAverage(elements_now))
        if(index>=len(dailyPrice)-1):
            break
        elements_now= elements_now[1:]+[dailyPrice[index+1]]

    return result

def findAverage(elements):
    total = 0
    for i in elements:
        total+=i

    return '{:0.2f}'.format(total/7)


    
print(stringFormattedWeeklyPrices([1,1,1,1,1,1,1,1]))

