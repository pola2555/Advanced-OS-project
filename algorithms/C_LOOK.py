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

class C_LOOK_class:
    def __init__(self):
        # this is the constructor of the class.
        # ignore it for now.
       pass



    # add as many functions as you want here but don't change the name of the function below or what it returns or its parameters.
    
    
    
    
    def run(self, queue:list = None, head_start :int = None, head_previous:int = None):
        '''
        queue: list of integers.\n
        head_start: integer.\n
        head_previous: integer.\n
        '''
        '''
        queue example:
        [98, 183, 37, 122, 14, 124, 65, 67]
        sorted_queue example:
        [14, 37, 65, 67, 98, 122, 124, 183]
        this is not the solution of the queue example, it is just an example of the output.
        '''
        sorted_queue = []
        if head_start == None or head_previous == None:
            dir = np.random.choice([-1, 1])
        else:
            Dir =  1 if head_start - head_previous > 0  else -1
            if head_start - head_previous == 0:
                Dir = np.random.choice([-1, 1])
        while len(queue) < len(sorted_queue):
            # apply the algorithm 
            pass
        return sorted_queue



if __name__ == "__main__":
    # you can test your code here.

    queue = [98, 183, 37, 122, 14, 124, 65, 67]
    head_start = 53
    head_previous = 98
    num_of_frames = 3
    second_chance = C_LOOK_class()
    LOOK_queue = second_chance.run(queue, head_start, head_previous)
    print(LOOK_queue)