<template>
  <div class="h-screen relative">
   <div id="map" class="h-full z-[1]"></div>
  </div>
</template>

<script>
import leaflet from "leaflet";
import { onMounted } from "vue";

export default {
  name: "AreaView",
  components: {},
  setup() {
    let map;
    onMounted(() => {
      // init the map right here
      map = leaflet.map('map').setView([51.505, -0.09], 13);

       // add tile layers
      leaflet
        .tileLayer(  // add vores api :=(
          `https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=${process.env.VUE_APP_API_KEY}`,
          {
            maxZoom: 18,
            id: "mapbox/streets-v11",
            tileSize: 512,
            zoomOffset: -1,
            accessToken: process.env.VUE_APP_API_KEY,
          }
        )
        .addTo(map);
    })
  },
};
</script>

<style>
.action-prompt {
  height: 100%;

}
</style>