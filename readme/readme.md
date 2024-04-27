**Algorithms description**

**LRU:**

![](readme/Aspose.Words.93caed6f-8eee-45d3-9396-b1d4e69ac92d.001.png)

LRU class will receive the pages as follows:

- A list of pages sorted by their arrival time.
- Each item (cell) in the list is a dictionary.
- The dictionary contains “arrival time” and the page “name”:

  Dictionary structure:

  {

  `	`“name”: None,

  `	`“arrival time”: None,

  }

LRU will also receive another parameter which is the number of frames, EX:- 3 frames: ![ref1]  which means 3 empty cells.



LRU should return one List:

![ref2]

- Each item (cell) in the list is a dictionary.
- The dictionary must carry:
1) Name which is the name of the page coming.
1) List of page names.
1) Hit is a boolean indicating if there is a change in the frames or not.

   Dictionary structure:

   {

   `	`“Name”: None,

   `	`“pages”: None,

   `	`“Hit”: False

   }

- The pages in the dictionary are the list of frames and it should be of length “number of frames” ![ref1].

Algorithm description (steps):

- LRU will start with empty frames.
- It will loop on the pages.
- If the page is already in the current frames, it will copy the frames list, add it to the dictionary, and turn the hit bool to false.
- If the page is not in the current frames it finds the least recently used (LRU) page and replaces it, then copies the frame to the list and turns the hit bool to true.
- Append everything to the memory list.



memory = []

frames = [] # current frames

for page in pages:

`	`temp = {“name” : page,  “pages” : None,  “Hit” : False}

`	`if page in frames:

`		`temp[“Hit”] = False

`	`else:

`		`replacement\_index = # Find the Least recently used page in your current frames

`		`frames[replacement\_index] = page

`		`temp[“Hit”] = True

`	`temp[“pages”] = copy.deepcopy(frames)

`	`memory.append(temp)









**Second chance:**

![](Aspose.Words.93caed6f-8eee-45d3-9396-b1d4e69ac92d.004.png)

![](Aspose.Words.93caed6f-8eee-45d3-9396-b1d4e69ac92d.005.png)



The second chance class will receive the pages as follows:

- A list of pages sorted by their arrival time.
- Each item (cell) in the list is a dictionary.
- The dictionary contains “arrival time” and the page “name”:

  Dictionary structure:

  {

  `	`“name”: None,

  `	`“arrival time”: None,

  }

Second chance will also receive another parameter which is the number of frames, EX:- 3 frames: ![ref1]  which means 3 empty cells.

Second chance should return one List:

![ref2]

- Each item (cell) in the list is a dictionary.
- The dictionary must carry:
1) Name which is the name of the page coming.
1) List of page names.
1) Hit is a boolean indicating if there is a change in the frames or not.

   Dictionary structure:

   {

   `	`“Name”: None,

   `	`“pages”: None,

   `	`“Hit”: False

   }

- The pages in the dictionary are the list of frames and it should be of length “number of frames” ![ref1].



Algorithm description (steps):

- Second will start with empty frames.
- It will loop on the pages.
- If the page is already in the current frames, it will copy the frames list, add it to the dictionary, and turn the hit bool to false.
- If the page is not in the current frames
  - it finds the page to be replaced and replaces it. 
  - then copies the frame to the list and turns the hit bool to true.
  - Then it updates the reference bit in the history.
- Append everything to the memory list.

memory = []

frames = [] # current frames

history = [] # first in first out with a reference bit

for page in pages:

`	`temp = {“name” : page,  “pages” : None,  “Hit” : False}

`	`if page in frames:

`		`temp[“Hit”] = False

`	`else:

`		`replacement\_index = # Find the bit to be replaced

`		`#update history

`		`frames[replacement\_index] = page

`		`temp[“Hit”] = True

`	`temp[“pages”] = copy.deepcopy(frames)

`	`memory.append(temp)

note :
history list would be like this:-

[{“name”: 7,  “refrence\_bit”: 0},

{“name”: 1,  “refrence\_bit”: 1}, … 

]

**LOOK:**

There are no direct slides for the LOOK but LOOK is just like the SCAN with a difference.

![](Aspose.Words.93caed6f-8eee-45d3-9396-b1d4e69ac92d.006.png)

![](Aspose.Words.93caed6f-8eee-45d3-9396-b1d4e69ac92d.007.png)

<a name="_hlk165146113"></a>It will not go to **ZERO** or **199** unless they are on the list. In other words:

![ref3]



- LOOK will receive: 
  - a list of integers representing the disk locations (name of the list: queue).
  - An integer representing where is the place of the head right now (name of the variable: head\_start).
  - An integer representing where is the place of the head before (name of the variable: head\_previous).
- It should return the list sorted by the LOOK algorithm that indicates the path of the head.

Algorithm description:

import numpy as np

head\_start = 143

head\_previous = 125

queue = […]

sorted\_queue = []

if head\_start == None or head\_previous == None:

`    `dir = np.random.choice([-1, 1])

else:

`    `Dir =  1 if head\_start - head\_previous > 0  else -1

`    `if head\_start - head\_previous == 0:

`        `Dir = np.random.choice([-1, 1])

while len(queue) < len(sorted\_queue):

`     `# apply the algorithm 

return sorted\_queue





**C-LOOK:**

Same as LOOK but:

![](Aspose.Words.93caed6f-8eee-45d3-9396-b1d4e69ac92d.009.png)

![](Aspose.Words.93caed6f-8eee-45d3-9396-b1d4e69ac92d.010.png)

It will not go to **ZERO** or **199** unless they are on the list. In other words:

![ref3]

Take a look on the LOOK if you need more knowledge 

- LOOK will receive: 
  - a list of integers representing the disk locations (name of the list: queue).
  - An integer representing where is the place of the head right now (name of the variable: head\_start).
  - An integer representing where is the place of the head before (name of the variable: head\_previous).
- It should return the list sorted by the LOOK algorithm that indicates the path of the head.

Algorithm description:

import numpy as np

head\_start = 143

head\_previous = 125

queue = […]

sorted\_queue = []

if head\_start == None or head\_previous == None:

`    `dir = np.random.choice([-1, 1])

else:

`    `Dir =  1 if head\_start - head\_previous > 0  else -1

`    `if head\_start - head\_previous == 0:

`        `Dir = np.random.choice([-1, 1])

while len(queue) < len(sorted\_queue):

`     `# apply the algorithm 

return sorted\_queue


[ref1]: Aspose.Words.93caed6f-8eee-45d3-9396-b1d4e69ac92d.002.png
[ref2]: Aspose.Words.93caed6f-8eee-45d3-9396-b1d4e69ac92d.003.png
[ref3]: Aspose.Words.93caed6f-8eee-45d3-9396-b1d4e69ac92d.008.png
