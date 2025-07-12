SELECT city
    FROM airports
    WHERE airports.id =
(SELECT destination_airport_id
    FROM flights
    WHERE flights.id =
(SELECT passengers.flight_id
    FROM passengers
    WHERE passengers.passport_number =
(SELECT passport_number
    From people
    WHERE name = 'Bruce')))
