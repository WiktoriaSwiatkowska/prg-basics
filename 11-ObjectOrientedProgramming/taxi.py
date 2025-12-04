class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_recipt(self):
        print(f"the distance:{self.distance}")
        print(f'the fare:{self.fare}')
        print(f'the rate:{self.rate_per_km}')
        



def main():
    # your program
    taxi1 =  TaxiRide(3)
    taxi1.distance = 4
    taxi1.calculate_fare(4)
    taxi1.print_recipt()

    taxi2 =  TaxiRide(6)
    taxi2.distance = 7
    taxi2.calculate_fare(7)
    taxi2.print_recipt()

if __name__ == "__main__":
    main()
