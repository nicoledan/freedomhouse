# Freedom House Scraping Project

I wanted to get:
* country name
* press freedom status
* political environment
* economic environment
* press freedom score
* populations
* net freedom status
* freedom in the world status
* internet penetration rate

I started by getting the URLS in a list which I had for the proposal for this project. Then I attempted to get everything I wanted for one country. First I gathered the names of what I wanted the columns to be (I didn't realize this wasn't needed until later). Then I got the numbers for each category.

I wasn't able to figure out how to make it loop through the urls. When I was able to get data for one county in the csv, it still had the tags around it.

Freedomhouse.py was my attempt to get it to write to the csv with many of the comments, then freedomhouse2.py was my attempt to loop through the links which does not work so I do not get a csv, then freedomhouse3.py was my attempt to get a csv with just one county.
