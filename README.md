#Thread safe rate limiter

## Overview
This project implements a thread safe rate limiter using sliding window in python. Restricting the number of requests a user can make within a time window

## Approach
~A dictionary to store timestamps for the user
~A deque to store timestamps in the chronological order
~Expired timestamps are removed
~A threading lock to make sure of thread safety

## Time complexity
~Adding a timestamp- O(1)
~To check number of requests- O(1)
~Removing expired timestamps- O(n)
~Overall- O(n) {for worst case for each}

## Space complexity
~O(u*n)
~here- u=number of users
       n=maximum number of requests allowed fro each user

## Design trade-offs
~Deque because of its chronology order is more effecient for inserting and removing
~For multiple thread lock prevents race condition
~Sliding window provides more accurate rate limiting than Fixed window
~Using global lock i sismpler but can make requests from different users wait for one another


