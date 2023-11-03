from os import *

from sys import *

from collections import *

from math import *

 

def coverageOfMatrix(mat):

    coverage = 0

    rows = len(mat)

    cols = len(mat[0])

    

    for i in range(rows):

        for j in range(cols):

            if mat[i][j] == 0:

                if j > 0 and mat[i][j - 1] == 1:

                    coverage += 1

            # Check right

                if j < cols - 1 and mat[i][j + 1] == 1:

                    coverage += 1

                # Check up

                if i > 0 and mat[i - 1][j] == 1:

                    coverage += 1

                # Check down

                if i < rows - 1 and mat[i + 1][j] == 1:

                    coverage += 1

 

    return coverage

    pass