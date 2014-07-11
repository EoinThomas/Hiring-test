Amadeus hiring test answers

I used pandas throughout all exercises, which greatly reduced the amount of code and the need for user defined functions. I am using large chunksizes when reading in the data as this greatly reduces the runtime of many of the exercises, naturally this requires more memory.

Notes:
Ex1: Print file length: loaded a single column iteratively with pandas



Ex2: top 10 airports: the code is based on pandas' groupby function. I have a compatibility issue with geobases on my machine. I included the code to use once compatibility is resolved in the comments, and accessed the relevant geobases data to create a workaround.



Ex3: Plot monthly searches for 3 arrival airports. Code is based on pandas' grouby function. I tidied up the figure properties so that any combination of airports can be selected.



Bonus1: Match searches to bookings.
1) Cleaned up the bookings: removed cancellations, removed return leg of trips, renamed columns.
2) Used the merge function to match searches and bookings according to departure, destination, and day of flight.
3) Removed matched searches where the search was dated after the booking.

I match roughly 2% of searches, however this is more than likely an overestimate. More information about the data is required in order to improve the matching accuracy. (i.e. the maximum time between a search date and booking creation date)



Bonus2: Webservice version of top n airports in json format. I used the Flask framework and tested the service locally.

With bookings.csv in the same folder, run:
python topairports_service.py
then access the service in a browser at:
http://127.0.0.1:5000