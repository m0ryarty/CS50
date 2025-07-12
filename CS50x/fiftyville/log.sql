-- Keep a log of any SQL queries you execute as you solve the mystery.
-- That'confirm when the kidnap Happen (10:15 am) and where (Humphrey Street bakery). I need to know what the witnesses said.
SELECT description FROM crime_scene_reports
WHERE description LIKE '%duck%'
;

-- Selecting what the three witness said:
SELECT name, transcript
FROM interviews
WHERE transcript
LIKE '%bakery%';

-- Now I know:
-- From Ruth I know the people who exit parking lot that day.

SELECT name
    FROM people
    where people.license_plate IN
(SELECT bakery_security_logs.license_plate
    FROM bakery_security_logs
    WHERE year = 2023
    AND month = 7
    AND day = 28
    AND hour >= 10
    AND minute <= 25
    AND activity = 'exit')
;

--From Eugene I know the people that withdraw money from Leggett Street's atm.
SELECT name
    FROM people
    WHERE people.id IN
(SELECT person_id
    FROM bank_accounts
    WHERE account_number IN
(SELECT account_number
    FROM atm_transactions
    WHERE year = 2023
    AND month = 7
    AND day = 28
    AND atm_location = 'Leggett Street'
    AND transaction_type = 'withdraw'))
;

-- From Raymond I know who made calls that day
SELECT name
    FROM people
    WHERE phone_number IN
(SELECT caller
    FROM phone_calls
    WHERE year = 2023
    AND month = 7
    AND day = 28
    AND duration < 60)
    ;


-- To know all the people who take a flight a day after that day.
SELECT name
    FROM people
    WHERE people.passport_number IN
(SELECT passengers.passport_number
    FROM passengers
    WHERE passengers.flight_id IN
(SELECT flights.id
    FROM flights
    WHERE year = 2023
    AND month = 7
    AND day = 29
    AND origin_airport_id =
(SELECT airports.id
    FROM airports
    WHERE city = 'Fiftyville') ORDER BY hour, minute LIMIT 1))
    ;


-- All toghther shows me the thief: Taylor.
SELECT name
    FROM people
    where people.license_plate IN
(SELECT bakery_security_logs.license_plate
    FROM bakery_security_logs
    WHERE year = 2023
    AND month = 7
    AND day = 28
    AND hour >= 10
    AND minute <= 25
    AND activity = 'exit')

AND people.id IN
(SELECT person_id
    FROM bank_accounts
    WHERE account_number IN
(SELECT account_number
    FROM atm_transactions
    WHERE year = 2023
    AND month = 7
    AND day = 28
    AND atm_location = 'Leggett Street'
    AND transaction_type = 'withdraw'))

AND phone_number IN
(SELECT caller
    FROM phone_calls
    WHERE year = 2023
    AND month = 7
    AND day = 28
    AND duration < 60)

AND people.passport_number IN
(SELECT passengers.passport_number
    FROM passengers
    WHERE passengers.flight_id IN
(SELECT flights.id
    FROM flights
    WHERE year = 2023
    AND month = 7
    AND day = 29
    AND origin_airport_id =
(SELECT airports.id
    FROM airports
    WHERE city = 'Fiftyville') ORDER BY hour, minute LIMIT 1))

;

-- Knowing Taylor is the thieth, now I need to know who is the acompplience : James
SELECT name
    FROM people
    WHERE phone_number IN
(SELECT receiver
    FROM phone_calls
    WHERE year = 2023
    AND month = 7
    AND day = 28
    AND duration <= 60
    AND caller =
(SELECT phone_number
    FROM people
    WHERE name = 'Bruce'))

-- And where they go
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
;
