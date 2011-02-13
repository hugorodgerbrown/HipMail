HipMail is (will be) an application for sending notifications to HipChat.

Why bother?
HipChat is a great team chat application, that has a very simple API for integrating with other notifications. Typical scenarios for a development team include automated build notifications, source code check-ins, deployments. Many existing tools / frameworks have the ability to send out event notifications via email, so a simple email<>hipchat bridge is a very simple way to integrate the two.

HipMail is an AppEngine application that does the following:
1. Defines an email endpoint for receiving emails.
2. Sends a notification of a new email to the appropriate HipChat room, using the email subject as the message, and the sender as the sender.
3. Stores the body of the email in the AppEngine datastore.
4. Provides a link in the HipChat notification to the original email.

The first draft has the HipChat API auth_token and room IDs hard-coded, so future enhancements include a simple admin screen.
