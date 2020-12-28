//Full screen map view
var mapId = document.getElementById('map');
function fullScreenView() {
    if (document.fullscreenElement) {
        document.exitFullscreen()
    } else {
        mapId.requestFullscreen();
    }
}

//Leaflet browser print function
L.control.browserPrint({ position: 'topright' }).addTo(map);

//Leaflet search
L.Control.geocoder().addTo(map);


//Leaflet measure
L.control.measure({
    primaryLengthUnit: 'kilometers',
    secondaryLengthUnit: 'meter',
    primaryAreaUnit: 'sqmeters',
    secondaryAreaUnit: undefined
}).addTo(map);

//zoom to layer
$('.zoom-to-layer').click(function () {
    map.setView([38.8610, 71.2761], 7)
})






    // var overlayMaps = {};
    // {% for s in shp %}

    // var {{ s.name }} = L.tileLayer.wms('http://localhost:8080/geoserver/wms', {
    //     layers: '{{s.name}}',
    //     transparent: true,
    //     format: "image/png",
    // }).addTo(map);
    // overlayMaps['{{s.name}}'] = {{ s.name }}


    // {% endfor %}


    // L.control.layers(baseMaps, overlayMaps, { collapsed: false, position: 'topleft' }).addTo(map);