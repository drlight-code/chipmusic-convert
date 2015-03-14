# chipmusic-convert

Set of python scripts to conveniently convert different chipmusic
formats into wav/ogg.

## Planned support:
* Atari SAP
* Atari SNDH
* Commodore64 SID
* Amiga MOD
* sc68 format

## Chipmusic archives:
* http://asma.atari.org/ - Atari SAP Music Archive
* http://sndh.atari.org/ - Atari ST YM2149 Archive
* http://www.hvsc.de/ - High Voltage SID Collection
* http://www.tphf.karoo.net/zhmain.htm - Grazey's Zak Hacks
* http://sc68.atari.org/musics.html - sc68 music collection

## Other chipmusic sites:
* http://www.creamhq.de/ymrockerz/index.php - YM Rockerz

If you know of any chipmusic archives or pages that are missing here,
please let me know!

## Required software by format

chipmusic-convert relies on different software packages to do the
actual conversion from the chipmusic formats to wav/ogg. The following
table shows which packages are used for each of the formats:

Format        | Package
------------- | -------------
SNDH          | sndplayer - http://sndplayer.atari.org/downloads.php
sc68          | sc68 - http://sc68.atari.org/download.html
ogg           | vorbis-tools - http://www.vorbis.com

Optional: saunaklub music collection (will be available on github
soon)