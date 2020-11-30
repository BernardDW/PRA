def clock(pages, invoer):

    pointer = 0

    queue = [0,1,2,3]
    r = [1,1,1,1]
    lyn1 = ""
    lyn2 = ""
    lyn3 = ""
    lyn4 = ""
    for x in invoer:
        #hit
        if(x in pages):
            indexOfPages = pages.index(x)
            indexOfQueue = queue.index(indexOfPages)
            if (r[indexOfQueue] == 0):
                r[indexOfQueue] = 1
                lyn1 += str(pages[0])+" | "
                lyn2 += str(pages[1])+" | "
                lyn3 += str(pages[2])+" | "
                lyn4 += str(pages[3])+" | "
                # print(pages)
            else:
                # print(pages)
                lyn1 += str(pages[0])+" | "
                lyn2 += str(pages[1])+" | "
                lyn3 += str(pages[2])+" | "
                lyn4 += str(pages[3])+" | "
        #fault  
        else:
            if(r[0] == r[1] == r[2] == r[3] == 1):
                r = [0,0,0,0]
            if(r[pointer] == 0):
                pages[queue[pointer]] = x
                r[pointer] = 1
                if (pointer == 0):
                    pointer = 3
                else:
                    pointer -= 1
                # print(pages)
                lyn1 += str(pages[0])+" | "
                lyn2 += str(pages[1])+" | "
                lyn3 += str(pages[2])+" | "
                lyn4 += str(pages[3])+" | "
            else:
                
                while(r[pointer]==1):
                    r[pointer] = 0
                    if (pointer == 0):
                        pointer = 3
                    else:
                        pointer -= 1
                pages[queue[pointer]] = x
                r[pointer] = 1
                if (pointer == 0):
                    pointer = 3
                else:
                    pointer -= 1
                # print(pages)
                lyn1 += str(pages[0])+" | "
                lyn2 += str(pages[1])+" | "
                lyn3 += str(pages[2])+" | "
                lyn4 += str(pages[3])+" | "

    strInvoer = ""
    streep = ""
    for i in invoer:
        strInvoer += str(i)+" | "
        streep += "----"
    print(strInvoer)
    print(streep)
    print(lyn1 +"\n"+ lyn2 +"\n"+ lyn3 +"\n"+ lyn4)


def secondChance(pages, queue, invoer):
    r = [1,1,1,1]
    lyn1 = ""
    lyn2 = ""
    lyn3 = ""
    lyn4 = ""
    for x in invoer:
        #hit
        if(x in pages):
            indexOfPages = pages.index(x)
            indexOfQueue = queue.index(indexOfPages)
            if (r[indexOfQueue] == 0):
                r[indexOfQueue] = 1
                #print(pages)
                lyn1 += str(pages[0])+" | "
                lyn2 += str(pages[1])+" | "
                lyn3 += str(pages[2])+" | "
                lyn4 += str(pages[3])+" | "
            else:
                #print(pages)
                lyn1 += str(pages[0])+" | "
                lyn2 += str(pages[1])+" | "
                lyn3 += str(pages[2])+" | "
                lyn4 += str(pages[3])+" | "
        #fault  
        else:
            if(r[0] == r[1] == r[2] == r[3] == 1):
                r = [0,0,0,0]
            if(r[0] == 0):
                pages[queue[0]] = x
                r.pop(0)
                r.append(1)
                temp = queue[0]
                queue.pop(0)
                queue.append(temp)
                #print(pages)
                lyn1 += str(pages[0])+" | "
                lyn2 += str(pages[1])+" | "
                lyn3 += str(pages[2])+" | "
                lyn4 += str(pages[3])+" | "
            else:
                while(r[0]==1):
                    r.pop(0)
                    r.append(0)
                    temp = queue[0]
                    queue.pop(0)
                    queue.append(temp)
                pages[queue[0]] = x
                r.pop(0)
                r.append(1)
                temp = queue[0]
                queue.pop(0)
                queue.append(temp)
                #print(pages)
                lyn1 += str(pages[0])+" | "
                lyn2 += str(pages[1])+" | "
                lyn3 += str(pages[2])+" | "
                lyn4 += str(pages[3])+" | "

    strInvoer = ""
    streep = ""
    for i in invoer:
        strInvoer += str(i)+" | "
        streep += "----"
    print(strInvoer)
    print(streep)
    print(lyn1 +"\n"+ lyn2 +"\n"+ lyn3 +"\n"+ lyn4)
    

