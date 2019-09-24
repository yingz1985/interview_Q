
def solution(A, B):
    if(len(A)==0 or len(B)==0):
        return 0
    # write your code in Python 3.6
    try:
        x = min(findSwaps(A[0],B[0],A[1:],B[1:]),1+findSwaps(B[0],A[0],A[1:],B[1:]))
    except:
        x = -1
    return x

def findSwaps(headA,headB,tailA,tailB):
    if(len(tailA)==0 or len(tailB)==0):
        return 0
    else:
        if(headA==tailA[0] or headB==tailB[0]):
            #print(headA,tailA[0],"no swap necessary",headB,tailB[0])
            return min(0+findSwaps(tailA[0],tailB[0],tailA[1:],tailB[1:]),
            1+findSwaps(tailB[0],tailA[0],tailA[1:],tailB[1:]))
        elif(headA==tailB[0] or headB==tailA[0]):
            #print("swap needed",headA,tailB[0]," ",headB,tailA[0])
            return 1+findSwaps(tailB[0],tailA[0],tailA[1:],tailB[1:])
        else:
            raise Exception


print(solution([1, 2, 1, 2], [2, 6, 1, 2]))
print(solution([2,1,2,4,2,2],[5,2,6,2,3,2]))
print(solution([5,2,6,2,3,2],[2,1,2,4,2,2]))
