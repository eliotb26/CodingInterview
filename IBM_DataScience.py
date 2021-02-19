#Predicting Temperature 


#Using Linear Regression, works
#In question, never says to use linear regression 

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'predictTemperature' function below.
#
# The function is expected to return a FLOAT_ARRAY.
# The function accepts following parameters:
#  1. STRING startDate
#  2. STRING endDate
#  3. FLOAT_ARRAY temperature
#  4. INTEGER n
#

from sklearn.linear_model import LinearRegression
import numpy as np

def predictTemperature(startDate, endDate, temperature, n):
    # Write your code here
    days = int(len(temperature)/24) 
    total_hours = [] 
    for num in range(1,24*days+1): 
        total_hours.append(num)   # [1, 2, 3, 4, ... total hours]
    lm = LinearRegression()
    lm.fit(np.asarray(total_hours).reshape(-1,1),temperature) #fits LM with temp
    
    future = total_hours[-1]+1
    fut_hours =[]
    for elem in range(24*n):
        fut_hours.append(future)
        future += 1 
    return(lm.predict(np.asarray(fut_hours).reshape(-1,1)).tolist()) 
        #predicts LM 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    startDate = input()

    endDate = input()

    temperature_count = int(input().strip())

    temperature = []

    for _ in range(temperature_count):
        temperature_item = float(input().strip())
        temperature.append(temperature_item)

    n = int(input().strip())

    result = predictTemperature(startDate, endDate, temperature, n)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

