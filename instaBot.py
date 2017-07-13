# Importing Libraries..!!!
import requests, urllib
import matplotlib.pyplot as plt
from termcolor import colored
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
color = ['red','green']
APP_ACCESS_TOKEN = '5716171827.dcad29e.9ea0a20986de4dcc971f3442a7f1d4b2'

#Sandbox Users :{"username1" : "im_mukeshdubey" ,"username2" : "rosetaylor1232" ,"username3" : "im_nikkimikki"  ,"username4" : "shreya1400"}


BASE_URL = 'https://api.instagram.com/v1/'


#Function declaration to get your own info !!!!!!

#self info function starts
# defining Function to ascess users information...
def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print colored('GET request url : %s','blue') % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print colored('Username: %s','blue') % (user_info['data']['username'])
            print colored('No. of followers: %s','blue') % (user_info['data']['counts']['followed_by'])
            print colored('No. of people you are following: %s','blue') % (user_info['data']['counts']['follows'])
            print colored('No. of posts: %s','blue') % (user_info['data']['counts']['media'])
        else:
            print colored('User does not exist!!','red')
    else:
        print colored('Status code other than 200 received!','red')
# self info function ends




#get_user_id function starts
#    Function declaration to get the ID of a user by username
def get_user_id(insta_username):                  # Defining function to get User_ID by passing username ..
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print colored('GET request url : %s','blue') % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print colored('Status code other than 200 received!','red')
        exit()
# get_user_id function ends




#get_user_info function starts
#Function declaration to get the info of a user by username!!!!
def get_user_info(insta_username):            #     Defining function to Get user information by passing username ...
    user_id = get_user_id(insta_username)     #     Calling Function of get user_Id  to further proceed..
    if user_id == None:
        print colored('Instauser Of This Username does not exist!','red')
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print colored('GET request url : %s','blue') % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print colored('Username: %s','blue') % (user_info['data']['username'])
            print colored('No. of followers: %s','blue') % (user_info['data']['counts']['followed_by'])
            print colored('No. of people you are following: %s','blue') % (user_info['data']['counts']['follows'])
            print colored('No. of posts: %s','blue') % (user_info['data']['counts']['media'])
        else:
            print colored('There is no data exists for this user!','red')
    else:
        print colored('Status code other than 200 received!','red')
 # get_user_info function ends





#get_own_post function starts
#Function declaration to get your recent post...................
def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print colored('GET request url : %s','blue') % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)    # using urllib library to download the post by passing link of recent media to it ..
            print colored('Your image From Your Recent Posts has been downloaded Successfully!','yellow')
        else:
            print colored('Post does not exist!','red')
    else:
        print colored('Status code other than 200 received!','red')
# get_own_post function ends




#get_user_post function starts
#Function declaration to get the recent post of a user by username!!!!!

def get_user_post(insta_username):   # Defining function to get recent posts of a user by passing username to function..
    user_id = get_user_id(insta_username)    # Calling get user id function to get user id by passing username ..
    if user_id == None:
        print colored('Instauser Of This Username does not exist!', 'red')
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print colored('GET request url : %s','blue') % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)  # Fetching users recent post by passing link to the function as parameter..
            print colored('The Image From users Recent Posts has been downloaded!','yellow')
        else:
            print colored('Post does not exist!', 'red')
    else:
        print colored('Status code other than 200 received!','red')
# get_user_post function ends




#get_post_id function starts
# Function declaration to get the ID of the recent post of a user by username........

def get_post_id(insta_username):
    user_id = get_user_id(insta_username)               #         Capturing the user id ......
    if user_id == None:                                 #         checking in case post exists or not .......
        print colored('InstaUser of this Username does not exist!','red')
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print colored('GET request url : %s','blue') % (request_url)
    user_media = requests.get(request_url).json()            #      Fetching json data ........

    if user_media['meta']['code'] == 200:                    #    checking the status code .......
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print colored('There is no recent post of the user!','red')
            exit()
    else:
        print colored('Status code other than 200 received!','red')
        exit()
# get_post_id function ends




#like_a_post function starts
# Function declaration to like the recent post of a user.........

def like_a_post(insta_username):                              #     Defining the Function ............
    media_id = get_post_id(insta_username)                     # Getting post id by passing the username .......
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}                 #    passing the payloads ........
    print colored('POST request url : %s','blue') % (request_url)         #    post request method  to posting the like ......
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:                        #    checking the status code .....
        print colored('Like was successful!','green')
    else:
        print colored('Your like was unsuccessful.Please Try again!','red')
# like_a_post function ends



#get like list function starts
# Function declaration to Get the like lists on the recent post of a user.........

def get_like_list(insta_username):            # Defining the Function ............
    media_id = get_post_id(insta_username)  # Getting post id by passing the username .......
    request_url = BASE_URL + 'media/%s/likes?access_token=%s' % (media_id, APP_ACCESS_TOKEN)
    print colored('GET request url : %s', 'blue') % (request_url)
    like_list = requests.get(request_url).json()

    if like_list['meta']['code'] == 200:  # checking the status code .....
        if len(like_list['data']):
            position = 1
            print colored("List of people who Liked Your Recent post", 'cyan')
            for users in like_list['data']:
                if users['username']!= None:
                    print position, colored(users['username'],'yellow')
                    position = position + 1
                else:
                    print colored('No one had liked Your post!', 'red')
        else:
            print colored("User Does not have any post",'red')
    else:
        print colored('Status code other than 200 recieved', 'red')

