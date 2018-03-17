import tweepy,os
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from flask import Flask,render_template, request

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def retrieve():
     if request.method == 'POST':
          #handle = input("Enter the handle :: ")
          name = request.form['handle']
          
          #Setting up the user keys and secret keys
          CONSUMER_KEY = '1RgtJSTpUkSA7HZAZhQuQVnF8'
          CONSUMER_SECRET = 'rfQRJT4I0OCyFcE87ytVjaiYvl94A1KXjHgkq4aViB6AgPlcge'
          ACCESS_KEY = '956171608313380865-nkZSFT3ztaE8E78Bsbm3UfcXUoxLPN8'
          ACCESS_SECRET = 'CrGMWxZE5ZJypR5W8mY21FbLWO7EsOwW18rPAnZC0yxZS'
          class TweetListener(StreamListener):
              # A listener handles tweets are the received from the stream.
              #This is a basic listener that just prints received tweets to standard output
              def on_data(self, data):
                  print (data)
                  return True
              def on_error(self, status):
                  print (status)
              def get_last_tweet(self):
                  tweet = self.client.user_timeline(id = self.client_id, count = 1)[0]
                  print(tweet.text)
          auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
          api = tweepy.API(auth)
          auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
          twitterStream = Stream(auth,TweetListener())
          f_count = 'Followes : 0'
          S_count = 'Tweets : 0'
          last_status = 'No Recent Tweet'
          invalid_handle = '0'
          try:
               user = api.get_user(name)
               if user.followers_count:
                    f_count = 'Total Number Of Follower : '+str(user.followers_count)
               if user.statuses_count:
                    S_count = 'Total Number of Tweets : '+ str(user.statuses_count)
               if api.user_timeline(screen_name=name,count=1, tweet_mode='extended'):
                    new_tweets = api.user_timeline(screen_name=name,count=1, tweet_mode='extended')
                    for tweet in new_tweets:
                         last_status = 'Recent Tweet : ' + str(tweet.full_text)
          except:
               invalid_handle=("Could Not find the Twitter Handle!")
          return render_template('twitter.html',f_count=f_count,S_count=S_count,last_status=last_status,invalid_handle=invalid_handle)
     return render_template('twitter.html')


if __name__ == '__main__':
   app.run(debug=True, host='127.0.0.1', port=5000)
