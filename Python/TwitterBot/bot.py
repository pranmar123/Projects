#Tutorial used:
#https://www.youtube.com/watch?v=LDVPOBCzj1g
#Tweepy documentation: http://docs.tweepy.org/en/v3.5.0/

from DataManager import DataManager
import tweepy
from time import sleep
#These are APIs so that the bot can access your twitter account using these secret keys.
#You can find these API on Twitter Developer after you create your bot acc
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret= ''

#authorizing the access
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

#securing the connection
auth.secure = True
#the wait on rate limit is so that the code obeys the rate limit that
#twitter allows your API to access the information
api = tweepy.API(auth)

'''This is a test to make sure that the API is working
print(str(api.get_user(screen_name = "enter_your_screen_name_here")))
'''

#to make sure that you are not retweeting your own tweets
myBot = api.get_user(screen_name = '@') #Enter the bots screename

#we are going to use data manager which stores the ids of tweets we already looked at
#and then in our loop, we can continue if the id exists so that the bot isn't looking for
#tweets it has already tweeted.
myData = DataManager("datafile.txt")

#You are going to iterate through whatever q (whether it be a hashtag
#or a word, then items is so you can specify how many items
#you want to go through
#tweet will contain the ACTUAL tweet, but it has attributes like
#user that tweeted it, etc.
pnum = 1
for page in tweepy.Cursor(api.search,q = '#enteryourhashtaghere',lang="en").pages(25):
    print("Page # %d"%pnum)
    for tweet in page:
        try:
            #to make sure that you are not retweeting your own tweets
            if (tweet.user.id == myBot.id) or (myData.is_stored_b(str(tweet.id))):
                print("This tweet was already processed.")
                continue

            myData.add_data(str(tweet.id))
            #printing out users that have tweeted with the hashtag
            print("\n\nFound tweet by: @",tweet.user.screen_name)

            #retweeting the tweet
            if(tweet.retweeted == False) or (tweet.favorited == False):
                #retweeting
                tweet.retweet()
                tweet.favorite()
                print("Retweeted and favorited the tweet by @ %s" %tweet.user.screen_name)

                #following the user
                if tweet.user.following == False:
                    #following
                    tweet.user.follow()
                    print("Followed the user @ %s" %tweet.user.screen_name)

        #this will print out the reason for the error
        except tweepy.TweepError as ex:
            print(ex.reason)
            if "429" in ex.reason:
                sleep(900) #sleeps for 30 mins so that it doesn't reach max
                #twitter limits. 

            else:
                sleep(1)
            sleep(1)
            continue
        
        
        #this is to break if you reach the end of the tweets
        except StopIteration:
            break
    pnum += 1

    

###This is to unfollow, unretweet, etc.
##for follower in tweepy.Cursor(api.friends).items():
##    try:
##        follower.unfollow()
##        print("Unfollowed: " + follower.screen_name)
##    except Tweepy.TweepError as e:
##        print(e)
##        sleep(5)
##        continue



 












