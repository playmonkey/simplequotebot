A simple autotweeter that sends a quote every hour to your twitter account. It's not finalized yet as i'm still debugging it

Stack
-----

i.   heroku

ii.  python 3.6+ & packages

iii. quotebot.py  -> selects a random quote from quote.json and tweets to user account

iv.  webscrape.py -> outputs quote.json (every day)



Create Schedulers on Heroku
---------------------------

1. run quotebot every hour
2. run webscrape every day


Set Environment Variables on Heroku
-----------------------------------

(To secure your private twitter keys enter them into Heroku environment variables. NB Please do not add them to your script)

1. Enter all twitter keys into variables (you can call them anything you like)


ToDo // More robust code with better error handling

[take a look at @randomquotebot1]


