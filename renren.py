import urllib2
import urllib
import cookielib
import re
import os
from PIL import Image
import cStringIO
class RenRen(object):
    def __init__(self,loginState=False,photoList=[],albumList=[],friendId=''):
        self.loginState=loginState
        self.cj=cookielib.CookieJar()#����cookie����
        self.opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))#����cookie������򣬴���opener
        self.photoList=photoList
        self.albumList=albumList
        self.friendId=friendId
    def login(self,email='',passward=''):#��������û���������
        
        data={"email":email,"password":passward}#����û�������
        post_data=urllib.urlencode(data )#��data����url����
        
        req=urllib2.Request("http://www.renren.com/PLogin.do",post_data)#��������
        content=self.opener.open(req).read().decode('utf-8')
        self.loginState=True
        #print content
        return content
        

    
    def findAlbum(self):#�ҳ����ID�����б�
        url='http://photo.renren.com/photo/'+self.friendId+'/albumlist/v7#'
        #url='http://photo.renren.com/photo/'+self.friendId+'/album/relatives'
        if self.loginState:
            res=self.request(url)        
            tup=re.findall("nx.data.photo = {(.*?)}};",res,re.S )
            album=re.findall('"albumId":"(.*?)",',tup[0],re.S )
            self.albumList=album
            return album
       
    def request(self,url=""):
        if self.loginState:
            req=urllib2.Request(url)
            res=self.opener.open(req).read().decode('utf-8')
            return res
        
    def findPicUrl(self):#�ҳ�ͼƬURL
        
        for i in range(len(self.albumList)):
            url='http://photo.renren.com/photo/'+self.friendId+'/album-'+str(self.albumList[i])+'/v7'
            res=self.request(url)
            #res.replace("","/")
            try:
                tup=re.findall("nx.data.photo = {(.*?)}};",res,re.S )
                #print tup
                photoUrl=re.findall('"url":"(.*?)"},',tup[0],re.S )
                #print photoUrl
                #print i
            
                self.photoList.append(photoUrl)
            except IndexError:
                self.photoList.append(["none"])
            
        return self.photoList

    def savePic(self):
        for j in range(len(self.albumList)):
            for i in range(len(self.photoList[j])):
                #print str(self.photoList[j][i])
                if self.photoList[j][i]!='none':
                    picUrl=self.photoList[j][i]
                    mode=[]
                    mode=picUrl.split('.')
                   
                    try:
                        
                        picRes=cStringIO.StringIO(urllib2.urlopen(picUrl).read())
                        im=Image.open(picRes)
                        dirName="c:/Python27/girls/"#���浽C��\Python27\girls�ļ�����
                        if not os.path.exists (dirName):
                            os.makedirs (dirName)
                            
                        im.save(dirName+str(self.albumList[j])+"("+str(i)+")."+mode[-1])
                        print self.photoList[j][i]
                    except urllib2.URLError:
                        #print self.photoList[j][i]
                        picUrl=self.photoList[j][i].replace("\\/","/")
                        picRes=cStringIO.StringIO(urllib2.urlopen(picUrl).read())
                        im=Image.open(picRes)
                        im.save("c:/Python27/girls/"+str(self.albumList[j])+"("+str(i)+")."+mode[-1])
                        print picUrl
                
                    
                    
                #im.show()
                #im.save("c:\Python27\girls\\"+str(self.albumList[j])+"("+str(i)+").jpg")
            
        
            
            
            
wuzhe=RenRen()

wuzhe.login()
wuzhe.friendId='225349250'#������ѵ�ID
wuzhe.findAlbum()
wuzhe.findPicUrl()
wuzhe.savePic()






























