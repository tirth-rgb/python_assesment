class BusReservation:
    def __init__(self):
        # Predefined routes with prices
        self.routes = {
            "Mumbai to Pune": 500,
            "Delhi to Jaipur": 600,
            "Bangalore to Chennai": 550,
            "Kolkata to Delhi": 1200
        }
        self.tickets = {}
        self.route_seats = {route: [] for route in self.routes}  # Tracks booked seats per route
        self.next_ticket_id = 1001  # Unique ticket ID

    # ➔ Show Available Routes
    def show_routes(self):
        route_list = [f"{route} - ₹{price}" for route, price in self.routes.items()]
        return "\n".join(route_list)

    # Validation functions
    def _validate_age(self, age):
        if age <= 0 or age > 120:
            raise ValueError("Invalid age")
        return True

    def _validate_mobile(self, mobile):
        if mobile.isdigit() and len(mobile) == 10:
            return True
        raise ValueError("Mobile number must be 10 digits")

    # ➔ Book Ticket
    def book_ticket(self, name, age, mobile, route):
        if route not in self.routes:
            return "Route not available"
        self._validate_age(age)
        self._validate_mobile(mobile)

        # Check seat availability
        if len(self.route_seats[route]) >= 40:
            return "No seats available on this route"

        seat_number = len(self.route_seats[route]) + 1
        ticket_id = self.next_ticket_id

        self.tickets[ticket_id] = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": route,
            "seat_number": seat_number,
            "price": self.routes[route]
        }
        self.route_seats[route].append(seat_number)
        self.next_ticket_id += 1

        return f"Ticket booked successfully! Ticket ID: {ticket_id}, Seat Number: {seat_number}"

    # ➔ View Ticket
    def view_ticket(self, ticket_id):
        return self.tickets.get(ticket_id, "Ticket not found")

    # ➔ Cancel Ticket
    def cancel_ticket(self, ticket_id):
        if ticket_id not in self.tickets:
            return "Ticket not found"

        route = self.tickets[ticket_id]["route"]
        seat_number = self.tickets[ticket_id]["seat_number"]

        # Remove seat from route
        if seat_number in self.route_seats[route]:
            self.route_seats[route].remove(seat_number)

        del self.tickets[ticket_id]
        return "Ticket cancelled successfully"
