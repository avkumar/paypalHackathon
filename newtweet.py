import csv
import twitter




CONSUMER_KEY = 'gM22WpHEbU3BZJPQ3JgyQ'

CONSUMER_SECRET = 'n8E9uWmUlSeiKqBm85OXHMG3PkE2sT18U37PjJTIQ'

OAUTH_TOKEN = '1518211567-ACbpB3tPXbo98mjnfGdqHCVNEhajmCoBtdUXvEY'

OAUTH_TOKEN_SECRET = 'MO8POnHnvRDyRqPKHmbEkYIVL2U0EjcFkEoYi8zgzMFDh'


auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,

                           CONSUMER_KEY, CONSUMER_SECRET)


twitter_api = twitter.Twitter(domain='api.twitter.com', 
 
                             api_version='1.1',
 
                             auth=auth
)
statuses=[]
q = "@BestBuy"
count = 100
for i in range(500):
     if i==0:
          search_results = twitter_api.search.tweets(q=q, count=count)
          statuses =  statuses + search_results['statuses']
          max_id=search_results['search_metadata']['max_id']
     else:
          search_results = twitter_api.search.tweets(q=q, count=count, max_id=max_id)
          statuses = statuses + search_results['statuses']
          max_id=search_results['search_metadata']['max_id']



tweets = [status['text'] for status in statuses]      
import json

print len(tweets) 

with open('path', 'wb') as f:
     writer=csv.writer(f)
     
     for i in tweets:
         writer.writerow([i.encode('utf-8')])
         print i.encode('utf-8')

