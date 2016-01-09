from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from version1.models import Person,File,Container
import os
import version1.GridFs
import time
from datetime import * 
import json 
#from django import forms
# Create your views here.

'''@sainty  2015-11-26
   File_Load_Show System
'''

       

def show(request):
    return render(request,'register.html',[])
                   
def register(request):
    username = request.GET.get('username')
    email1 = request.GET.get('Email')
    passwd1 = request.GET.get('passwd')
    confirm1 = request.GET.get('confirm')
    teacher = request.GET.get('container') 
    if passwd1==confirm1 :
#	handle_uploaded_file(request.FILES['photo'],username+'.image',user)
#	print 'image load successful'
	_id1 = 0
	if cmp(teacher,'wangwennai') == 0:
		_id1 = 1	
	Container.objects.get_or_create(_id=_id1)
        cont = Container.objects.get(_id = _id1)
#	print cont._id
	cont.person_set.create(name=username,email=email1,passwd=passwd1,identity=0,_id=1)
	print cont.person_set.all()
	
	print "saved success"
    else:
	print "different passwd" 
    return HttpResponseRedirect('/login/')
  
def login(request): 
    return render(request,'login.html',[])

def submit(request):
    email2 = request.GET.get('email')
    passwd2 = request.GET.get('passwd')
    es = Person.objects.all()
    m = 0
    name2 = ""
    for e in es:
	if e.email == email2 and e.passwd == passwd2:
		print "find info"
		m=1
		name2 = e.name    
    if m==0:
	print "no info"
        return HttpResponseRedirect('/login/')
    else:
        print "Logining..."
        request.session['username'] = name2	   
        return HttpResponseRedirect('/list/')

def index(request):
    name3 = request.session.get('username','anybody')   
    return render(request,'index.html',{'username':name3})

def logout(request):
    del request.session['username']
    return HttpResponseRedirect('/login/')

def send(request):
    if request.method == "POST":
       if request.POST.get('submit') == 'save':
	    user = request.session['username']
            p = Person.objects.get(name = user)
	    id1 = p._id
	    upload_file = request.FILES['attachment']
	    upload_filename = str(upload_file)
            handle_uploaded_file(upload_file,id1,user+'-'+upload_filename,user)
	    
	    print 'file load success not by db'	
	    filename_list = upload_filename.split('.')     
            note = request.POST.get('note')
	    p.file_set.create(name = user+'-'+filename_list[0],note = note)
	    handle_pptx2imgs(user+'-'+filename_list[0],user,id1)
	    f = open('upload/'+str(id1)+'/'+user+'/' + user+'-'+upload_filename,"r")
	    dbname = str(id1)+'-'+user
 	    store_GridFs(dbname,f)	    
   	    f.close()
            return HttpResponseRedirect('/list/')
       elif request.POST.get('submit') == 'draft':
	   return HttpResponse('draft')
       elif request.POST.get('submit') == 'discard':
           return HttpResponse('discard')

def get_Connection(url,port):
	connect = version1.GridFs.PyConnect(url,port)
	return connect

def store_GridFs(dbname,f):    
	    connect = get_Connection('localhost',27017)
	    connect.use(dbname)
	    connect.setGridFs("PPT")
	    connect.insertGridFs(f.read(),f.name)
	    print 'File load success by GridFs'

def handle_uploaded_file(file,containerid1,filename,user):
    containerid = str(containerid1) 
    if not os.path.exists('upload/'):
          os.mkdir('upload/')
    if not os.path.exists('upload/'+containerid+'/'):
          os.mkdir('upload/'+containerid+'/')    
    if not os.path.exists('upload/'+containerid+'/'+user+'/'):
	  os.mkdir('upload/'+containerid+'/'+user+'/')
    if not os.path.exists('static/images/'+containerid+'/'):
	  os.mkdir('static/images/'+containerid+'/')
    if not os.path.exists('static/images/'+containerid+'/'+user+'/'):
	  os.mkdir('static/images/'+containerid+'/'+user+'/')
    with open('upload/'+containerid+'/'+user+'/' + filename,'wb+') as destination:
	  for chunk in file.chunks():
              destination.write(chunk)


