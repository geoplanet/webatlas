{% load leaflet_tags %}

         var map = L.map('map', {
                        center: [66, -145],
                        zoom: 5,
                        maxZoom: 20,
                        zoomControl: false
                });
   	var zoomControl = L.control.zoom ().addTo(map);
	var RedIcon = L.Icon.extend({
          options: {
            	    iconUrl: '/static/css/images/location-marker.png',
		    iconSize: [30,30] }
         });
        var redIcon = new RedIcon;
	var myIcon = L.divIcon({html: '<i class="fa fa-map-marker" style="color:darkgreen;"></i>'});


	var defaultLayer = L.tileLayer.provider('Stamen.Watercolor',{ maxZoom:6.9 }).addTo(map);
        var defaultImageLayer = L.tileLayer.provider('Esri.WorldImagery',{ minZoom:7.0, maxzoom:11 }).addTo(map);
        var transport_layer  = L.tileLayer.wms("http://ows.geobase.ca/wms/geobase_en?service=wms", {
                layers: 'nrn:roadnetwork,nrwn:track',
                format: 'image/png',
                transparent: true,
                reuseTiles: true,
                unloadInvisibleTiles: false,
                attribution: "Geobase © Minister of Natural Resources Canada"
        }).addTo(map);
   	var dataurl = '{{ object.dataurl }}';
        var markerCluster =  L.markerClusterGroup({ spiderfyOnMaxZoom: false, showCoverageOnHover: true, zoomToBoundsOnClick: false, disableClusteringAtZoom: 10  });        

        $.getJSON(dataurl, function (data) {
	    	var mylayer = L.geoJson(data, {
                      pointToLayer: function(feature, latlng) {
                                	return L.marker(latlng,{icon: redIcon});
                        	    }, 
 			onEachFeature: onEachFeature
		     });

//        map.addLayer(mylayer);
   	map.fitBounds(mylayer.getBounds());
 var searchControl =  new L.Control.Search({layer: markerCluster, propertyName: 'other_name', zoom: 12, initial: false, autoCollapse:true}).addTo(map);
 //   map.addControl( new L.Control.Search({layer: mylayer, propertyName: 'other_name', zoom: 9, initial: false, autoCollapse:true}) );

});


  function onEachFeature(feature, layer){
       layer.on({mouseover: highlightFeature, click:zoomToFeature});
      	markerCluster.on('clusterclick', function (a) {a.layer.spiderfy(); });
        markerCluster.addLayer(layer);        
        map.addLayer(markerCluster);

	function highlightFeature (e){
        	e.target.bindPopup("Name: <b>"+ feature.properties.other_name +"</b>").openPopup();
        	};

       function zoomToFeature(e) {
		var lonlat = Array(feature.geometry.coordinates[1],feature.geometry.coordinates[0]);
               // alert (lonlat);
 	        map.setView(lonlat,10);
  //          map.fitBounds(e.target.getBounds());
        }  //End of onEachFeature
  }