# Generic Mention Bot 
An infrastructure to create a Twitter bot that acts on mentions of it.

# How To Use
In order to create your own bot, you need to:
1. Create a Twitter user for the bot and get the API tokens from Twitter.
2. Extend the next classes and implement the functions they declare:
   1. LastMentionService - to store and get the last mention the bot has processed (for persistence)
   2. MentionAction - The actual action that needs to be done with each mention
3. Changed main.py to match your needs


# Related Projects
An implementation of this infrastructure:
https://github.com/yuvalgarti/screenshot-for-blocked
