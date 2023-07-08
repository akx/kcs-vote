# D'Hondt tally system for organization elections

## Method of Usage

* Digitize the ballot papers into a file with lines of the format
  * `<candidate> <vote rank>` (or `<vote rank> <candidate>` if using the `-r` flag)
* Run `python3 tally.py file.txt -c 5`, where here `5` is the number of primary committee members ("pääjäsenet").
