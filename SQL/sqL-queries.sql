-- Total number of flights per airport -- 
SELECT airport_code, COUNT(*) AS total_flights
FROM flights
GROUP BY airport_code
ORDER BY total_flights DESC;

-- Average delay per airport --
SELECT a.airport_code, a.city_name,AVG(d.total_delay) AS avg_delay
FROM airports a
INNER JOIN flights f ON a.airport_code = f.airport_code
INNER JOIN delays d ON f.flight_id = d.flight_id
GROUP BY a.airport_code
ORDER BY avg_delay DESC;

-- Delay by state -- 
SELECT a.state_name AS STATE,AVG(d.total_delay) AS Average_delay
FROM airports a
JOIN flights f ON a.airport_code = f.airport_code
JOIN delays d ON f.flight_id = d.flight_id
GROUP BY a.state_name
ORDER BY Average_delay DESC;

--Delay Probability based on the time --
SELECT dep_hour,AVG(total_delay) AS Average_delay
FROM flights
JOIN delays ON flights.flight_id = delays.flight_id
ORDER BY dep_hour;

-- Congestion Indicator -- 
SELECT a.airport_code, AVG(f.taxi_out) AS avg_taxi_out
FROM flights f
JOIN airports a ON f.airport_code = a.airport_code
GROUP BY a.airport_code
ORDER BY avg_taxi_out DESC;

-- Airports ranked based on delays --
SELECT a.airport_code, a.city_name,AVG(d.delay_label) AS delay_probability
FROM airports a
JOIN flights f ON a.airport_code = f.airport_code
JOIN delays d ON f.flight_id = d.flight_id
GROUP BY a.airport_code, a.city_name
ORDER BY delay_probability DESC;









