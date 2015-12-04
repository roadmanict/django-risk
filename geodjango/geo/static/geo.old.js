jQuery(document).ready(function () {
    $(document).foundation();

    var map;

    var options = {
        zoom: 3,
        center:  new google.maps.LatLng(53.215112686156, 6.5917110443111),
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true,
        styles: [{
            "featureType": "administrative.neighborhood",
            "elementType": "labels",
            "stylers": [{
              "visibility": "off"
            }]
              }, {
            "featureType": "administrative.land_parcel",
            "elementType": "labels",
            "stylers": [{
              "visibility": "off"
            }]
              }, {
            "featureType": "administrative.land_parcel",
            "elementType": "labels",
            "stylers": [{
              "visibility": "off"
            }]
              }, {
            "featureType": "administrative._area_level_1",
            "elementType": "labels",
            "stylers": [{
              "visibility": "off"
            }]
        }, {}]
    };

    var clickListenerFunction = function(event) {
        var lat = event.latLng.lat();
        var lng = event.latLng.lng();
        var get_country_url = "/api/get_country/" + lat + "/" + lng;
        console.log(get_country_url);
        $.get(get_country_url, function(data) {
            $modal.html(data.name).foundation('open');
        });
    };
    
    map = new google.maps.Map($('#map')[0], options);

    var $modal = $('#result');

    var bounds = {
        north: 44.599,
        south: 44.490,
        east: -78.443,
        west: -78.649
    };


    var drawingManager = new google.maps.drawing.DrawingManager({
        drawingMode: google.maps.drawing.OverlayType.RECTANGLE,
        drawingControl: false
    });


    google.maps.event.addListener(drawingManager, 'rectanglecomplete', function(rectangle) {
        var get_countries_url = "/api/get_countries_in_rectangle/" +
            rectangle.getBounds().getNorthEast().lat() + "/" +
            rectangle.getBounds().getNorthEast().lng() + "/" +
            rectangle.getBounds().getSouthWest().lat() + "/" +
            rectangle.getBounds().getSouthWest().lng();
        console.log(get_countries_url);
        $.get(get_countries_url, function(data) {
            var html = "";
            console.log(data);
            for(country in data) {
                html += data[country] + "<br />";
            }
            $modal.html(html).foundation('open');
        });
        rectangle.setMap(null);
    });

    $.get("/api/get_markers", function(data) {
        for(var key in data) {
            new google.maps.Marker({
                position: {lat: data[key].lat, lng: data[key].lon},
                map: map,
                title: data[key].description
            });
        }
    })

    $('#whatCountry').click(function(event) {
        map.addListener('click', clickListenerFunction);
    });

    $('#disableWhatCountry').click(function(event) {
        google.maps.event.clearListeners(map, 'click');
    });

    $('#drawManager').click(function(event) {
        drawingManager.setMap(map);
    });

    $('#removeDrawManager').click(function(event) {
        drawingManager.setMap(null);
    });

    $('#placeMarker').click(function(event) {
        map.addListener('click', function(event) {
            
        })
    });

    $('#disablePlaceMarker').click(function(event) {

    });
});

