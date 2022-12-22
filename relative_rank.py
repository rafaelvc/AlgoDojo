# https://leetcode.com/problems/relative-ranks


def find_relative(arr):
    result_sorted = sorted(arr, reverse=True)
    if len(arr) > 0:
        arr [ arr.index(result_sorted[0]) ] = "Gold Medal"
    if len(arr) > 1:
        arr [ arr.index(result_sorted[1]) ] = "Silver Medal"
    if len(arr) > 2:
        arr [ arr.index(result_sorted[2]) ] = "Bronze Medal"
    if len(arr) > 3:
        pos = 4
        while pos <= len(arr):
            arr[ arr.index(result_sorted[pos-1]) ] = str(pos)
            pos += 1
    return arr

arr = [5,1,2,10]
print (find_relative(arr))

arr = [5,4,3,2,1]
print (find_relative(arr))

arr = [10,3,8,9,4]
print (find_relative(arr))


class PriorQ(list):
    def __init__(self, myl=[]):
        super().__init__(myl)
        self.removed = 0
    def __delitem__(self, item): 
        self.removed += 1
        super().__delitem__(item)
        #del self[item] # creates infinity loop
        #del super()[item] # does not work as well
    def pop_next_max(self):
        if len(self) == 0:
            return
        maxv = -1
        for i in range(0, len(self)):
            if self[i] >= maxv:
                ixmax = i
                maxv = self[i]
        del self[ixmax]
        return self.removed + ixmax


def find_relative(arr):
    pqueue = PriorQ(arr.copy())
    pos = 1
    while len(pqueue) > 0:
        if pos == 1:
            arr[ pqueue.pop_next_max() ] = "Gold Medal"
        elif pos == 2:
            arr[ pqueue.pop_next_max() ] = "Silver Medal"
        elif pos == 3:
            arr[ pqueue.pop_next_max() ] = "Bronze Medal"
        else:
            arr[ pqueue.pop_next_max() ] = str(pos)
        pos += 1

def pop_next_max(pq):
    max_score = max(pq)
    pos = pq[max_score]
    del pq[max_score]
    return pos

def find_relative(arr):
    pqueue = {vl:i for i, vl in enumerate(arr)}
    pos = 1
    while len(pqueue) > 0:
        if pos == 1:
            arr[ pop_next_max(pqueue) ] = "Gold Medal"
        elif pos == 2:
            arr[ pop_next_max(pqueue) ] = "Silver Medal"
        elif pos == 3:
            arr[ pop_next_max(pqueue) ] = "Bronze Medal"
        else:
            arr[ pop_next_max(pqueue) ] = str(pos)
        pos += 1



# Very good from leet code:
def findRelativeRanks(score):
    scores = sorted ([[score[i],i] for i in range(len(score))], key=lambda x:x[0], reverse=True)
    
    #scores = sorted([(score[i],i) for i range(len(score))])
    
    positions = [None for i in range(len(score))]
    def getName(pos):
        if pos > 3:
            return str(pos)
        if pos == 1:
            return "Gold Medal"
        if pos == 2:
            return "Silver Medal"
        return "Bronze Medal"
    
    for i in range(len(scores)):
        _, index = scores[i]
        positions[index] = getName(i+1)
        
    return positions

