# chipmusic-convert

Set of python scripts to conveniently convert different chipmusic
formats into wav/ogg/flac.

## Supported:
* Commodore64 SID
* Atari SNDH
* sc68 format

## Planned support:
* Atari SAP
* Amiga MOD

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
actual conversion from the chipmusic formats to wav/ogg/flac. The
following table shows which packages are used for each of the formats:

Formats       | Package
------------- | -------------
SID           | sidplay2 - http://sidplay2.sourceforge.net/
SNDH, sc68    | sc68 - http://sndplayer.atari.org/downloads.php
ogg           | vorbis-tools - http://www.vorbis.com
flac          | flac - https://xiph.org/flac/download.html

pytaglib required for song information in ogg/flac headers.