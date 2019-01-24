#!/usr/bin/awk -f

# This is a simple conversion script for output from metar -d <ICAO_ID>
# Usage: metar -d khsv | convert.awk
# Please forgive the lazy variables....

{
    if ($1 == "Time")
    {
        offset = strftime("%z")/100
        tz = strftime("%Z")

        split($3, x, ":")
        y = (x[1]+offset+24)%24
        z = sprintf( "%02d:%d", y, x[2])
        r = gensub($3, z, 1)
        r = gensub(/UTC/,tz,1,r)
        print r
    }
    else if ($1 == "Temperature")
    {
        t = $3*9./5 + 32
        r = gensub($3, t, 1)
        r = gensub(/C/,"F",1,r)
        print r
    }
    else if ($1 == "Dewpoint")
    {
        t = $3*9./5 + 32
        r = gensub($3, t, 1)
        r = gensub(/C/,"F",1,r)
        print r
    }
    else print
}
