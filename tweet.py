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

q = "@BestBuy"
count = 500
search_results = twitter_api.search.tweets(q=q, count=count)
statuses = search_results['statuses']
#print statuses

for _ in range(count):
     try:
          next_results = search_results['search_metadata']['next_results']
     except KeyError, e: # No more results when next_results doesn't exist
        break

     kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ]) # Create a dictionary from the query string params
     search_results = twitter_api.search.tweets(**kwargs)
     #print search_results['statuses']

     statuses += search_results['statuses']
tweets = [status['text'] for status in statuses]      
import json
print "length of tweets is", len(tweets) 


with open('output', 'wb') as f:
     writer=csv.writer(f)
     
     for i in tweets:
         writer.writerow([i.encode('utf-8')])
         print i.encode('utf-8')

print "length of tweets is", len(tweets) 
