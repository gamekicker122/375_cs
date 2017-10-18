def main():
    total = 0
    score = input ("Whats the score?")
    scores = 0
    while score != "" :
        total = total + eval(score)
        score = input("Whats the next score? click enter twice when done entering grades!")
        scores = scores + 1
    print("Total", total / scores)
    print ("Heres your average!")

main()