def get_comment_list(insta_username):  # Defining the Function ............
    media_id = get_post_id(insta_username)  # Getting post id by passing the username .......
    request_url = BASE_URL + 'media/%s/comments?access_token=%s' % (
        media_id, APP_ACCESS_TOKEN)  # passing the end points and media id along with access token ..
    print colored('GET request url : %s\n', 'blue') % (request_url)
    comment_list = requests.get(request_url).json()

    if comment_list['meta']['code'] == 200:  # checking the status code .....
        if len(comment_list['data']):
            position = 1
            print colored("List of people who commented on Your Recent post", 'blue')
            for _ in range(len(comment_list['data'])):
                if comment_list['data'][position - 1]['text']:
                    print colored(comment_list['data'][position - 1]['from']['username'], 'yellow') + colored(
                        ' said: ', 'yellow') + colored(comment_list['data'][position - 1]['text'],
                                                       'cyan')  # Json Parsing ..printing the comments ..
                    position = position + 1
                else:
                    print colored('No one had commented on Your post!\n', 'red')
        else:
            print colored("There is no Comments on User's Recent post.\n", 'red')
    else:
        print colored('Status code other than 200 recieved.\n', 'red')
# get like list function ends




#post_a_comment function starts
# Function declaration to make a comment on the recent post of the user................

def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment_text = raw_input(colored("Your comment: ",'magenta'))
    payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print colored( 'POST request url : %s','blue') % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print colored("Successfully added a new comment!",'blue')
    else:
        print colored("Unable to add comment. Try again!",'red')
 # post_a_comment function ends




 #plot function starts
#  Function declaration to make delete negative comments from the recent post.........................

def plot_neg_pos_comments(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print colored('GET request url : %s' ,'blue')% (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            #Here's a naive implementation of how to delete the negative comments :)
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                print colored('negative sentiment:','red'),blob.sentiment.p_neg     #printing negative sentiments in comment
                print colored(' positive sentiment:','green'), blob.sentiment.p_pos    #printing positive sentiments in comment
                plt.pie([blob.sentiment.p_neg,blob.sentiment.p_pos],colors=color)    #plot both sentiments n piechart
                plt.show()
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print colored('Negative comment : %s','red') % (comment_text)
                    #extra work(delete negative comment)
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, APP_ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)    #delete negative comment if any present in a post
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        print colored('Comment successfully deleted!\n','cyan')
                    else:
                        print colored('Unable to delete comment!','red')
                else:
                    print colored('Positive comment : %s\n','cyan') % (comment_text)
        else:
            print colored ('There are no existing comments on the post!','yellow')
    else:
        print colored('Status code other than 200 received!','red')

 # plot function starts






# Defining the Main function under which above sub-function works by calling ...........

def start_bot():
    while True:
        print colored('Hey! We Welcomes U to instaBot!','green')
        print colored('Select your menu options:','blue')
        print colored("Select Option:'A'  To Get your own details\n",'magenta')
        print colored("Select Option:'B'  To Get details of a user by username\n",'magenta')
        print colored("Select Option:'C'  To Get your own recent post\n",'magenta')
        print colored("Select Option:'D'  To Get the recent post of a user by username\n",'magenta')
        print colored("Select Option:'E'  To Get a list of people who have liked the recent post of a user\n",'magenta')
        print colored("Select Option:'F'  To Like the recent post of a user\n",'magenta')
        print colored("Select Option:'G'  To Get a list of comments on the recent post of a user\n",'magenta')
        print colored("Select Option:'H'  To Make a comment on the recent post of a user\n",'magenta')
        print colored("Select Option:'I'  To plot negative and positive comments on pie chart /Also deleted negative comment\n",'magenta')
        print colored("Select Option:'J'  To Exit From The Application..",'red')

        choice = raw_input(colored("Enter you choice: ",'blue'))
        if choice.upper() == "A":
            self_info()
        elif choice.upper() == "B":
            insta_username = raw_input(colored("Enter the username of the user: ",'blue'))
            get_user_info(insta_username)
        elif choice.upper() == "C":
            get_own_post()
        elif choice.upper() == "D":
            insta_username = raw_input(colored("Enter the username of the user: ",'blue'))
            get_user_post(insta_username)
        elif choice.upper() == "E":
            insta_username = raw_input(colored("Enter the username of the user: ",'blue'))
            get_like_list(insta_username)
        elif choice.upper() == "F":
            insta_username = raw_input(colored("Enter the username of the user: ",'blue'))
            like_a_post(insta_username)
        elif choice.upper() == "G":
            insta_username = raw_input(colored("Enter the username of the user: ",'blue'))
            get_comment_list(insta_username)
        elif choice.upper() == "H":
            insta_username = raw_input(colored("Enter the username of the user: ",'blue'))
            post_a_comment(insta_username)
        elif choice.upper() == "I":
            insta_username = raw_input(colored("Enter the username of the user: ",'blue'))
            plot_neg_pos_comments(insta_username)
        elif choice.upper() == "J":
            exit()
        else:
            print colored("Wrong Choice Selected By U",'red')


#   Calling the main function ..........to start the application....
if __name__ =='__main__':
    start_bot()