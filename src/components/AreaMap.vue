<template>
        <!-- <MapFeatures
    :fetchCoords="fetchCoords"
    :coords="coords"
    @toggleSearchResults="toggleSearchResults"
    @getGeolocation="getGeolocation"
    @plotResult="plotResult"
    @removeResult="removeResult"
    :searchResults="searchResults"
    class="w-full md:w-auto absolute md:top-[40px] md:left-[60px] z-[2]"
/> -->
        <div id="mapid"></div>

</template>

<style scoped>
#mapid {
    min-height: 200px;
    min-width: 100px;
    z-index: 0;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.2);
}
/* @media (min-width: 991px) {
    #mapid {
        min-height: 200px;
    }
} */
</style>

<script>
import leaflet from "leaflet";
import { onMounted, ref } from "vue";
// import MapFeatures from "../components/MapFeatures.vue";
export default {
    name: "AreaMap",
    components: {  },
    methods: {
    },
    setup() {
        let map;
        onMounted(() => {
            // init map
            map = leaflet
                .map("mapid", {
                    zoomControl: false,
                })
                .setView([28.538336, -81.379234], 10);
            // add tile layers
            leaflet
                .tileLayer(
                    `https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=${"pk.eyJ1IjoidG9ieWpjb2RlIiwiYSI6ImNsY3N4Z2xjMzAxemQzb25zY3RzYWV5NjEifQ.hr_qqO7-Z3nNwVhqnVWxwg"}`,
                    {
                        maxZoom: 18,
                        id: "mapbox/streets-v11",
                        tileSize: 512,
                        zoomOffset: -1,
                        accessToken: "pk.eyJ1IjoidG9ieWpjb2RlIiwiYSI6ImNsY3N4Z2xjMzAxemQzb25zY3RzYWV5NjEifQ.hr_qqO7-Z3nNwVhqnVWxwg",
                    }
                )
                .addTo(map);
            map.on("moveend", () => {
                closeSearchResults();
            });
            // get users location
            // getGeolocation();

            let coordinates = {
                "coordinates": [
                    10.126,
                    56.114
                ],
            }
            plotResult(coordinates);
        });
        const coords = ref(null);
        const fetchCoords = ref(null);
        const geoMarker = ref(null);
        const geoError = ref(null);
        const geoErrorMsg = ref(null);
        const getGeolocation = () => {
            // if function is called, only run if we dont have coords
            if (!coords.value) {
                // check to see if we have coods in session sotrage
                if (sessionStorage.getItem("coords")) {
                    coords.value = JSON.parse(sessionStorage.getItem("coords"));
                    plotGeoLocation(coords.value);
                    return;
                }
                // else get coords from geolocation API
                fetchCoords.value = true;
                navigator.geolocation.getCurrentPosition(setCoords, getLocError);
                return;
            }
            // otherwise, remove location
            coords.value = null;
            sessionStorage.removeItem("coords");
            map.removeLayer(geoMarker.value);
        };
        const setCoords = (pos) => {
            // stop fetching
            fetchCoords.value = null;
            // set coords in session storage
            const setSessionCoords = {
                lat: pos.coords.latitude,
                lng: pos.coords.longitude,
            };
            sessionStorage.setItem("coords", JSON.stringify(setSessionCoords));
            // set ref coords value
            coords.value = setSessionCoords;
            plotGeoLocation(coords.value);
        };
        const getLocError = (error) => {
            // stop fetching coords
            fetchCoords.value = null;
            geoError.value = true;
            geoErrorMsg.value = error.message;
        };
        const plotGeoLocation = (coords) => {
            // create custom marker
            const customMarker = leaflet.icon({
                iconUrl: require("../assets/map-marker-red.svg"),
                iconSize: [35, 35],
            });
            // create new marker with coords and custom marker
            geoMarker.value = leaflet
                .marker([coords.lat, coords.lng], { icon: customMarker })
                .addTo(map);
            // set map view to current location
            map.setView([coords.lat, coords.lng], 10);
        };
        const resultMarker = ref(null);
        const plotResult = (coords) => {
            console.log('plot result', coords)
            // If there is already a marker, remove it. Only allow 1
            if (resultMarker.value) {
                map.removeLayer(resultMarker.value);
            }
            const customMarker = leaflet.icon({
                iconUrl: require("../assets/map-marker-blue.svg"),
                iconSize: [35, 35], // size of the icon
            });

            console.log('marker', [coords.coordinates[1], coords.coordinates[0]]);

            resultMarker.value = leaflet
                .marker([coords.coordinates[1], coords.coordinates[0]], { icon: customMarker })
                .addTo(map);
            map.setView([coords.coordinates[1], coords.coordinates[0]], 13);
        };
        const removeResult = () => {
            map.removeLayer(resultMarker.value);
        };
        const closeGeoError = () => {
            geoErrorMsg.value = null;
            geoError.value = null;
        };
        const searchResults = ref(null);
        const toggleSearchResults = () => {
            searchResults.value = !searchResults.value;
        };
        const closeSearchResults = () => {
            searchResults.value = null;
        };
        return {
            geoError,
            closeGeoError,
            geoErrorMsg,
            fetchCoords,
            coords,
            getGeolocation,
            plotResult,
            searchResults,
            toggleSearchResults,
            closeSearchResults,
            removeResult,
        };
    },
};
</script>