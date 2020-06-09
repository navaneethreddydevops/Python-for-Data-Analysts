#!/usr/bin/python3

import pandas
import datetime
import os 
import logging
import boto3

path=os.getcwd()
workdir="/Users/navaneethreddy/Documents/Code/"

def get_current_directory():
    try:
        print("This the current directory of code :" + path + ".")
    except:
        print("Not able to get the current working directory")
        
def change_directory():
    try:
        print("Changing to working directory :" + os.chdir(workdir) +".")
    except:
        print("Not able to change to working directory defined")
        
if __name__ == "__main__":
    change_directory()
    get_current_directory()