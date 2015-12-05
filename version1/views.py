from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from version1.models import Person,File
import os
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
    if passwd1==confirm1 :
	 handle_uploaded_file(request.FILES['photo'],username+'.image',user)
	    print 'image load successful'	
	Person.objects.get_or_create(name=username,email=email1,passwd=passwd1)
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
   # return HttpResponse('welcome %s' %name3)

def logout(request):
    del request.session['username']
    return HttpResponseRedirect('/login/')

def send(request):
    if request.method == "POST":
       if request.POST.get('submit') == 'save':
	    user = request.session['username']
            handle_uploaded_file(request.FILES['attachment'],str(request.FILES['attachment']),user)
	    print 'file load success not by db'	
            note = request.POST.get('note')
            p = Person.objects.get(name = user)
	    p.file_set.create(name = request.POST.get('filename'),note = note)
	    print 'note saved in db'
	    handle_pptx2imgs(request.POST.get('filename'),user)	    
#           return HttpResponseRedirect('/list/')
#           p = Person.objects.get(name = request.session['username'])
#	   p.file_set.create(name='Filename'+request.session['username'],files = request.FILES['attachment'])
#           print 'file load sucess by db '
            return HttpResponseRedirect('/list/')
       elif request.POST.get('submit') == 'draft':
	   return HttpResponse('draft')
       elif request.POST.get('submit') == 'discard':
           return HttpResponse('discard')

   

def handle_uploaded_file(file,filename,user): 
    if not os.path.exists('upload/'):
          os.mkdir('upload/')
    if not os.path.exists('upload/'+user+'/'):
	  os.mkdir('upload/'+user+'/')
    if not os.path.exists('static/images/'+user+'/'):
	  os.mkdir('static/images/'+user+'/')
    with open('upload/'+user+'/' + filename,'wb+') as destination:
	  for chunk in file.chunks():
              destination.write(chunk)

def handle_pptx2imgs(f,u):
    file_name = f
    upload_url = '/upload/'+u+'/'
    images_url = '/static/images/'+u+'/'
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
    note_all = p.file_set.all()
    print note_all
    note_read = ''
    file_name1 = f
    for i in note_all:
        if i.name == file_name1:  
		note_read = i.note
		print i.note           
    return render(request,'read-mail.html',{'username':name_read,'filename':file_name1,'note':note_read})
#    return HttpResponse('read')

def delete(request,index):
    name_read = request.session.get('username','anybody')
    filename_content = dict_filename_content(name_read)
    print 'index :',index
    m=0
    for i in filename_content:
	if int(index) == m:
		f = File.objects.get(name=i)
		f.delete()
		
		upload_url = '/upload/'+name_read+'/'
   		images_url = '/static/images/'+name_read+'/'
		item_url = os.getcwd()
                full_name = i + '.pptx'
                pdf_name = i +'.pdf'
                jpg_name = i +'.jpg'
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
        m=m+1
    return HttpResponse('ok')






