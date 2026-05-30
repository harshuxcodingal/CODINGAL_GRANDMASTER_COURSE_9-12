movieName = "Inception"
ticketPrice = 250.75
availableSeats = 40
showRunning = True

print("Movie:", movieName)
print("Ticket Price:", ticketPrice)
print("Seats Available:", availableSeats)
print("Show Running:", showRunning)

print(type(movieName))
print(type(ticketPrice))
print(type(availableSeats))
print(type(showRunning))

collectionEstimate = ticketPrice * availableSeats
specialOfferPrice = ticketPrice - 25
extraSeats = availableSeats * 2

print("Expected Collection:", collectionEstimate)
print("Offer Price:", specialOfferPrice)
print("Seats After Expansion:", extraSeats)

print("Ticket price below 300?", ticketPrice < 300)
print("More than 30 seats available?", availableSeats > 30)
print("Price exactly 250.75?", ticketPrice == 250.75)

cinemaHall = "Silver" + " " + "Screen"

print("Cinema Hall:", cinemaHall)
print("Movie Name Length:", len(movieName))
print("First Character:", movieName[0])

morningRate = 180
eveningRate = 320

print("Before Swap:", morningRate, eveningRate)

morningRate, eveningRate = eveningRate, morningRate

print("After Swap:", morningRate, eveningRate)