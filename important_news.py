# trump_tweets.py - Uses the twitter API to retrieve Mr.Trump's 5 most recent
# tweets then reads them out automatically (Mac Only)

import requests, json, time, os
from requests_oauthlib import OAuth1


tweet_count = 1
tweet_numbers = ['First', 'Second', 'Third', 'Fourth', 'Fifth']
trump_twitter_account = 'https://api.twitter.com/1.1/statuses/user_timeline.\
json?screen_name=realDonaldTrump&count=' + str(tweet_count)


# Twitter API authentication parameters
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
app_key = 'RG8zK6eIAZjIRpE4CpyJnY5oL'
app_secret = '7MYbeKM6wkvjOLAwhm8FcpWdL3eVsJ2Ie3u4UnQMFKxYA4KHAG'
oauth_token = '747079994665467904-IZRFmklnNOzPeCaDIt9oR1JfyCyD7yL'
oauth_token_secret = '2dANaCZ9PtU8ZeRO4NN75tjxCI9DiKw4SeOCqSDFFmNox'


# Get authentication 1.0 request
auth = OAuth1(app_key, app_secret, oauth_token, oauth_token_secret)
requests.get(url, auth=auth)


# Get latest trump tweets
response = requests.get(trump_twitter_account, auth=auth)
tweets = json.loads(response.text)

# os.system("say 'Here are the Donalds most recent tweets, as read by yours \
          # truely, Microsoft Sam.'")

time.sleep(1)


# Read tweets
tweet_text = ''


for count in range(len(tweets)):

    tweet_text = tweets[count]['text']

    if 'https' in tweet_text:
        image_location = tweet_text.find('https')
        tweet_text = tweet_text[:image_location]

    os.system("say " + tweet_numbers[count] + ' tweet')
    os.system("say " + tweet_text.replace("'", ""))
    time.sleep(1)


# Conclude
os.system("say 'That concludes the Trump news for today. Farewell.'")
