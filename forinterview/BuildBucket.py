import boto3
import botocore


class ManageBucket:
    __s3 = 0
    __bucket = 0
    
    def __init__(self):
        self.__s3 = boto3.resource('s3')
        
    def getS3(self):
        return self.__s3
        
    def getBucket(self , name):
        self.__bucket = self.__s3.Bucket('com.tianxiang.%s' %(name))
        exists = True
        try:
            self.__s3.meta.client.head_bucket(Bucket = 'com.tianxiang.%s' % (name))
        except botocore.exceptions.ClientError as e:
            error_code = int(e.response['Error']['Code'])
            if error_code == 404:
                exists = False
            return 0
        return self.__bucket
        
    def createOrGetBucket(self , name):
        if(not isinstance(name , str)): # if name is not string we dont move forward. 
            return
        self.__bucket = self.__s3.Bucket('com.tianxiang.%s' %(name))
        exists = True
        
        try:
         
            self.__s3.meta.client.head_bucket(Bucket = 'com.tianxiang.%s' %(name)) # if bucket exist    
        except botocore.exceptions.ClientError as e:
            error_code = int(e.response['Error']['Code'])
            print error_code
            if error_code == 404:
                self.__s3.create_bucket(Bucket='com.tianxiang.%s' %(name) , CreateBucketConfiguration={
                    'LocationConstraint': 'us-west-1'}) 
                self.__bucket = self.__s3.Bucket('com.tianxiang.%s' %(name))    
        return self.__bucket
        
    def accessControl(self , bucket , status):
        if(status == True):
            bucket.Acl().put(ACL = 'private')  #if true make this bucket private
        if(status == False):
            bucket.Acl().put(ACL = 'public-read') 
       
        
    def deleteBucket(self , name):
        bucket = self.getBucket(name)
        if(bucket == 0):
            print 'not exist'
            return
        bucket.delete()
    
    
    



# s3 = boto3.resource('s3')
#
# s3.create_bucket(Bucket='com.tianxiang.image' , CreateBucketConfiguration={
#     'LocationConstraint': 'us-west-1'})
#