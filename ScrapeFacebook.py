# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 17:28:59 2016

@author: lalit
"""
import urllib2
import json
import datetime
#import time

app_id = "app_id"
app_secret_key = "app_secret_key"# DO NOT SHARE WITH ANYONE!
access_token = app_id + "|" + app_secret_key

def getFacebookData(page_id):
    url="https://graph.facebook.com/"+page_id+"/feed/?fields=message,created_time,likes.limit(1).summary(true),comments.limit(1).summary(true),shares&access_token=%s" % (access_token)
    print url
    req = urllib2.Request(url)
    success = False
    while success is False:
        try: 
            response = urllib2.urlopen(req)
            if response.getcode() == 200:
                success = True
        except Exception, e:
            print e
            print "error in url %s: %s" % (url, datetime.datetime.now())    
    return response.read()

if __name__ == '__main__':
    page_id = raw_input("Please enter the page id of the Facebook page : ")
    #print page_id
    data_set = json.loads(getFacebookData(page_id))
    
    for data in data_set['data']:
        post = '' if 'message' not in data.keys() else data['message'].encode('utf-8')
        published_date = datetime.datetime.strptime(data['created_time'],'%Y-%m-%dT%H:%M:%S+0000')
    
    # Nested items require chaining dictionary keys.
    
        tot_likes = 0 if 'likes' not in data.keys() else data['likes']['summary']['total_count']
        tot_comments = 0 if 'comments' not in data.keys() else data['comments']['summary']['total_count']
        tot_shares = 0 if 'shares' not in data.keys() else data['shares']['count']
        print("Post :"+str(post))
        print("\n")                
        print("Posted date :"+str(published_date))
        print("\n")                
        print("Likes :"+str(tot_likes))
        print("\n")                
        print("Comments :"+str(tot_comments))
        print("\n")                
        print("Shares :"+str(tot_shares))        
        print("\n")                
        print("----------------------------------------------------------")
    