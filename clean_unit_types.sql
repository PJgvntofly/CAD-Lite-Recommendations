UPDATE units
SET unit_type = (CASE WHEN unit_type LIKE "%Engine%" THEN "Engine"
					  WHEN unit_type LIKE "%Aid Unit%" THEN "Aid Unit"
                      WHEN unit_type LIKE "%Ladder%" THEN "Ladder"
				END)
WHERE unit_type LIKE '%Engine%' OR unit_type LIKE '%Aid Unit%' OR unit_type LIKE '%Ladder%'
