import twitter

api = twitter.Api(consumer_key='T5Fbc00BN8njOfwm69kQbg', 
                  consumer_secret='7MszETCcJFiEssyf5INrLXb6qHqW9mI1MomSnZvs',
                  access_token_key='97066974-coLrESIedyUMuQAM7uLkdIFe6MUDB4aNApanmerte',
                  access_token_secret='IKk7n3rSfG0JUYJZNe4VFt4dazSQIYdNhfzUmYpWU')

user = api.VerifyCredentials()
print user

#searchResult = api.GetSearch(term = "",lang="ES", geocode=("19.432924","-99.128265","50km"))
searchResult = api.GetSearch(term = "aristegui", per_page=50, geocode=("19.432924","-99.128265","50km"))

for result in searchResult:
    print result.id, result.text, result.location, result.user.screen_name 