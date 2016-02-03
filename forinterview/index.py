
import UploadData



#path of your image
path  = '/Users/tianxiangzhang/Desktop/forinterview/DSC_1790.JPG'
upload = UploadData.UploadData()
upload.uploadImage('image' , path , 'tian11')

#input location of your image that you want to store
downloadpath = '/Users/tianxiangzhang/Desktop/'
upload.getImageThumb('tian11' , 'tianxiang' , downloadpath)