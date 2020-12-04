from django.shortcuts import render,redirect
from django.conf import settings
from stegano import exifHeader
from cryptography.fernet import Fernet
import os
import time
from .models import Stega
from django.contrib import messages
# Create your views here.
def encode(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            message=str(request.POST['msg'])
            uploaded_filename=save_upload_image(request.FILES['img'],'upload')
            user_defined_key=str(request.POST['custom_key'])
            try:
                details=Stega.objects.get(username=request.user.username,user_key=user_defined_key)
                messages.error(request,"Looks like there is a problem with the key")
                return render(request,'menu/encode.html')
            except Stega.DoesNotExist:
                fkey=Fernet.generate_key()
                f=Fernet(fkey)
                spc_name=request.user.username+str(int(time.time()))+".jpg"
                message=f.encrypt(message.encode()).decode()
                storage_path="/home/jack1and1jack/django_projects/easystega/media/upload/"+spc_name
                img=exifHeader.hide(uploaded_filename,storage_path,message)
                new_entry=Stega(username=request.user.username,user_key=user_defined_key,fernet_key=fkey.decode())
                new_entry.save()
                os.remove(uploaded_filename)
                messages.success(request,"The information is successfully encoded")
                return render(request,'menu/encode.html',{'source':spc_name})
            except:
                messages.error(request,"Looks like there is a problem with the file")
                return render(request,'menu/encode.html')

        else:
            return render(request,'menu/encode.html')
    else:
        return redirect('%s' % (settings.LOGIN_URL))
def decode(request):
    if  request.user.is_authenticated:
        if request.method=="POST":
            owner=str(request.POST['owner_name'])
            key=str(request.POST['custom_key'])
            uploaded_filename=save_upload_image(request.FILES['image_decode'],'download')
            try:
                fkey=Stega.objects.get(username=owner,user_key=key)
                msg_img=exifHeader.reveal(uploaded_filename).decode()
                fkey=fkey.fernet_key
                f=Fernet(fkey.encode())
                org_msg=f.decrypt(msg_img.encode()).decode()
                os.remove(uploaded_filename)
                messages.success(request,"Success the stored information is displayed below")
                return render(request,'menu/decode.html',{'data':org_msg})
            except:
                messages.error(request,"Please check the file, key and owner name")
                return render(request,'menu/decode.html')

        else:
            return render(request,'menu/decode.html')
    else:
        return redirect('%s' % (settings.LOGIN_URL))

def about_us(request):
    return render(request,'menu/about_us.html')


def save_upload_image(file, tofolder):
	# create the folder if it doesn't exist.
	try:
		os.mkdir(os.path.join(settings.MEDIA_ROOT, tofolder))
	except:
		pass

    # save original file
	original_img = os.path.join(settings.MEDIA_ROOT, tofolder, file.name)
	fout = open(original_img, 'wb+')
    # Iterate through the chunks.
	for chunk in file.chunks():
		fout.write(chunk)
	fout.close()
	return original_img