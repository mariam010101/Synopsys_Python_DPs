class Email:
    def __init__(self):
        self.to = ""
        self.subject = ""
        self.body = ""

    def __str__(self):
        return f"To: {self.to}\nSubject: {self.subject}\n\n{self.body}"

class EmailBuilder:
    def __init__(self):
        self.email = Email()

    def set_recipient(self, recipient):
        self.email.to = recipient
        return self

    def set_subject(self, subject):
        self.email.subject = subject
        return self

    def set_body(self, body):
        self.email.body = body
        return self

    def build(self):
        return self.email


email = (EmailBuilder()
         .set_recipient("tosomeone@mail.com")
         .set_subject("Greetings")
         .set_body("bla bla bla")
         .build())
print(email)
