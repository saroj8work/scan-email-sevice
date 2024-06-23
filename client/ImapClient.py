from imap_tools import MailBox;

class ImapClient:
    username = "";
    password = "";
    imapHost = "";
    def __init__(self, host, username, password):
        self.username = username;
        self.password = password;
        self.imapHost = host;

    def connect(self):
        print("connecting ... " );
        print(self.imapHost+" : "+self.username+" : "+self.password);
        return MailBox(self.imapHost).login(self.username, self.password, 'INBOX');

    def fetchEmails(self, client, uid):
        if uid:
            messages = client.fetch(criteria=f"UID {uid}:*");
        else:
            # If no last processed UID, fetch all emails
            messages = client.fetch();
        return messages;

