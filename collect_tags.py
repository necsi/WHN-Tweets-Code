import pandas as pd
import snscrape.modules.twitter as sntwitter
import datetime

data=pd.read_excel(open('WhoarethetopAdvocates_All.xlsx', 'rb'),sheet_name='Who are the top Advocates',index_col=3)
names=data['Unnamed: 2'].to_list()[2:]

for nam in names:
    tweets_candidats=[]
    tweet_collection = pd.DataFrame({'Username':[],'Date':[],'Likes':[],'Content':[]})
    #https://i.stack.imgur.com/gewA8.png since:{datetime.date(2023,2,20)},until:{datetime.date.today()},
    for tweet in sntwitter.TwitterSearchScraper(f'from:{nam}').get_items():
        #'since:{date_beg} until:{date_end}
        #print(tweet)
        tweets_collection = tweets_candidats.append([tweet.id,tweet.user.username,tweet.date,tweet.rawContent,tweet.coordinates,tweet.place,tweet.hashtags,tweet.cashtags])
        #print(len([tweet.user.username,tweet.date,tweet.rawContent,tweet.likeCount,tweet.sourceUrl,tweet.quotedTweet,tweet.outlinks,tweet.quoteCount,tweet.replyCount,tweet.retweetCount,tweet.retweetedTweet,tweet.inReplyToTweetId,tweet.inReplyToUser,tweet.mentionedUsers]),len(["Username","Date","Tweet","Likes","quotecount","sourceUrl","quotedTweet","quotecount","replyCount","Retweets","retweetedTweet","inReplyToTweetId","inReplyToUser","mentionedUsers"]))
    pd.DataFrame(tweets_candidats,columns=["id","Username","Date","Tweet","coordinates","place","hashtags","cashtags"]).to_csv('data_tags/'+nam+'.csv')


'''
coordinates: typing.Optional ['Coordinates'] = None
place: typing.Optional['Place'] = None
hashtags: typing.Optionalityping.List[str]] = None
cashtags: typing.Optional[typing.List[str]l


replyCount: int retweetCount: int
likeCount: int
quotecount: int conversationId: int lang: str
source: str
sourceUrl: typing.Optional[str] = None
sourceLabel: typing.Optional(str] = None
outlinks: typing.Optional[typing.List[str]] = None
tcooutlinks: typing.Optional[typing.List[str]] = None
media: typing.Optional[typing.List ['Medium']] = None
retweetedTweet: typing.Optional[ 'Tweet'] = None
quotedTweet: typing.Optional[ 'Tweet'] = None
inReplyToTweetId: typing.Optional[int] = None
inReplyToUser: typing.Optional['User'] = None
mentionedUsers: typing.Optionalityping.List['User']] = None
'''
