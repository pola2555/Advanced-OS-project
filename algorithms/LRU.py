import numpy as np # if you want to use it.
import copy # if you want to use it. in copying lists. using copy.deepcopy() method.
'''
copy.deepcopy() method is used to copy the list and its elements to a new list without referencing the original list.
usage:
    list1 = [1, 2, 3]
    list2 = copy.deepcopy(list1)
    list2.append(4)
    print(list1) # [1, 2, 3]
    print(list2) # [1, 2, 3, 4]
you can try it in a test file.
'''

class LRU_class:
    def __init__(self):
        # this is the constructor of the class.
        # ignore it for now.
       pass



    # add as many functions as you want here but don't change the name of the function below or what it returns or its parameters.
    
    
    
    
    def run(self, pages:list = None, num_of_frames:int = None):
        # don't delete the next comment but you can delete this line.
        '''
        pages: list of dictionaries.\n
        num_of_frames: integer.\n
        return: List of dictionaries.
        '''

        # you can remove the next comment 
        '''
        pages example:
        [
            {'name': '7', 'arrival_time': 0},
            {'name': '0', 'arrival_time': 1},
            {'name': '1', 'arrival_time': 2},
            {'name': '2', 'arrival_time': 3},
            {'name': '0', 'arrival_time': 4},
            {'name': '3', 'arrival_time': 5},
            {'name': '0', 'arrival_time': 6},
            {'name': '4', 'arrival_time': 7},
            {'name': '2', 'arrival_time': 8},
            {'name': '3', 'arrival_time': 9},
            {'name': '0', 'arrival_time': 10},
            {'name': '3', 'arrival_time': 11},
            {'name': '2', 'arrival_time': 12},
            {'name': '1', 'arrival_time': 13},
            {'name': '2', 'arrival_time': 14},
            {'name': '0', 'arrival_time': 15},
            {'name': '1', 'arrival_time': 16},
            {'name': '7', 'arrival_time': 17},
            {'name': '0', 'arrival_time': 18},
            {'name': '1', 'arrival_time': 19},
        ]
        '''
        if pages is None or num_of_frames is None:
            return None
        memory = []
        
        # you can remove the next comment 
        '''
        the hit is a boolean value that indicates if the frame has changed or not.
        example:
        if the num_of_frames is 3, then the frames will be like this:
        memory = [
        {'name' : 7, pages: [7], "Hit": True},
        {'name' : 0, pages: [7, 0], "Hit": True},
        {'name' : 1, pages: [7, 0, 1], "Hit": True},
        {'name' : 2, pages: [2, 0, 1], "Hit": True},
        {'name' : 0, pages: [2, 0, 1], "Hit":, False}  # 0 is already in the memory. so no change happened here.
        ]
        look at the example in the word file.
        '''
        ########################################################
        ########################################
        ######################
        # your code goes here.
        ######################
        ########################################
        ########################################################

        # don't delete the next line or change it. you can remove this one
        return memory

if __name__ == "__main__":
    # you can test your code here.

    pages = [
            {'name': '7', 'arrival_time': 0},
            {'name': '0', 'arrival_time': 1},
            {'name': '1', 'arrival_time': 2},
            {'name': '2', 'arrival_time': 3},
            {'name': '0', 'arrival_time': 4},
            {'name': '3', 'arrival_time': 5},
            {'name': '0', 'arrival_time': 6},
            {'name': '4', 'arrival_time': 7},
            {'name': '2', 'arrival_time': 8},
            {'name': '3', 'arrival_time': 9},
            {'name': '0', 'arrival_time': 10},
            {'name': '3', 'arrival_time': 11},
            {'name': '2', 'arrival_time': 12},
            {'name': '1', 'arrival_time': 13},
            {'name': '2', 'arrival_time': 14},
            {'name': '0', 'arrival_time': 15},
            {'name': '1', 'arrival_time': 16},
            {'name': '7', 'arrival_time': 17},
            {'name': '0', 'arrival_time': 18},
            {'name': '1', 'arrival_time': 19},
        ]
    num_of_frames = 3
    lru = LRU_class()
    memory = lru.run(pages=pages, num_of_frames=num_of_frames)
    for frame in memory:
        print(frame)