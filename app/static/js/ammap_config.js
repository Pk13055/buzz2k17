/**
 * SVG path for target icon
 */
var targetSVG = "M9,0C4.029,0,0,4.029,0,9s4.029,9,9,9s9-4.029,9-9S13.971,0,9,0z M9,15.93 c-3.83,0-6.93-3.1-6.93-6.93S5.17,2.07,9,2.07s6.93,3.1,6.93,6.93S12.83,15.93,9,15.93 M12.5,9c0,1.933-1.567,3.5-3.5,3.5S5.5,10.933,5.5,9S7.067,5.5,9,5.5 S12.5,7.067,12.5,9z";

/**
 * SVG path for plane icon
 */
var planeSVG = "m2,106h28l24,30h72l-44,-133h35l80,132h98c21,0 21,34 0,34l-98,0 -80,134h-35l43,-133h-71l-24,30h-28l15,-47";

/**
 * Create the map
 */
var map = AmCharts.makeChart("chartdiv", {
    "type": "map",
    "theme": "light",


    "dataProvider": {
        "map": "worldLow",
        "zoomLevel": 1,
        "zoomLongitude": 10,
        "zoomLatitude": 45,

        "lines": [{
            "id": "line1",
            "arc": -0.85,
            "alpha": 0.3,
            "latitudes": [28.7041, -33.8688, 35.6895, 55.7558, 48.8567, 43.8163, 34.3000, -34.6037, -33.9249, 30.5852],
            "longitudes": [77.1025, 151.2093, 139.6917, 37.6173, 2.3510, -79.4287, -118.15, -58.3816, 18.4241, 36.2384]
        }, {
            "id": "line2",
            "alpha": 0,
            "color": "#000000",
            "latitudes": [28.7041, -33.8688, 35.6895, 55.7558, 48.8567, 43.8163, 34.3000, -34.6037, -33.9249, 30.5852],
            "longitudes": [77.1025, 151.2093, 139.6917, 37.6173, 2.3510, -79.4287, -118.15, -58.3816, 18.4241, 36.2384]
        }],
        "images": [

            {
                "svgPath": targetSVG,
                "title": "About us - Start from India and fly across the world with felicity buzz",
                "contest": "about",
                "latitude": 28.7041,
                "longitude": 77.1025
            },
            {
                "svgPath": targetSVG,
                "title": "Gordian Knot - Fly to Sydney and beat turing.",
                "contest": "gordianknot",
                "latitude": -33.8688,
                "longitude": 151.2093
            },

            {
                "svgPath": targetSVG,
                "title": "Schedule - Fly to Tokyo and have a look at what's in store for you in these 3 days!",
                "contest": "schedule",
                "latitude": 35.6895,
                "longitude": 139.6917
            },


            {
                "svgPath": targetSVG,
                "title": "LitQuiz - Take a broomstick and fly to Moscow, for winter has come!",
                "contest": "litquiz",
                "latitude": 55.7558,
                "longitude": 37.6173
            },
            {
                "svgPath": targetSVG,
                "title": "Turn the coat: Fly to Paris and debate your heart out!",
                "contest": "debate",
                "latitude": 48.8567,
                "longitude": 2.3510
            },
            {
                "svgPath": targetSVG,
                "title": "CacheIn - Fly to Toronto and unlock the box of mystery, but only to find a new one ahead.",
                "contest": "cachein",
                "latitude": 43.8163,
                "longitude": -79.4287
            },
            {
                "svgPath": targetSVG,
                "title": "Meet the team - Take a ride to LA and party with the team!!",
                "contest": "team",
                "latitude": 34.3,
                "longitude": -118.15
            },
            {
                "svgPath": targetSVG,
                "title": "HackIn - Fly to Buenos Aires!!",
                "contest": "hackin",
                "latitude": -34.6037,
                "longitude": -58.3816
            },
            {
                "svgPath": targetSVG,
                "title": "Toast Masters - Discover the leader in you in Cape Town!!",
                "contest": "toastmasters",
                "latitude": -33.9249,
                "longitude": 18.4241
            },
            {
                "svgPath": targetSVG,
                "title": "Zombie Zone - Are you game to go Zombie in Jordan?!",
                "contest": "zombiezone",
                "latitude": 30.5852,
                "longitude": 36.2384
            },

            {
                "svgPath": planeSVG,
                "positionOnLine": 0,
                "color": "#000000",
                "alpha": 0.1,
                "animateAlongLine": true,
                "lineId": "line2",
                "flipDirection": true,
                "loop": true,
                "scale": 0.1,
                "positionScale": 1.3
            },

            {
                "svgPath": planeSVG,
                "positionOnLine": 0,
                "color": "#585869",
                "animateAlongLine": true,
                "lineId": "line1",
                "flipDirection": true,
                "loop": true,
                "scale": 0.09,
                "positionScale": 1.8
            }

        ]
    },

    "areasSettings": {
        "unlistedAreasColor": "#006666"
    },

    "imagesSettings": {
        "color": "#585869",
        "rollOverColor": "#585869",
        "selectedColor": "#585869",
        "pauseDuration": 0.2,
        "animationDuration": 3.5,
        "adjustAnimationSpeed": true
    },

    "linesSettings": {
        "color": "#585869",
        "alpha": 0.4
    },

    "export": {
        "enabled": true
    }

});