def fifo(pages,queue, invoer):
    lyn1 = ""
    lyn2 = ""
    lyn3 = ""
    lyn4 = ""
    for x in invoer:
        #hit
        if(x in pages):
            
            lyn1 += str(pages[0])+" | "
            lyn2 += str(pages[1])+" | "
            lyn3 += str(pages[2])+" | "
            lyn4 += str(pages[3])+" | "

        #fault  
        else:
            
            pages[queue[0]] = x
            temp = queue[0]
            queue.pop(0)
            queue.append(temp)
            #print(pages)
            lyn1 += str(pages[0])+" | "
            lyn2 += str(pages[1])+" | "
            lyn3 += str(pages[2])+" | "
            lyn4 += str(pages[3])+" | "
            

    strInvoer = ""
    streep = ""
    for i in invoer:
        strInvoer += str(i)+" | "
        streep += "----"
    print(strInvoer)
    print(streep)
    print(lyn1 +"\n"+ lyn2 +"\n"+ lyn3 +"\n"+ lyn4)


def lru(pages,queue, invoer):

    lyn1 = ""
    lyn2 = ""
    lyn3 = ""
    lyn4 = ""
    for x in invoer:
        #hit
        if(x in pages):
            indexOfPages = pages.index(x)
            indexOfQueue = queue.index(indexOfPages)
            temp = queue[indexOfQueue]
            queue.pop(indexOfQueue)
            queue.append(temp)

            lyn1 += str(pages[0])+" | "
            lyn2 += str(pages[1])+" | "
            lyn3 += str(pages[2])+" | "
            lyn4 += str(pages[3])+" | "

        #fault  
        else:
            
            pages[queue[0]] = x
            temp = queue[0]
            queue.pop(0)
            queue.append(temp)
            #print(pages)
            lyn1 += str(pages[0])+" | "
            lyn2 += str(pages[1])+" | "
            lyn3 += str(pages[2])+" | "
            lyn4 += str(pages[3])+" | "
            

    strInvoer = ""
    streep = ""
    for i in invoer:
        strInvoer += str(i)+" | "
        streep += "----"
    print(strInvoer)
    print(streep)
    print(lyn1 +"\n"+ lyn2 +"\n"+ lyn3 +"\n"+ lyn4)

  
# Driver code 
if __name__ =="__main__": 

    # For optimal go to: https://solver.assistedcoding.eu/page_replacement 

    # How to use:

    # If table looks like this:
        # Frame   | Load time | Page in frame
        # Frame 3 |     11    |     5
        # Frame 2 |     8     |     8
        # Frame 1 |     3     |     1
        # Frame 0 |     14    |     4

    # Then your queue and pages would look like this:
        # queue = [2,1,0,3]       (The queue looks like this because we handle the frames as an array from top to bottom. Don't get confused with frame names)
        # pages = [5, 8, 1, 4]
        # sampleInput = [9,7,8,3,5,7,7,9,6,3,3,7,9,7,4,6,7,8,3,2,5,4,7,6,4,2,3,4,3,2,7,7]
    
    # Call the algorithm you want output of like this:
        # secondChance(pages, queue, sampleInput)
        # clock(pages, sampleInput)
        # fifo(pages, queue, sampleInput)
        # lru(pages, queue, sampleInput)

    queue = [2,1,0,3]
    pages = [5, 8, 1, 4]
    sampleInput = [9,7,8,3,5,7,7,9,6,3,3,7,9,7,4,6,7,8,3,2,5,4,7,6,4,2,3,4,3,2,7,7]

    secondChance(pages, queue, sampleInput)