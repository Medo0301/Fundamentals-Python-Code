class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
while True:
    email = input()
    if email == "Stop":
        break
    email_parts = email.split()
    new_email = Email(email_parts[0], email_parts[1], email_parts[2])
    emails.append(new_email)

indices = [int(x) for x in input().split(", ")]
for idx in indices:
    emails[idx].send()

for index in range(len(emails)):
    print(emails[index].get_info())