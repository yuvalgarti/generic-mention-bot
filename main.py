import os

import tweepy
from mention_action.mention_action import MentionAction
from mention_handler.mention_handler import MentionHandler
from mention_handler.services.last_mention_service import LastMentionService

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(os.environ['TWITTER_CONSUMER_KEY'], os.environ['TWITTER_CONSUMER_VALUE'])
    auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN_KEY'], os.environ['TWITTER_ACCESS_TOKEN_VALUE'])

    tweepy_api = tweepy.API(auth, wait_on_rate_limit=True)
    is_production = os.environ.get('IS_PRODUCTION', 'True') == 'True'

    action = MentionAction()
    last_mention_service = LastMentionService()

    mention_handler = MentionHandler(tweepy_api,
                                     action,
                                     last_mention_service,
                                     is_production,
                                     int(os.environ.get('SCREENSHOT_TIMEOUT', 30)),
                                     int(os.environ.get('RETRY_COUNT', 3)))
    mention_handler.run()
