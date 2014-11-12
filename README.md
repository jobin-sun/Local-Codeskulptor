Local-Codeskulptor
==================

A Tool to make Codeskulptor works offline .

Documentation
-------------
### Quick Start:
* Put the codeskulptor python file to src folder , and named codeskulptor.py .
* Double click create.bat , the script will generate "App" folder .
* Click Run.exe , The program will run .
* Compression the App folder , then send it to your buddies :D 

### More
* Add package.json to src folder to make customized demand , [See More][Manifest-format] , the main page must be index.html .
* Store the resources to local , for example , Use a local sound test.ogg , put test.ogg to src folder , then return to parent directory , click create.bat , then all is same to Quick Start .

Note: Only ogg,matroska,wav are supported , if you want to use mp3,H.264 and so on , [See][note-webkit-mp3]

Credits
-------

Local Codeskulptor incorporates code from:
* [node-webkit][node-webkit] 
* [skulpt][skulpt] 
* [codeskulptor][codeskulptor]

License
-------

Local-Codeskulptor is free and unencumbered public domain software. For more
information, see <http://unlicense.org/> or the accompanying UNLICENSE file.

[node-webkit]:		https://github.com/rogerwang/node-webkit/
[skulpt]:	http://www.skulpt.org/
[codeskulptor]: http://www.codeskulptor.org/
[Manifest-format]:https://github.com/rogerwang/node-webkit/wiki/Manifest-format
[note-webkit-mp3]:https://github.com/rogerwang/node-webkit/wiki/Using-MP3-%26-MP4-%28H.264%29-using-the--video--%26--audio--tags.
