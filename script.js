let map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 44.475883,lng: -73.212074},
    zoom: 15
  });
}
let champlain = {lat: 44.4731, lng: -73.2041};

let markerOne = new google.maps.Marker({
  position: uluru,
  map: map
});

/*
// FOR SHOWING CURRENT LOCATION UNABLE TO USE CURRENTLY VS CODE DOESNT SUPPORT
//GEOLOCATION NEED TO HOST WEBSITE TO USE
let infoWindow = new google.maps.InfoWindow;

if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      let pos = {
        lat: 44.4731, //position.coords.latitude,
        lng: -73.2041 //position.coords.longitude
      };

      infoWindow.setPosition(pos);
      infoWindow.setContent('Location found.');
      infoWindow.open(map);
      map.setCenter(pos);
    }, function() {
      handleLocationError(true, infoWindow, map.getCenter());
    });
  } else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
  }

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(browserHasGeolocation ?
                                                `Error: Not working Chief`:
                                                `Error: Browser not supporting it.`
    );
    infoWindow.open(map);
    }
*/
