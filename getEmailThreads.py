email_dict = {}
def getEmailThreads(emails):
    thread_num = 1
    result = []
    for comma in emails:
        first = comma.find(",")+1
        second = comma[first:].find(",")+1
        text=comma[first+second:].strip()
        print(text)
        #text = email[2]
        index = text.rfind("---") #find last index
        print(index)
        if index>-1:
            text = text[index+3:]
            print("key: ")
            print(text)
            email_dict[text][1]+=1    #increment thread count
        else:
            #start a new thread
             #increment thread num
            email_dict[text]=[thread_num,1]
            thread_num += 1
        x =[]
        x.append(email_dict[text][0])
        x.append(email_dict[text][1])
        result.append(x)
    return result
        

        

r = getEmailThreads(['abc@gmail.com, x@gmail.com, hello x, how are you?',
                     'c@gmail.com, abc@gmail.com, did you take a look at the event?',
                     'x@gmail.com, abc@gmail.com, i am great. how are you?---hello x, how are you?'])
print(r)
