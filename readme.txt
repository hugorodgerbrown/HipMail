HipMail is an application for sending notifications to HipChat.

Why bother?
HipChat is a great team chat application, that has a very simple API for integrating with other notifications. 
Typical scenarios for a development team include automated build notifications, source code check-ins, deployments. 
The lowest common denominator for many tools is the ability to send out event notifications via email, so an email<>hipchat bridge is a simple way to integrate the two.

HipMail is an AppEngine application that does the following:
1. Defines an email endpoint for receiving emails.
2. Sends a notification of a new email to the appropriate HipChat room, using the email subject as the message.
3. Stores the body of the email in the AppEngine datastore.
4. Provides a link in the HipChat notification to the original email.

The first draft has the HipChat API auth_token and room IDs hard-coded, so future enhancements include a simple admin screen.

NB This is not a hosted application - in order to use it you will need to do the following:
1. Have a working Google AppEngine account
2. Download the the GAE Python SDK
3. Download and amend the source code in this repo - updating the AUTH_TOKEN and ROOM_ID variables in the hipmailer.py file
4. Upload to your own GAE account.

The email address to which to send the notifications will depend on the AppEngine app_id you use - more details can be found on the Google help site here - http://code.google.com/appengine/docs/python/mail/receivingmail.html

