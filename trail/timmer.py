

import time
 
count_seconds = 4
for i in reversed(range(count_seconds)):
    if i > 0:
        print(i, end='>>>')
        # print(count_seconds)
        time.sleep(2)
    else:
        print('Start')

for x in range(2, 30, 3):
    print(x)