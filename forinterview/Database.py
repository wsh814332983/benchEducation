
import boto3
from boto3.dynamodb.conditions import Key

class DatabaseManage:
    dynamodb = boto3.resource('dynamodb')
    def createTable(self):
        table = self.dynamodb.create_table(
               TableName='PicInfo',
                   KeySchema=[
                       {
                           'AttributeName': 'name',
                           'KeyType': 'HASH'  
                       },
                       {
                         'AttributeName':'owner',
                         'KeyType':'RANGE'  
                       },
                   ],
                   AttributeDefinitions=[
                       {
                           'AttributeName': 'name',
                           'AttributeType': 'S'
                       },
                       {
                           'AttributeName': 'owner',
                           'AttributeType': 'S'
                       },
                   ],
                   ProvisionedThroughput={
                       'ReadCapacityUnits': 10,
                       'WriteCapacityUnits': 10
                   }
            
        )
    
    def getTable(self , name):
        table = self.dynamodb.Table(name)
        return table
        #table.put_item(Item = {'name' : 'tian' , 'age' : 22 ,})
    def insertData(self , name , owner  , date):
        table = self.getTable('PicInfo')
        table.put_item(
            Item = {
                'name' : name ,
                'owner' : owner,
                'date' : date,
            }
            
        )
   
    def getData(self , name , owner):
        table = self.getTable('PicInfo')
        response = table.query(KeyConditionExpression = Key('name').eq(name) & Key('owner').eq(owner))
        return response
    


