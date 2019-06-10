import tweepy
import time

CONSUMER_KEY = 'qmVEdhqOjexn04dOo4FW13sTB'
CONSUMER_SECRET = 'oC1ynd8N6Fmwq2FwARkUAUguUX1aP30EceldITJb5KosE4n5lf'
ACCESS_KEY = '1136537605275656192-zqJRRk3TqbTV0ZS5zw9FynFUtOHd7k'
ACCESS_SECRET = '3KyiNthLEEhLvg7PMRbnoqMjckDxb4YRsbkZKwSF6nB6I'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

print('this is my')

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    #DevNote: use 1136576972723593216 for testing
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#helloworld' in mention.full_text.lower():
            print('Found #helloworld', flush=True)
            print('responding back', flush=True)
            api.update_status('@'+ mention.user.screen_name + '#HelloWorld back to you!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(3)
