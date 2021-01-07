service.subtitles.yifysubtitles
===============================

YIFY Subtitles (http://www.yifysubtitles.com/) service plugin for XBMC / Kodi.

Installation
------------

Get last release archive and manually install it in kodi/osmc settings.

If you get an error, you can follow this *advance* way : 

```bash
unzip yifysubtitles-*.zip
cp -r service.subtitles.yifysubtitles .kodi/addons
xbmc-send -a "UpdateLocalAddons()"
sqlite3 $dbpath/Addons27.db "UPDATE installed SET enabled = 1 WHERE addonID = 'service.subtitles.yifysubtitles'"
xbmc-send -a "UpdateLocalAddons()"
```
Addon should be activated and working.

### Warning

>This addon need an OMDB API key, which you can get from http://www.omdbapi.com/apikey.aspx
>You should be able to set it in the settings of the plugin (the label is empty, it need further testing)


Development 
-----------

This addons includes somes tests with pytests and tox framework to test alongside python2 and python3. 
Tested with python 2.7.18 and python3.9.1. 
Six dependency is included in the 1.15.0 version.
