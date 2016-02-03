import boto3
#import sys;
#sys.path.append("Users/tianxiangzhang/Desktop/forinterview/")
import BuildBucket
import time
import Database
import sys

from PIL import Image


class UploadData:
    thumbnailwidth = 150
    thumbnailheight = 150
    manager = BuildBucket.ManageBucket()
    table = Database.DatabaseManage()
    def uploadImage(self , bucketname , path , name):
        ## I assume the path is valid
        bucket = self.manager.createOrGetBucket(bucketname)
        if(not bucket == 0):
            timestamp = time.strftime('%y-%m-%d' , time.localtime(time.time()))
            bucket.upload_file(path , name + timestamp + '.jpg') # I assume the format of the uploading image is jpg
            img = Image.open(path)
            self.table.insertData(name , 'tianxiang' , timestamp)
            if(img.size[0] > 150 or img.size[2] > 150):
                img.thumbnail((self.thumbnailwidth , self.thumbnailheight) , Image.ANTIALIAS)
                bucket = self.manager.createOrGetBucket('thumbnail')
                img.save('/Users/tianxiangzhang/Desktop/forinterview/%sthumbnail.jpg' % (name))
                bucket.upload_file('/Users/tianxiangzhang/Desktop/forinterview/%sthumbnail.jpg' % (name) , name + timestamp + '.jpg')
                thumbimg_acl = boto3.resource('s3').ObjectAcl('com.tianxiang.thumbnail' , name + timestamp + '.jpg')
                thumbimg_acl.put(ACL = 'public-read')
    
    def getImageThumb(self , name , owner , file):
        dm = Database.DatabaseManage()
        response = dm.getData(name , 'tianxiang')
        date = 0
        path = file + name + '.jpg'
        print path
        try:
               file = open(path,'w')  
               file.close()

        except:
               print('Something went wrong! Can\'t tell what?')
               sys.exit(0) 
        
        for i  in response['Items']:
            date = i['date']
        self.manager.getBucket('thumbnail').download_file(name + date + '.jpg' , path)

