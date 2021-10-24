### Question
If we asked you to attempt to "predict" or "score" who would be
the most likely winner of a race on a particular track, how would you attempt to solve this question (please
include any clarifying questions you may have)?

### Answer

Different Formula 1 seasons include different rule changes to the way a car can be built. Some examples of this might be
restricting the use of `ground effect`, which sucks cars to the ground, or removing V8 engine designs. These various rule 
changes, while minor from season to season, can be distinctly categorized by their various "eras", such as when the 
change was made to remove V8 engines, and add energy recovery mechanisms, moving from the `V8 era` to the `KERS era`, or
when hybrid technology was allowed to be put on cars, leading to the current `hybrid era`. 

Various other rule changes were implemented into the sport that affected race strategy and race outcomes, for example, 
removing the ability to refuel the car mid-race, increasing the tyre degradation so that pit stop strategy was much more
important, and enforcing design limitations on aero packages.

A Formula 1 team's success is also highly dependent on their financials. One great example of this would be the Willaims
team, whose success in the 1980s and 1990s is not reflected in the current era, where they are frequently at the bottom
of the leaderboards, following the increased cost of Formula 1 lead by corporate giants with deep pockets, such as the 
likes of Ferrari, Mercedes-Benz, and Red Bull. 

Context aside, I think the best way to predict/score the likelihood of a certain driver/team winning on a specific track would 
be to assign "properties" to the race being analyzed. Going through historical race results, we can assign these properties
to each race. Races in the 2000s might be flagged as "mid-race refueling, V8", whereas races in the 2015-2020 range can be
flagged "single pit stop, hybrid". Looking at future races, we can assemble these properties to match those of the race 
we want to predict. We can even assign properties to circuits as well, for example, Monza is known to favor cars with 
straight line acceleration and speed, called power tracks, whereas a circuit like Singapore prioritizes corner performance 
and traction, known as high downforce tracks.

We can then build our own supervised machine learning model to look at the historical races held at similar circuits to
the one that we are predicting for, as well as for those historical races, look at the number of pit stops, tyre changes,
average lap time, etc, of the drivers in the top three places. Based on that data, we can analyze the performance of a 
driver in the practice and qualifying stages of the race, and compare their difference to the historical data, and see 
if statistically, they are meeting/close to the numbers that previous race winners were holding.

