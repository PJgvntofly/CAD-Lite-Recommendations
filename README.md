# CAD-Lite-Recommendations
This is a script that will pull unit recommendations from CAD Lite based on the simplified reponse plans identified by agencies during the basic unit recommendations trial.

For this script to work as designed, some of the unit data that exists in the CAD Lite SQL server would need to be cleaned. For example, the script expects all engines to have the unit type of "Engine". "ALS Engines" or the various other engine types that currently exist in Enterprise CAD would need to be simplified to the base unit type in CAD Lite. There are a handful of unit types where this would apply. A script could be applied to clean the data either when it is extracted from Enterprise CAD or when it is uploaded to CAD Lite. 
