import twitter

api = twitter.Api(consumer_key='xx', 
                  consumer_secret='xx',
                  access_token_key='x-xx',
                  access_token_secret='xx')

user = api.VerifyCredentials()
print user

#searchResult = api.GetSearch(term = "",lang="ES", geocode=("19.432924","-99.128265","50km"))
searchResult = api.GetSearch(term = "aristegui", per_page=50, geocode=("19.432924","-99.128265","50km"))

for result in searchResult:
    print result.id, result.text, result.location, result.user.screen_name 