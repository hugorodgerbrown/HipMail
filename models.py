from google.appengine.ext import db

class EmailNotification(db.Model):
    email_sender = db.StringProperty()
    email_subject = db.StringProperty()
    email_body = db.TextProperty()
    email_received = db.DateTimeProperty(auto_now_add=True)
    