# CAD-Lite-Recommendations
Version 1.0 Updated on 1/26/2023 by Christopher Gass

This version adds support for FDID specific and response grid specific response plans. For South County Fire, response plans can also be deignated for their RFA and city areas. 

There is preliminary support for multiple dispatch agencies, but that functionality is not fully implemented at this time. 

This is a script that will pull unit recommendations from CAD Lite based on the simplified reponse plans identified by agencies during the basic unit recommendations trial.

This script connects to an API to read real-time unit data from cadlite.org. Logs are output to a connection log and a recommendation log. 

Dependencies are a csv file with the quadrant station order called "Quadrant Station Order.csv", a csv file with a list of all units in CAD Lite called "CadLiteUnitList.csv, and a json file containing response plans called "response_plans.json"

