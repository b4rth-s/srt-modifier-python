# srt-modifier-python
To modify linearly the time of occurence of subtitles in a .srt file
Did you ever encounter a subtitles file with delay or advance ? If you have, you know you only have one solution, using VLC to read the movie and wedge the subtitles using the 'h' and 'j' keys.
But you also know it is quite annoying if you want to read the movie from a TV, a tablet without VLC or if you want to give it to somebody that isn't very good with computer.
Therefore, I created that small utility, based on python code. 
Run it with Python3 using 'exec(open(""path to .py file"").read())', give the path to the .srt file and the amount of delay (or advance). Then you'll have a new file with good subtitles.
To finish, you can also use MKVTools to merge the movie file and subtitles file into one .mkv file. By doing that, you'll only have one file for both and the coice whether or not to use the subtitles.
