import tweepy # to gather tweeter data
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import re
from wordcloud import WordCloud
plt.style.use('fivethirtyeight')
# Twitter Api  Credentials
APIkey= "qBbo2B5vQxnDBtwqNTZ3C57UA"
APISecreatKey= "tbveShl1CGJPM706ybeIPIWGNZWBaXtsyAi8wZ6VgmiWR9AOGB"
accessToken= "1080866487819272192-VhW4s2WGskT3tg65eVeC6BdgRxMHpN"
accessTokenSecreat= "8EPbYCHl3aXculBl4SxfpCIsCsfEJxyoMIrZv6icU0oUJ"
# create the authentication object
authenticate = tweepy.OAuthHandler(APIkey,APISecreatKey)
authenticate.set_access_token(accessToken,accessTokenSecreat)
api= tweepy.API(authenticate)
posts= api.user_timeline(screen_name='Trump',count=100,lang="en",tweet_mode='extended')
i=1
for tweet in posts[:10]:  # just want to see the top 10 from 100
    print(str(i) + ') ' + tweet.full_text + '\n')
    i= i+1
    # Create a dataframe with a column called tweets
df= pd.DataFrame([tweet.full_text for tweet in posts],columns=['Tweets'])
df
# make a function to clean tweets
def cleanTxt(text):
    text= re.sub('@[A-Za-z0-9]+','',text ) #removing mentions
    text= re.sub("#",'',text) #removing #
    text= re.sub('RT[\s]+','',text) # removing Retweets
    text= re.sub('https?:\/\/\S+','',text) #removing links
    return text
    df['Tweets']= df['Tweets'].apply(cleanTxt)
    df
    