# chipmusic-convert

Python script to conveniently convert different chipmusic formats into
wav/ogg/flac.

## Supported:
* Commodore64 SID
* Atari SNDH
* Atari SAP
* sc68 format

## Planned support:
* Amiga MOD
* NSF
* SPC
* GB*

## Chipmusic archives:
* http://asma.atari.org/ - Atari SAP Music Archive
* http://sndh.atari.org/ - Atari ST YM2149 Archive
* http://www.hvsc.de/ - High Voltage SID Collection
* http://modarchive.org/ - The Mod Archive
* http://sc68.atari.org/musics.html - sc68 music collection
* http://www.tphf.karoo.net/zhmain.htm - Grazey's Zak Hacks
* http://vgmusic.com/ - Video Game Music Archive
* http://www.vgmpf.com/Wiki/ - Videogame Music Preservation Foundation
* http://www.arc-nova.org/ - Arc-Nova archive
* http://gilgalad.arc-nova.org/NSF-Archive/ - gilgalad NSFs at Arc-Nova
* http://www.zophar.net - Zophar's domain
* http://akumunsf.good-evil.net/ - AKumu NSF Archive
* http://www.snesmusic.org/v2/ - SNESmusic SPC archive
* http://www.snesmusic.org/hoot/gbs/ - GBS Penultimate Archive
* http://www.snesmusic.org/hoot/kingshriek/ - Kingshriek's rip page
* http://nsf.joshw.info/ - NSF archive at joshw.info
* http://patpend.net/ftp/music/ - Patent Pending


## Other chipmusic sites:
* http://www.creamhq.de/ymrockerz/index.php - YM Rockerz
* http://www.angelfire.com/nc/ugetab/ - ugetab music and resources

If you know of any chipmusic archives or pages that are missing here,
please let me know!

## Required software by format

chipmusic-convert relies on different software packages to do the
actual conversion from the chipmusic formats to wav/ogg/flac. The
following table shows which packages are used for each of the formats:

Formats       | Package
------------- | -------------
SID           | sidplayfp - https://bel.fi/alankila/c64-sw/index-cpp.html
SNDH, sc68    | sc68 - http://sndplayer.atari.org
SAP           | asapconv - http://asap.sf.net
ogg           | vorbis-tools - http://www.vorbis.com
flac          | flac - https://xiph.org/flac

pytaglib required for song information in ogg/flac headers.

## Resources
* MOD software on linux-sound: http://linux-sound.org/mod.html
* sidplay2 - http://sidplay2.sf.net

