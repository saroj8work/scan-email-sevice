from client.ImapClient import ImapClient
from client.SmtpClient import SmtpClient
from service.MongoService import MongoService;

class EmailService:
    mongo = None;
    def __init__(self) :
        self.mongo = MongoService();

    def getReadEmailClient(self):
        #imap_client = ImapClient("imap.gmail.com","sarojtestemail@gmail.com","Abcd@1234");
        #apppassword = vrqa oqmb rsyw cqva
        imap_client = ImapClient("imap.gmail.com","testtktemail2024@gmail.com","vrqa oqmb rsyw cqva");
        return imap_client;

    def fetchEmail(self, imap_client):
        #uid = self.mongo.getlastMessageUID();
        connection = imap_client.connect();
        messages = imap_client.fetchEmails(connection, 2);
        return messages;
    def sendEmail(self, smtp_client):
        pass;
    def getSmtpClient():
        pass;