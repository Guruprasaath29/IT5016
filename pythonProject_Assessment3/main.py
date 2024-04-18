from ticket import Ticket

#ticket details
def create_ticket():
    creator_name = input("Enter ticket creator's name: ")
    staff_id = input("Enter staff ID: ")
    contact_email = input("Enter contact email: ")
    description = input("Enter description of the issue: ")

    ticket = Ticket(creator_name, staff_id, contact_email, description)
    print("Ticket created successfully!")
    ticket.print_ticket()  # Displaying ticket number here
    return ticket

def resolve_ticket():
    ticket_number = int(input("Enter ticket number to resolve: "))
    for ticket in tickets:
        if ticket.ticket_number == ticket_number:
            response = input("Enter response to the ticket: ")
            ticket.respond_to_ticket(response)
            print("Ticket resolved successfully!")
            return
    print("Ticket not found!")

def display_ticket_statistics():
    print("Displaying Ticket Statistics")
    print("Tickets Created:", Ticket.tickets_created)
    print("Tickets Resolved:", Ticket.tickets_resolved)
    print("Tickets To Solve:", max(Ticket.tickets_open, 0))

def print_tickets():
    for ticket in tickets:
        ticket.print_ticket()

def generate_password(ticket):
    ticket.resolve_password()
    print("Password generated and ticket resolved successfully!")

tickets = []

while True:
    print("\n1. Create a ticket")
    print("2. Resolve a ticket")
    print("3. Display ticket statistics")
    print("4. Print Tickets")
    print("5. Generate password")
    print("6. Reopen ticket")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        tickets.append(create_ticket())
    elif choice == '2':
        resolve_ticket()
    elif choice == '3':
        display_ticket_statistics()
    elif choice == '4':
        print_tickets()
    elif choice == '5':
        ticket_number = int(input("Enter ticket number to generate password: "))
        for ticket in tickets:
            if ticket.ticket_number == ticket_number:
                generate_password(ticket)
                break
        else:
            print("Ticket not found!")
    elif choice == '6':
        ticket_number = int(input("Enter ticket number to reopen: "))
        for ticket in tickets:
            if ticket.ticket_number == ticket_number:
                ticket.reopen_ticket()
                print("Ticket reopened successfully!")
                break
        else:
            print("Ticket not found!")
    elif choice == '7':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")