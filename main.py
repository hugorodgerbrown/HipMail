#!/usr/bin/env python
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
import models

class MessageHandler(webapp.RequestHandler):

    def get(self, message_id):
        #TODO: add exception handling
        message = models.EmailNotification.get_by_id(int(message_id))
        self.response.out.write(template.render('templates/message.html',
            {'from':message.email_sender,
            'id':message_id,
            'received':message.email_received,
            'subject':message.email_subject,
            'body':message.email_body}))

def main():
    application = webapp.WSGIApplication([('/message/(.*)', MessageHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
