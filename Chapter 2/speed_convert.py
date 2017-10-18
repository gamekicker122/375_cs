#speed_convert.py
# A program to convert m/s to mph

def main():
    print("I can convert meters per second into miles per hour")
    meters_per_second = eval(input("What is the m/s ? "))
    miles_per_hour = 3600 / 1609.34 * meters_per_second
    print("The mph is () ,")
    print(miles_per_hour)
    print("Congrats here's your miles per hour!")
    print("Do you need more help?")
    print("If so refresh the page!")
main()
