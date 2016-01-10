'''
Created on Dec 10, 2015

@author: xinchenTang
'''
import pymongo
from pymongo  import MongoClient
from gridfs import *
import gridfs

class PyConnect(object):
    '''
    classdocs
    '''
    def __init__(self, host, port):
        '''
        Constructor
        '''
        self.client = MongoClient(host,port)
    
    def use(self,dbname):
        self.db = self.client[dbname]
    
    def setGridFs(self,collection):
        self.fs = gridfs.GridFS(self.db,collection) 

    def insertGridFs(self,data,title):
        id = self.fs.put(data,filename=title)
        return id
 
    def findGridFs(self,id):
        result = self.fs.get(id).read()
        return result
    
    def setCollection(self,collection):
        self.coll = self.db[collection]
        
    def find(self,query = {}):
        result = self.coll.find(query)
        return result
    
    def insert(self,data):
        self.coll.insert(data)
        
    def remove(self,data):
        self.coll.remove(data)
        
    def update(self,data,setdata):
        self.coll.update(data,{'$set':setdata})



