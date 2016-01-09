# Django-AdminLTE
PPT real-time display web system 

Introductions:

    1.This is a small system to manage your personal or gourp files and it can collect newest info on intern.However this system can only be run in linux system.
    2.It`s a web server which developed by django and the UI all used from AdminLTE.
    3.MongoDB has been used and all files are all stored in GridFS. 
    4.'http://localhost:8080/shixi/' this url show you a table which present all the newest infomations on intern.
    5.I'm using scrapy to collect all the info from '南大小百合bbs' and '南京邮电大学招生就业信息网'.Also all the info can be download as '.csv' files.
    

Features:

     1.login in/login out
     2.support multi-users and if u`r admin user in your container , you can watch all the files which upload by other users in your container. 
     3.upload files and download them. Insert some tips on your files
     4.when you upload your file like '.pptx',you can watching your ppt online real-time
     5.Find newest info on intern when you get url on 'http://localhost:8080/shixi/'
     
Tips:

     1.You must install django (at leaset v1.7.6)  python 2.7 
     2.If you using ubuntu system,some plugins must be installed.
        apt-get install unoconv
        apt-get install imagemagick
     3.MongoDB database is required.
     4.If you want to  get url on 'http://localhost:8080/shixi/',scrapy will be in need.

Add Functions:

     1.ML-algorithm:I`m going to using ML-algorithm to predict some useful info on appropriate intern choose by analysis your resume. The underline chooses will be 非技术类、技术类（开发、测试、技术支持）.
     2.Comments: You can upload your files which all the users can view or comment.
     3.Wiki on this item will be coming soon.
