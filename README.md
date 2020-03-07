# clarity_finder
query honda API to find all dealerships that are stocking 2020 Clarity by zip code
# Why
2020 Clarity is only being sold in California despite demand elsewhere and is difficult to find. Someone on a Facebook post recommended finding zip codes of major cities and checking each one. I figured we could brute force that problem and maintain a list. The list in clarity_dealers.txt was last updated 2020-03-06. 
## Usage
```
pip3 install -r requirements.txt
python3 clarity_finder.py
python3 clarity_finder.py --year=2019 #use this to switch model year
open clarity_dealers.txt
```
## I just want to see the data
check out [the most recent list](./clarity_dealers.txt)
## Caveats
If Honda changes or limits their API, this might no longer work. The data in the text file is only as good as the last time it was run. It takes a while to run, I let it go overnight. The count may be inaccurate, but all of the ones listed should have or be expecting at least one Clarity. There also may be a few that are missed if there's ever a case where there are more than one dealer in the same zip+4 area. This is probably unlikely.

