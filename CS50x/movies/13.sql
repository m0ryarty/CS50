SELECT name FROM people WHERE people.id IN
(SELECT DISTINCT person_id FROM stars WHERE movie_id IN
(SELECT movie_id FROM stars WHERE person_id =
(SELECT id FROM people WHERE name = 'Kevin Bacon' and birth = 1958)))
AND name <> 'Kevin Bacon'
;
