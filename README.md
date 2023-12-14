# CAD-Lite-Recommendations
This is a script for generating unit recommendations for CAD Lite based on simplified response plans identified by fire agencies.
This script connects to an API from cadlite.org to read the unit's status and wiil only recommend units that match the unit type requested
in the response plan, are assigned to a station contained in the station area of the quadrant, and are in an Available or AIQ status. 

Dependencies for this script are:
 - A csv file for the quadrant station order called "Quadrant Station Order.csv"
    - This file should be formatted so that the quadrant name is in the first column and the station order for the 
      quadrant is in the second column as a string with the stations seperated by commas within the string.
    - There should only be 2 columns of data total
 
 - A list of all units in CAD Lite that is used if the API connection cannot be 
   established called "CADLiteUnitList.csv"
    - This file should have thee following formatting:
      - Unit#,Jurisdiction,Unit Type,Assigned Station,Assigned Beat,Display in USM,Unit Status,Cross Staffing
 
 - A JSON file containing the simplified response plans called "response_plans.json"
   - The data should be structured with the root keys as the agency or agencies, with nested keys for the radio
     position or jurisdictions with response plan differences. These should then contain a nested set of key value 
     pairs with the keys being the call types and the values being a list of apparatus types that should be 
     recommended for the call. 
      - If more than one apparatus type could satisfy a request under a specific call type, the apparatus should 
        be contained in a list within the overall list for the call type.
      -Example:
            "BLS1": [
                [
                    "Aid Unit",
                    "Engine",
                    "Ladder"
                ]
            ],