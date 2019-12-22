import sys
#Creates a star pattern with user entered number of rows
[print(' '*(int(sys.argv[1])-x-1)+'*'*(2*x+1) ) for x in range(int(sys.argv[1]))]

