import datetime

class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False
        self.timestamp = datetime.datetime.now()
    def mark_as_read(self):
        self.read = True

    def display_full_email(self):
       """Display the full email details."""
       self.mark_as_read()
       print('\n--- Email ---')
       print(f'From: {self.sender.name}')
       print(f'To: {self.receiver.name}')
       print(f'Subject: {self.subject}')
       print(f'Received: {self.timestamp.strftime("%Y-%m-%d %H:%M")}')
       print(f'Body: {self.body}')
       print('------------\n')
    
    def __str__ (self):
        """Return a string representation of the email."""
        status = "Read" if self.read else "Unread"
        return f'[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime("%Y-%m-%d %H:%M")}'


class User:
    def __init__ (self,name, inbox):
        """Initial a User object with a name and inbox"""
        self.name = name
        self.inbox= Inbox()   
    
    def send_email(self, receiver, subject, body):
        """Create an Email object and send it to the receiver."""
        email=Email(self, receiver, subject, body)
        receiver.inbox.receive_email(email)
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    def check_inbox(self):
        """List all emails in the user's inbox."""
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index):
        """Read an email from the inbox by its index."""
        self.inbox.read_email(index)
    
    def delete_email(self, index):
        """Delete an email from the inbox by its index."""
        self.inbox.delete_email(index)

class Inbox:
    def __init__(self):
        """Initialize an Inbox object with an empty list of emails."""
        self.emails = []

    def receive_email(self, email):
        """Add an Email object to the inbox."""
        self.emails.append(email)

    def list_emails(self):
        if not self.emails:
            print("Your inbox is empty.\n")
        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')

    def read_email(self, index):
        """Display the full details of the email at the given index."""
        if not self.emails:
            print("Inbox is empty.\n")
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print("Invalid email number.\n")
        self.emails[actual_index].display_full_email()
            
    def delete_email(self, index):
        """Delete the email at the given index from the inbox."""
        if not self.emails:
            print("Inbox is empty.\n")
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print("Invalid email number.\n")
        del self.emails[actual_index]
        print("Email deleted.\n")
    
    def main():
        tory = User("Tory")
        ramy= User("Ramy")
        tory.send_email(ramy, "Hello", "Hi Ramy, just saying hello!")
        ramy.send_email(tory, "Re: Hello", "Hi Tory, hope you are fine.")
        ramy.check_inbox()
        ramy.read_email(1)
        ramy.delete_email(1)
        ramy.check_inbox()

if __name__ == "__main__":
    main()