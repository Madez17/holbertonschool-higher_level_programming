-- Inner Join
SELECT cities.id, states.name, cities.name FROM states INNER JOIN cities ON cities.state_id = states.id ORDER BY cities.id ASC;
