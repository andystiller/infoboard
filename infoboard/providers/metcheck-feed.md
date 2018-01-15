# JSON file structure

<table>
    <tr>
        <td><i>
        {<br/>
            "metcheckData": {<br/>
            "forecastLocation": {<br/>
            "forecast": [         <br/>
            {                      <br/>
                "temperature": "9",   <br/>
                "dewpoint": "6",      <br/>
                "rain": "0.05",          <br/>
                "freezinglevel": "1553",   <br/>
                "uvIndex": "0",           <br/>
                "totalcloud": "50",       <br/>
                "lowcloud": "35",     <br/>
                "medcloud": "0",       <br/>
                "highcloud": "0",       <br/>
                "humidity": "88",        <br/>
                "windspeed": "4",          <br/>
                "meansealevelpressure": "1020.41", <br/>
                "windgustspeed": "9",         <br/>
                "winddirection": "89",       <br/>
                "windletter": "E",        <br/>
                "icon": "FA",             <br/>
                "iconName": "Fair",        <br/>
                "chanceofrain": "85",        <br/>
                "chanceofsnow": "10",        <br/>
                "dayOfWeek": "5",          <br/>
                "weekday": "Thursday",      <br/>
                "sunrise": "6:28",          <br/>
                "sunset": "17:14",          <br/>
                "dayOrNight": "N",            <br/>
                "utcTime": "2016-10-13T06:00:00.00"  <br/>
            }                          <br/>
        ,                     <br/>
        .... Continue For Each Time Step Until...<br/>
        ],            <br/>
        "continent": "EUROPE", <br/>
        "country": "UK",       <br/>
        "location": "Sunderland",<br/>
        "latitude": 54.9,         <br/>
        "longitude": -1.4,        <br/>
        "timezone": 0             <br/>
        }                              <br/>
        },                             <br/>
        "feedCreation": "2016-10-13T08:59:17.00",  <br/>
        "feedCreator": "Metcheck.com",       <br/>
        "feedModel": "GHX",           <br/>
        "feedModelRun": "00Z",        <br/>
        "feedModelRunInitialTime": "2016-10-13T00:00:00.00",<br/>
        "feedResolution": "0.01"     <br/>
}                                 <br/>
        </i>
        </td>
        <td>
            <br/>
            <br/>
            <br/>
            degrees celcius<br/>
            degrees celcius     <br/>
            mm/hr         <br/>
            metres   <br/>
            UV Scale 1-10        <br/>
            percent       <br/>
            percent    <br/>
            percent     <br/>
            percent      <br/>
            percent    <br/>
            miles per hour       <br/>
            millibars <br/>
            miles per hour           <br/>
            bearing 0-359 degrees     <br/>
            e.g E=East, ESE=EastSouthEast     <br/>
            percent      <br/>
            percent      <br/>
            1 (Sunday) to 7 (Saturday)  <br/>
            <br/>
            Local Time        <br/>
            Local Time        <br/>
            Forecast Time Step (Local Time) <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br />
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            Difference To UK Time <br/>
            <br/>
            <br/>
            UK Time Feed Created <br/>
            Us :-)   <br/>
            Model Used       <br/>
            Model Run Used     <br/>
            <br/>
            <br/>
            <br/>
        </td>
    </tr>
</table>

## Update Times

The GHX model is updated at around 08:40Z, 20:40Z

## TimeSteps

6-120 hours : 1 Hour Intervals
123-240 hours : 3 Hour Intervals

## Possible Weather Variables

<table width="100%">
    <tr>
        <td >Weather</td>
        <td >Weather Code (Day/Night)</td>
    </tr>
    <tr>
        <td>Sunny/Clear</td>
        <td>SU / NSU</td>
    </tr>
    <tr>
        <td>Fair</td>
        <td>FA / NFA</td>
    </tr>
    <tr>
        <td>Mostly Cloudy</td>
        <td>PC / NPC</td>
    </tr>  <tr>
        <td>Cloudy</td>
        <td>CL / NCL</td>
    </tr>  <tr>
        <td>Mist/Fog</td>
        <td>FG / NFG</td>
    </tr>
    <tr>
        <td>Light Rain</td>
        <td>LR / NLR</td>
    </tr>
    <tr>
        <td>Sleet Showers <font color="red">NEW</font></td>
        <td>SL / NSL</td>
    </tr>
    <tr>
        <td>Hazy/High Cloud <font color="red">NEW</font></td>
        <td>HZ / NHZ</td>
    </tr>
    <tr>
        <td>ThunderSnow <font color="red">NEW</font></td>
        <td>TS / NTS</td>
    </tr>
    <tr>
        <td>ThunderSleet <font color="red">NEW</font></td>
        <td>TL / NTL</td>
    </tr>
    <tr>
        <td>Heavy Rain</td>
        <td>HR / NHR</td>
    </tr>
    <tr>
        <td>Intermittent Rain</td>
        <td>RO / NRO</td>
    </tr>
    <tr>
        <td>Drizzle</td>
        <td>DZ / NDZ</td>
    </tr>
    <tr>
        <td>Rain Showers</td>
        <td>SH / NSH</td>
    </tr>
    <tr>
        <td>Light Snow</td>
        <td>LS / NLS</td>
    </tr>
    <tr>
        <td>Light Sleet</td>
        <td>LL / NLL</td>
    </tr>
    <tr>
        <td>Heavy Snow</td>
        <td>HS / NHS</td>
    </tr>
    <tr>
        <td>Heavy Sleet</td>
        <td>HL / NHL</td>
    </tr>
    <tr>
        <td>Thunderstorms</td>
        <td>TH / NTH</td>
    </tr>
    <tr>
        <td>Wet &amp; Windy</td>
        <td>WW / NWW</td>
    </tr>
    <tr>
        <td>Partly Cloudy</td>
        <td>PC / NPC</td>
    </tr>
    <tr>
        <td>Hail</td>
        <td>HI / NHI</td>
    </tr>
    <tr>
        <td>Snow Showers</td>
        <td>SS / NSS</td>
    </tr>
    <tr>
        <td>Dry &amp; Windy</td>
        <td>WI / NWI</td>
    </tr>
</table>