def handle_pptx2imgs(f,u,containerid1):
    containerid = str(containerid1) 
    file_name = f
    upload_url = '/upload/'+containerid+'/'+u+'/'
    images_url = '/static/images/'+containerid+'/'+u+'/'
    item_url = os.getcwd()
    print item_url
    full_name = file_name + '.pptx'
    pdf_name = file_name +'.pdf'
    jpg_name = file_name +'.jpg'
    os.system('unoconv '+item_url+upload_url+full_name+' '+pdf_name)
    print "Finish : PPTX---->PDF"
    os.system('convert '+item_url+upload_url+pdf_name+' '+item_url+images_url+jpg_name)
    print "Finish : PDF ---->JPG named file_name-i"


def list(request):
    name_read = request.session.get('username','anybody')
    print 'username',name_read
    p = Person.objects.get(name=name_read)
    identity1 = p.identity
    container_id1 = p._id
    request.session['identity'] = identity1
    if cmp(identity1,1) == 0:
	cont = Container.objects.get(_id=container_id1)
	p1 = cont.person_set.all()
	filename_content = {}
	for l in p1:
		filename_content1 = dict_filename_content(l.name)
		dictMerged = dict(filename_content,**filename_content1)
		filename_content = dictMerged
	print 'filename_content',filename_content
    else:
	filename_content = dict_filename_content(name_read)
    return render(request,'list.html',{'username':name_read,'filename_content':filename_content})

def dict_filename_content(username):
    p = Person.objects.get(name=username)
    note_all = p.file_set.all()
    print note_all
    filename_content={}
    for i in note_all:
	filename_content[i.name]=i.note
    print filename_content
    return filename_content


def read(request,f):
    name_read = request.session.get('username','anybody')
    p = Person.objects.get(name = request.session['username'])
    identity1 = p.identity
    id1 = p._id
    note_all = p.file_set.all()
    print note_all
    note_read = ''
    file_name1 = f
    for i in note_all:
        if i.name == file_name1:  
		note_read = i.note
		print i.note           
    return render(request,'read-mail.html',{'username':name_read,'filename':file_name1,'note':note_read,'id':id1,'identity':identity1})

def delete(request,index):
    name_read = request.session.get('username','anybody')
    filename_content_list = dict_filename_content(name_read).keys()
    print 'name_read',name_read
    print 'filename_content',filename_content_list
    print 'index :',index
    f = File.objects.get(name=filename_content_list[int(index)])
    f.delete()
    p = Person.objects.get(name=name_read)
    id1 = p._id
    identity1 = p.identity
    if cmp(identity1,1) == 0:
	pass
    upload_url = '/upload/'+str(id1)+'/'+name_read+'/'
    images_url = '/static/images/'+str(id1)+'/'+name_read+'/'
    item_url = os.getcwd()
    i = filename_content_list[int(index)]
    full_name = i + '.pptx'
    pdf_name = i +'.pdf'
    jpg_name = i +'.jpg'
#    print 'rm '+item_url+upload_url+pdf_name
    os.system('rm '+item_url+upload_url+pdf_name)
    print "DELETE : PDF"
    os.system('rm '+item_url+upload_url+full_name)
    print "DELETE : PPTX"
    l = 0
    while (l<2):
           os.system('rm '+item_url+images_url+i+'-'+str(l)+'.jpg')
           l=l+1
    print "DELETE : JPG"
    print 'delete sucess'
    return HttpResponse('ok')




def find(request):
    connect = get_Connection('localhost',27017)
    connect.use('intern_nupt')
    date1 = str(date.today()).replace('-','')
    coll1_name = 'intern'+date1
    connect.setCollection(coll1_name)
    result_list = []
    for i in connect.find():
        result_list.append(i)
    for i in result_list:
       del i['_id'] 
       if i.has_key('intern_location'):
           pass
       else:
           i['intern_location'] = ' '
           i['intern_company'] = ' '

    result = {"data":result_list}
    return HttpResponse(json.dumps(result), content_type="application/json")
   
def test(request):
    return render(request,'projects.html',[])	





