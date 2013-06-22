
'''
Created on Feb 13, 2011

@author: mariano
'''

import twitter

def post(api, user, msg):
    if not user: return
    update = "@" + user + ' ' + msg
    print "update :", update
    api.PostUpdate(update)

api = twitter.Api(consumer_key='T5Fbc00BN8njOfwm69kQbg', 
                  consumer_secret='7MszETCcJFiEssyf5INrLXb6qHqW9mI1MomSnZvs',
                  access_token_key='97066974-coLrESIedyUMuQAM7uLkdIFe6MUDB4aNApanmerte',
                  access_token_secret='IKk7n3rSfG0JUYJZNe4VFt4dazSQIYdNhfzUmYpWU')

serviceUser = api.VerifyCredentials()
print "Service User: ", serviceUser
print

searchResult = api.GetSearch(term = "chico", geocode=("19.432924","-99.128265", "20mi"))

#searchResult = api.GetSearch(term = "chico", geocode=("Mexico City"))

posts =0

print searchResult

for result in searchResult:
    user = result.user
    print
    print "user:", user
    print "result:", result
    msg = "@"+user.screen_name + " " +"&#0191;Chico?, pues pr&eacute;stame tu atenci&oacute;n."
    if posts<10:
        print msg, result.id
        api.PostUpdate(msg, in_reply_to_status_id=result.id)
        posts +=1
