# Generic Mention Bot 
An infrastructure to create a Twitter bot that acts on mentions of it.

# How To Use
In order to create your own bot, you need to:
1. Create a Twitter user for the bot and get the API tokens from Twitter.
2. Extend the next classes and implement the functions they declare:
   1. `LastMentionService` - to store and get the last mention the bot has processed (for persistence)
   2. `MentionAction` - The actual action that needs to be done with each mention
3. Change `main.py` to match your needs

# Environment Variables Used
* **TWITTER_CONSUMER_KEY**
* **TWITTER_CONSUMER_VALUE**
* **TWITTER_ACCESS_TOKEN_KEY**
* **TWITTER_ACCESS_TOKEN_VALUE**
* **IS_PRODUCTION** - is the program running on the production environment
* **MENTION_PROCESS_TIMEOUT** - how much time to wait for mention process before raising a timeout exception (default is 30 seconds)
* **RETRY_COUNT** - how many times to retry mention processing (if failed) before continuing to the next mention
* **MENTIONS_PER_REQUEST** - how many mentions to get in each API request

# Related Projects
An implementation of this infrastructure:
[https://github.com/yuvalgarti/screenshot-for-blocked]()
