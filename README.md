# server
Server for handling resquest/response from app

The server uses Django framework for handling json response and also to get the data for recommendation system

It will have the script to handle the PhotoFriends Scripts(which is going to detect friends from photos and send them request on various social media platforms)

To setup the server do following things

install Django - sudo pip3 install django

then just copy the whole folder and the type the following command

[x] cd server

[x] python3 manage.py  runserver

Now to get the json type the following URL's (Provided the base url is same)

1.http://127.0.0.1:8000/trending/news

2.http://127.0.0.1:8000/trending/fb

3.http://127.0.0.1:8000/trending/insta

4.http://127.0.0.1:8000/trending/tweeter

5.http://127.0.0.1:8000/trending/youtube
