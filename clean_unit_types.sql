UPDATE units
SET unit_type = (CASE WHEN unit_type LIKE "%Engine%" THEN "Engine"
					  WHEN unit_type LIKE "%Aid Unit%" THEN "Aid Unit"
                      WHEN unit_type LIKE "%Ladder%" THEN "Ladder"
				END)
WHERE jurisdiction LIKE "31C%" OR jurisdiction LIKE "31D%" OR jurisdiction LIKE "31M%" 
