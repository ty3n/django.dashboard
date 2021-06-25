# -*- coding: iso-8859-15 -*-
import pyodbc
import os,sys,time
import smtplib,traceback
import bz2,re
import socket#,cx_Oracle
import pandas as pd
from datetime import datetime, timedelta
#from svn_cmd import *

#serverU configuration
severU_ip = '127.0.0.1'
TgsIp = '127.0.0.1'
port = 831115
#Mail_sender configuration
sender = 'ed-te1@sz.hitrontech.com'
host = '172.28.10.110'
#host = 'exchange.sz.hitrontech.com'#spam
#host = '58.240.164.252'
website = 'http://172.25.70.190'

server = ['172.25.70.190', 'test', 'test', 'test','TESTlog_20210528']
# server = ['172.18.130.11','test','test','test','TESTLog20210416_20210527','idx']

class DBQuery():
    def __init__(self):
        # self.db = odbc.odbc("TESTlog/TEST/test") 
        self.db = pyodbc.connect('DRIVER={SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'%(server[0],server[1],server[2],server[3]))
        # self.cursor = self.db.cursor()
    def passByDay(self,t):
        self.cursor.execute("SELECT count(idx) FROM [test].[dbo].[TESTlog_20210528] where testtime between '2021-6-1' and '2021-6-2' and status = 'PASS'") 
        querydata = self.cursor.fetchone()
        return querydata
    def getdata(self,d):
        t = d.date().__str__()
        p = d.date() + timedelta(days=3)
        query = ("SELECT distinct PN,ModelName,Status,Counts=count(PN)\
FROM [test].[dbo].[TESTlog_VN] \
where testtime between '{0}' and '{1}'\
group by PN,ModelName,status \
ORDER by Status".format(t,p.__str__()))
        data = pd.read_sql(query, self.db)
        return data.sort_values(by=['Status','Counts'], ascending=False)
    def get(self,d):
        t = d.date().__str__()
        p = d.date() + timedelta(days=3)
        query = ("SELECT distinct PN,ModelName,Status,Station,StationPort,Counts=count(PN)\
FROM [test].[dbo].[TESTlog_VN] \
where testtime between '{0}' and '{1}'\
group by PN,ModelName,status,station,StationPort \
ORDER by Status".format(t,p.__str__()))
        data = pd.read_sql(query, self.db)
        return data.sort_values(by=['Status','Counts'], ascending=False)        
