import threading
import time
from collections import deque,defaultdict

class RateLimiter:

    def __init__(self,maxrequests,timewindow):
        self.maxrequests=maxrequests
        self.timewindow=timewindow
        self.requests=defaultdict(deque)
        self.lock=threading.Lock()
    def allow_request(self,userid):
        with self.lock:
            currenttime=time.monotonic()
            userrequests=self.requests[userid]
            while userrequests and (
              currenttime-userrequests[0]>=self.timewindow

            ):
              userrequests.popleft()      
            if len(userrequests)<self.maxrequests:
                  userrequests.append(currenttime)
                  return True
            else:
                  return False

#demo run

'''
limiter=RateLimiter(3,10)
print(limiter.allow_request("user1")) 
print(limiter.allow_request("user1"))
print(limiter.allow_request("user1"))
print(limiter.allow_request("user1"))
print(limiter.allow_request("user2")) '''    