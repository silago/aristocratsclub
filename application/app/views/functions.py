import hashlib
from app import cfg
from werkzeug.utils import secure_filename
import os,time,datetime
from PIL import Image

def fileUpload(request,fname):
        filename=''
        dt = time.mktime(datetime.datetime.now().timetuple())
        file = request.files[fname]
        if file:
            filename=str(dt)+"_"+secure_filename(file.filename)
            path = os.path.join(cfg['UPLOAD_FOLDER'],filename)
            path_thumb = os.path.join(cfg['UPLOAD_FOLDER'],'thumb_'+filename)
            file.save(path)
            thumb = Image.open(path)
            if thumb.size[0]<thumb.size[1]: thumb = thumb.transform((thumb.size[0],thumb.size[0]),Image.EXTENT,(0,0,thumb.size[0],thumb.size[0]))
            else:                           thumb = thumb.transform((thumb.size[1],thumb.size[1]),Image.EXTENT,(0,0,thumb.size[1],thumb.size[1]))
                
            
            thumb.thumbnail((300, 300), Image.ANTIALIAS)
            thumb.save(path_thumb)
            return filename
        else: return false
