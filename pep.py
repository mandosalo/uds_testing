# import sys, os  # 1 unused imports

# from typing import *  #2 2spaces befor any function


# def Calculate_VehicleSpeed(distance, time, unit="mph"):  # 3 Name of function, no space around "=",  after a comma
#     """Calculate speed"""
#     Speed = distance / time       # 4 space around =
#     result = Speed if unit == "mph" else Speed * 1.60934  # 4 space around = and == , 5 format line 
#     return result


# x = Calculate_VehicleSpeed(100, 2)
# print("Speed: %s" % x)


import sys,os
from typing import *
def Calculate_VehicleSpeed( distance,time,unit = "mph" ):
    """Calculate speed"""
    Speed=distance/time;result= Speed if unit=="mph" else Speed*1.60934
    return result

x=Calculate_VehicleSpeed(100,2)
print( "Speed: %s"%x )


