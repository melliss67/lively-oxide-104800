App Engine application for the Udacity training course.

## Task 1: Add Sessions to a Conference

I created the Session entity as a child of the Conference entity because
every Session neeeds to be part of a Conference. I used the ENUM SessionType
class for the typeOfSession so only certain values are allowed. I am storing 
the start day and time as a DateTime value and then seperating the time on the 
SessionForm into 24 hour noation so it can be sorted.

I decided to create a sperate Speaker entity instaed of allowing any text entry.
I feel this will keep the data more consistent and make querying easier and 
more accurate in the future. I added an endpoint to allow adding new speakers
and store the sppeaker id inthe session to retrieve the speker object later.

## Task 2 : Add Sessions to User Wishlist

I added both endpoints to sessions to a wish list and to retrieve a wish list.
I decided that the user did not not have to already be registered for the 
conference to be required to add the session. I felt they could use their wish 
list to decide if they want to attend the conference.

## Task 3: Work on indexes and queries

I created a query to list all conferences that are less than half full so more
effort can be put into filling those conferences. The endpoint for the query is
getLowReg.

I also created a query to show conferences with no sessions. This could be used
to make sure the sessions have been added to the conference. The endpoint for
the query is getNoSessions.

The problem with the proposed qury to show no workshops and only session before
7 pm is that you can not filter using 2 or more inequalities. To solve this I 
would first get all sessions that are not workshops. Then I would loop through 
the sessions and add only the session before 7 pm to a new list and return that
list. I have implemented that code with the endpoint getNoWorkshops.

## Task 4

Added a task to add a new Memcache entry if a speaker has more than one session
at a conference. I check for multiple sessions by the same speaker right after 
the session is added and then trigger the action if they have more than one 
session. Also added the getFeaturedSpeaker() endpoint to get the featured 
speaker.

## Products
- [App Engine][1]

## Language
- [Python][2]

## APIs
- [Google Cloud Endpoints][3]

## Setup Instructions
1. Update the value of `application` in `app.yaml` to the app ID you
   have registered in the App Engine admin console and would like to use to host
   your instance of this sample.
1. Update the values at the top of `settings.py` to
   reflect the respective client IDs you have registered in the
   [Developer Console][4].
1. Update the value of CLIENT_ID in `static/js/app.js` to the Web client ID
1. (Optional) Mark the configuration files as unchanged as follows:
   `$ git update-index --assume-unchanged app.yaml settings.py static/js/app.js`
1. Run the app with the devserver using `dev_appserver.py DIR`, and ensure it's running by visiting
   your local server's address (by default [localhost:8080][5].)
1. Generate your client library(ies) with [the endpoints tool][6].
1. Deploy your application.


[1]: https://developers.google.com/appengine
[2]: http://python.org
[3]: https://developers.google.com/appengine/docs/python/endpoints/
[4]: https://console.developers.google.com/
[5]: https://localhost:8080/
[6]: https://developers.google.com/appengine/docs/python/endpoints/endpoints_tool
