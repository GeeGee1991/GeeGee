#"gbk"
import urllib2
import urllib
import re
import time
import os
class Songtaste(object):
    def __init__(self,url="http://www.songtaste.com/",songList=[],page=1,album=0):
        self.url=url
        self.songList=songList
        self.page=page
        self.album=album
    def getRecommend(self):
        url=self.url+"music/"+str(self.page)
        response=urllib2.urlopen(url).read()
        tup=re.findall('MSL\((.*?)\);',response,re.S)
        temp=[]
        for i in range(len(tup)):
            temp=tup[i].replace("\"","").replace(" ","").split(",")
            #print temp
            self.songList.append([temp[0].decode("gbk"),temp[1].decode("gbk")])
            #self.songIdList.append(temp[1].decode("gbk"))
            #self.dic[self.songNameList[i]]=self.songIdList[i]
        #print self.songNameList
##        for i in range(len(self.songList)):
##            print self.songList[i][0]
            
        return self.songList
    def rank(self):
        #time=[]
        rankList=[]
        for i in range(len(self.songList)):
            url=self.url+"song/"+str(self.songList[i][1])
            #print url
            response=urllib2.urlopen (url).read()
            #print response
            tup=re.findall("该歌曲共被听 <b>(.*?)</b> 次",response,re.S )
            #print tup
            #time.append(int(tup[0]))
            self.songList[i].insert(0,int(tup[0]))
            
        #print self.songList[0]
        
        print self.songList
        #print rankList
        #rankList1=rankList.reverse()
        #return rankList
    def save(self):
        t= time.strftime ('%x').replace('/','')
        dirName='c:/Python27/song/'+t+'/'
        if not os.path.exists(dirName): 
            os.makedirs(dirName)
        mp3url=[]
        for i in range(len(self.songList)):
            mp3url=''
            print self.songList[i][0]
            url='http://huodong.duomi.com/songtaste/?songid='+self.songList[i][1]

            downloadData=urllib2.urlopen(url).read()
            #print downloadData
            try:
                
                mp3url=re.findall ('var mp3url = (.*?);',downloadData,re.S )[0].replace('\"','')
                #print mp3url
                u=urllib2.urlopen (mp3url).read()
                mp3name=dirName+self.songList[i][0]+'.mp3'
                if not os.path.exists (mp3name):
                #print mp3name
                    with open(mp3name,'wb') as code:
                        code.write(u)
            except IndexError:
                print 'download '+self.songList[i][0]+' failed because of IndexError'
            except IOError:
                print 'download '+self.songList[i][0]+' failed because of IOError'
            except urllib2.HTTPError:
                print 'download '+songList[i][0]+' failed because of HTTPError'
            except ValueError:
                print 'download '+songList[i][0]+' failed because of ValueError'
            except urllib2.URLError:
                print 'download '+songList[i][0]+' failed because of URLError'
            time.sleep(5)

    def save(self,songList):
        t=str(self.album)
        dirName='c:/Python27/song/album'+t+'/'
        if not os.path.exists(dirName): 
            os.makedirs(dirName)
        mp3url=[]
        for i in range(len(songList)):
            mp3url=''
            print songList[i][0]
            url='http://huodong.duomi.com/songtaste/?songid='+songList[i][1]

            downloadData=urllib2.urlopen(url).read()
            #print downloadData
            try:
                
                mp3url=re.findall ('var mp3url = (.*?);',downloadData,re.S )[0].replace('\"','')
                #print mp3url
                u=urllib2.urlopen (mp3url).read()
                mp3name=dirName+songList[i][0]+'.mp3'
                if not os.path.exists (mp3name):
                    
                    #print mp3name
                    with open(mp3name,'wb') as code:
                        code.write(u)
            except IndexError:
                print 'download '+songList[i][0]+' failed because of IndexError'
            except IOError:
                print 'download '+songList[i][0]+' failed because of IOError'
            except urllib2.HTTPError:
                print 'download '+songList[i][0]+' failed because of HTTPError'
            except ValueError:
                print 'download '+songList[i][0]+' failed because of ValueError'
            except urllib2.URLError,e:
                print e.reason()
                #'download '+songList[i][0]+' failed because of URLError'
            time.sleep(5)

        
    def getAlbum(self):
        url='http://www.songtaste.com/user/album/a'+str(self.album)
        albumData=urllib2.urlopen(url).read()
        temp=re.findall ('WS((.*?));',albumData,re.S )[1:]
        songList=[]
        for i in range(len(temp)):
            
            song=temp[i][0].replace('\"','').split(",")
            song[2]=song[2].replace("\\",'')
            songList.append([song[2],song[1]])
            #print song[2]

        
        return songList
            
        
     
#main

songtaste=Songtaste()
songtaste.album=626300
songlist=songtaste.getAlbum()
songtaste.save(songlist)
#songtaste.getRecommend()
#songtaste.save()
#songtaste.rank()

