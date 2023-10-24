

import io

dummyFile= io.StringIO()
print("hello dummyFile !!", file=dummyFile)
print(dummyFile.getvalue())

Testfile = io.StringIO()
print('Welcome to GeeksforGeeks Python world.!!', file=open('Testfile.txt', 'w'))




print("hello last")