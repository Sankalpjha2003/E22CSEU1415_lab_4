class Flight:
    def __init__(self, pid, startTime, priority):
        self.pid = pid
        self.startTime = startTime
        self.priority = priority

    def __repr__(self):
        return f"Flight({self.pid}, {self.startTime}, {self.priority})"


def main():
    flights = [
        Flight("P1", 100, "MID"),
        Flight("P23", 234, "MID"),
        Flight("P93", 189, "HIGH"),
        Flight("P42", 9, "HIGH"),
        Flight("P9", 7, "HIGH"),
        Flight("P87", 23, "LOW"),
    ]

    print("Select the sorting parameter:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        flights.sort(key=lambda flight: flight.pid)
    elif choice == 2:
        flights.sort(key=lambda flight: flight.startTime)
    elif choice == 3:
        flights.sort(key=lambda flight: flight.priority)
    else:
        print("Invalid choice.")
        return

    print("The sorted flights are:")
    for flight in flights:
        print(flight)


if __name__ == "__main__":
    main()
