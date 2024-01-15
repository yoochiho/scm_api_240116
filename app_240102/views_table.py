import os
import sys
sys.path.insert(0,os.path.dirname(os.path.dirname((os.path.dirname(os.path.abspath(__file__))))))
sys.path.insert(0,os.path.dirname(os.path.dirname((os.path.dirname(os.path.abspath(__file__)))))+'/autoinput')
import pandas as pd
from django.shortcuts import render
import pymysql
from sqlalchemy import create_engine
from autoinput import df_to_db
from autoinput import input


def crontab_scm(request):
        import autoinput.get_input_inf
