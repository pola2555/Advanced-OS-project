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

class LOOK_class:
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
            dir =  1 if head_start - head_previous > 0  else -1
            if head_start - head_previous == 0:
                dir = np.random.choice([-1, 1])
        current_head = head_start
        sorted_queue.append(current_head)
        while len(sorted_queue) < len(queue) +1:
            _min = float('inf')
            _max = -1
            for i in range(len(queue)):
                if dir == 1:
                    if queue[i] > current_head and queue[i] < _min and queue[i] not in sorted_queue:
                        _min = queue[i]
                else:
                    if queue[i] < current_head and queue[i] > _max and queue[i] not in sorted_queue:
                        _max = queue[i]
            if _min != float('inf'):
                current_head = _min
            if _max != -1:
                current_head = _max
            if _min != float('inf') or _max != -1:
                sorted_queue.append(current_head)
            else:
                dir *= -1
           
        
        
        return sorted_queue



if __name__ == "__main__":
    # you can test your code here.

    # queue = [98, 183, 37, 122, 14, 124, 65, 67]
    queue = [86, 1470, 913, 1774, 948, 1509, 1022, 1750, 130]
    import matplotlib.pyplot as plt
    head_start = 143
    head_previous = 125
    look = LOOK_class()
    LOOK_queue = look.run(queue, head_start, head_previous)
    
    
    plt.plot(LOOK_queue, range(len(LOOK_queue)))
    plt.yticks(range(len(LOOK_queue)), LOOK_queue)
    plt.ylabel('Time or Sequence')
    plt.xlabel('Cylinder Number')
    plt.title('Transition of the head from one cylinder to another')
    plt.show()
    print(LOOK_queue)