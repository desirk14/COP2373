# Function to get a valid ticket request
def get_ticket_request(remaining_tickets):
    tickets = int(input(f"How many tickets would you like to purchase today? (1–4, {remaining_tickets} remaining): "))
    # If statement to ensure that user input a valid amount of tickets
    if tickets < 1 or tickets > 4:
        print("You can only buy between 1 and 4 tickets.")
        return 0
    elif tickets > remaining_tickets:
        print("Not enough tickets remaining.")
        return 0
    else:
        return tickets

# Function to handle the ticket sales process
def main():
    total_tickets = 10
    # Accumulator for tickets sold
    tickets_purchased = 0
    # Accumulator for number of buyers
    customers = 0
    # While loop that calculates the amount of tickets remaining and number of buyers
    while tickets_purchased < total_tickets:
        remaining = total_tickets - tickets_purchased
        requested = get_ticket_request(remaining)

        if requested > 0:
            tickets_purchased += requested
            customers += 1
            print(f"Purchase successful. Tickets remaining: {total_tickets - tickets_purchased}\n")

    print("All tickets have been sold!")
    print(f"Total number of buyers: {customers}")

# Call the main function
if __name__ == "__main__":
    main()

    


