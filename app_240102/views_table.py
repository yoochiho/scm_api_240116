import pandas as pd
from django.shortcuts import render
import pymysql
from sqlalchemy import create_engine
from app_240102.test_sql import call_query


def load_data(request):
                
        df = call_query("SELECT * from boosters_items")

        return render(request, 'table_template.html',{'df':df})

