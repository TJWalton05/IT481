import threading
import random
import time

class DressingRooms:
    def __init__(self, number_of_rooms=3):
        self.number_of_rooms = number_of_rooms
        self.semaphore = threading.Semaphore(number_of_rooms)

    def request_room(self):
        self.semaphore.acquire()

    def release_room(self):
        self.semaphore.release()

class Customer(threading.Thread):
    def __init__(self, id, dressing_rooms, number_of_items=0):
        threading.Thread.__init__(self)
        self.id = id
        self.dressing_rooms = dressing_rooms
        self.number_of_items = number_of_items if number_of_items else random.randint(1, 6)
        self.time_spent = 0

    def run(self):
        self.dressing_rooms.request_room()
        print(f"Customer {self.id} entered a dressing room with {self.number_of_items} items.")
        for i in range(self.number_of_items):
            try_on_time = random.randint(1, 3)
            self.time_spent += try_on_time
            time.sleep(try_on_time)  # Simulate trying on clothes
        print(f"Customer {self.id} leaving dressing room after {self.time_spent} minutes.")
        self.dressing_rooms.release_room()

class Scenario:
    def __init__(self, number_of_rooms, number_of_customers, specific_items=None):
        self.dressing_rooms = DressingRooms(number_of_rooms)
        self.customers = [Customer(i, self.dressing_rooms, specific_items) for i in range(1, number_of_customers + 1)]
        self.start_time = None
        self.end_time = None

    def run_scenario(self):
        self.start_time = time.time()
        for customer in self.customers:
            customer.start()
        for customer in self.customers:
            customer.join()
        self.end_time = time.time()

    def calculate_results(self):
        total_time = self.end_time - self.start_time
        total_items = sum(customer.number_of_items for customer in self.customers)
        total_usage_time = sum(customer.time_spent for customer in self.customers)
        avg_items = total_items / len(self.customers)
        avg_usage_time = total_usage_time / len(self.customers)
        return {
            "total_time": total_time,
            "average_items_per_customer": avg_items,
            "average_usage_time": avg_usage_time,
            "total_customers": len(self.customers)
        }

def run_scenarios():
    scenarios = [
        Scenario(3, 10),  # 3 rooms, 10 customers
        Scenario(5, 15),  # 5 rooms, 15 customers
        Scenario(7, 20)   # 7 rooms, 20 customers
    ]

    for i, scenario in enumerate(scenarios, start=1):
        print(f"Running scenario {i}...")
        scenario.run_scenario()
        results = scenario.calculate_results()
        print(f"Scenario {i} Results:")
        print(f"Total time: {results['total_time']} seconds")
        print(f"Average items per customer: {results['average_items_per_customer']}")
        print(f"Average usage time per customer: {results['average_usage_time']} minutes")
        print(f"Total customers served: {results['total_customers']}\n")

run_scenarios()
