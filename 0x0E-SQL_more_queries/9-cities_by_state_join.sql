-- Inner Join
SELECT cities.id, states.name, cities.name FROM states INNER JOIN cities ON states.id = cities.state_id ORDER BY cities.id ASC;
