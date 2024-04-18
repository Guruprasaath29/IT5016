class Ticket:
    counter = 0
    tickets_created = 0
    tickets_resolved = 0
    tickets_open = 0

    def __init__(self, creator_name, staff_id, contact_email, description):
        Ticket.counter += 1
        Ticket.tickets_created += 1
        self.ticket_number = Ticket.counter + 2000
        self.creator_name = creator_name
        self.staff_id = staff_id
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"
        Ticket.tickets_open += 1  # Increment open ticket count when a new ticket is created

    def resolve_password(self):
        self.response = f"New password generated: {self.staff_id[:2]}{self.creator_name[:3]}"
        self.status = "Closed"
        Ticket.tickets_resolved += 1
        Ticket.tickets_open -= 1

    def respond_to_ticket(self, response):
        self.response = response
        self.status = "Closed"
        Ticket.tickets_resolved += 1
        Ticket.tickets_open -= 1

    def reopen_ticket(self):
        self.status = "Reopened"
        Ticket.tickets_resolved -= 1
        Ticket.tickets_open += 1

    def print_ticket(self):
        print("Ticket Number:", self.ticket_number)
        print("Ticket Creator:", self.creator_name)
        print("Staff ID:", self.staff_id)
        print("Email Address:", self.contact_email)
        print("Description:", self.description)
        print("Response:", self.response)
        print("Ticket Status:", self.status)
