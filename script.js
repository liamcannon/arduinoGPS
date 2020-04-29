//var ws = new WebSocket("fuzytech.com:47001");
//ws.onmessage = function (event) {
 // createMarker(event.data[0], event.data[1]);

fetch("http://fuzytech.com:47001/points.json")
  .then((response) =>{
    return response.json();
  })
  .then((data) => {
    console.log(data);
  });

function initMap() {
  var test = {lat: 43.207010, lng: -70.774210}

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 15,
    center: test
  });
  var marker = new google.maps.Marker({
    position: test,
    map: map
  });
}

function createMarker(lat, lng) {
  let temp = {lat: lat, lng: lng};
    marker = new google.maps.Marker({
      position: temp,
      center: test
    });
}






