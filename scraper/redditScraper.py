import praw

reddit = praw.Reddit(client_id='CLIENT_ID',
                    client_secret='CLIENT_SECRET',
                    user_agent='USER_AGENT')

def redditScraper(subReddit, amountOfPosts=None, topOfWhat='week'):
    listOfPosts = []
    for submission in reddit.subreddit(subReddit).top(topOfWhat, limit=amountOfPosts):
        urlAndTitle = {}
        urlAndTitle["url"] = submission.url
        urlAndTitle["title"] = submission.title
        listOfPosts.append(urlAndTitle)
    print ("Grabing " + str(len(listOfPosts)) + " posts from r/" + subReddit)
    print ("")
    return listOfPosts