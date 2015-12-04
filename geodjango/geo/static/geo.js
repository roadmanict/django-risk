require(["esri/map", "dojo/domReady!"], function(Map) {
  var map = new Map("map", {
    center: [6.5917110443111, 53.215112686156],
    zoom: 4,
    basemap: "topo"
  });
});