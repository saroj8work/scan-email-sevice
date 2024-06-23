from service.EmailService import EmailService;

def startEmailScan():
    emailService = EmailService();
    client = emailService.getReadEmailClient();
    messages = emailService.fetchEmail(client);
    for msg in messages:
        # Print form and subject
        print(msg.from_, ': ', msg.subject);
        # Print the plain text (if there is one)
        print(msg.text);
        print("UID :"+msg.uid);
        print(msg);

if __name__ == "__main__":
    startEmailScan();