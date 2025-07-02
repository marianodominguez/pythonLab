'''
Created on Mar 10, 2011

@author: mariano
'''

import twitter

def post(api, user, msg):
    if not user: return
    update = "@" + user + ' ' + msg
    print(update)
    api.PostUpdate(update)

api = twitter.Api(consumer_key='T5Fbc00BN8njOfwm69kQbg', 
                  consumer_secret='7MszETCcJFiEssyf5INrLXb6qHqW9mI1MomSnZvs',
                  access_token_key='97066974-coLrESIedyUMuQAM7uLkdIFe6MUDB4aNApanmerte',
                  access_token_secret='IKk7n3rSfG0JUYJZNe4VFt4dazSQIYdNhfzUmYpWU')

user = api.VerifyCredentials()

me = api.GetUser('i_tichy')

print(me)

friends = api.GetFriends('i_tichy')

for f in friends:
    print(f.GetId(), f.GetName(), f.GetScreenName())




