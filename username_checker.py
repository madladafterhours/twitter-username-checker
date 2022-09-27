import tweepy
import random
import threading
import string
import time

#Deactivated acounts may get flagged as available. To my knowledge, theres no way to fix this.

threadnum = 10 #Increasing this value lowers performance and increases speed
letters = 5 #The amount of letters in the username
gens = 1000 #The amount of randomly generated usernames to check against
numbers_included = True #Include numbers in random username generations

def check(incr, tn):
    for index, name in enumerate(names):
        if index-incr == 0 or (index-incr)%tn == 0:
            try:
                api.get_user(screen_name=name)
            except Exception as e:
                if '50' in str(e)[14:16]:
                    valid.append(name)

#####AUTHENTICATION#####
auth = tweepy.OAuthHandler('auth', 'authsecret') #ENTER INFO HERE
auth.set_access_token('key', 'keysecret') #ENTER INFO HERE

api = tweepy.API(auth)

names = [''.join(random.choice(string.ascii_lowercase+string.digits if numbers_included else string.ascii_lowercase) for a in range(5)) for b in range(gens)]
valid = []
threads = []

start_time = time.time()

for i in range(threadnum):
    threads.append(threading.Thread(target=check, args=(i, threadnum)))
    threads[i].start()
for t in threads:
    t.join()

with open('valid_usernames.txt', 'w') as f:
    f.write(''.join(un+'\n' for un in valid))

print(f'Checked {gens} usernames. Process took {round(time.time()-start_time, 2)}s.')