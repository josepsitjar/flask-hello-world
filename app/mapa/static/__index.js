import 'ol/ol.css';
import Map from 'ol/Map';
import OSM from 'ol/source/OSM';
import TileLayer from 'ol/layer/Tile';
import View from 'ol/View';

var map = new Map({
    layers: [
        new TileLayer({
            source: new OSM(),
    }) ],
    target: 'map',
    view: new View({
        center: [313649.79,5157717.47],
        zoom: 8,
    }),
});