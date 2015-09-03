#!/usr/bin/env python
import webapp2
from google.appengine.api import app_identity
from google.appengine.api import mail
from google.appengine.api import memcache

from conference import ConferenceApi
from conference import MEMCACHE_FEATURED_SPEAKER_KEY

class SetAnnouncementHandler(webapp2.RequestHandler):
    def get(self):
        """Set Announcement in Memcache."""
        # TODO 1
        # use _cacheAnnouncement() to set announcement in Memcache
        ConferenceApi._cacheAnnouncement()
        self.response.set_status(204)


class SendConfirmationEmailHandler(webapp2.RequestHandler):
    def post(self):
        """Send email confirming Conference creation."""
        mail.send_mail(
            'noreply@%s.appspotmail.com' % (
                app_identity.get_application_id()),     # from
            self.request.get('email'),                  # to
            'You created a new Conference!',            # subj
            'Hi, you have created a following '         # body
            'conference:\r\n\r\n%s' % self.request.get(
                'conferenceInfo')
        )


class AddFeaturedSpeakerHandler(webapp2.RequestHandler):
    def post(self):
        """add memcache entry for featured speaker"""
        # memcache.set(MEMCACHE_FEATURED_SPEAKER_KEY, 
            # '%s is our latest Featured Speaker' % 'Matt')
        
        memcache.set(MEMCACHE_FEATURED_SPEAKER_KEY, 
            '%s is our latest Featured Speaker' % self.request.get(
            'speakerName'))


app = webapp2.WSGIApplication([
    ('/crons/set_announcement', SetAnnouncementHandler),
    ('/tasks/send_confirmation_email', SendConfirmationEmailHandler),
    ('/tasks/add_featured_speaker', AddFeaturedSpeakerHandler),
], debug=True)
