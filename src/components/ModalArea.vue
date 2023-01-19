<template>
  <!-- Button trigger modal -->
  <button
    class="btn btn-primary"
    color="primary"
    aria-controls="areaModal"
    @click="areaModal = true"
  >
    <span v-if="edit == 'true'">EDIT <font-awesome-icon icon="fas fa-edit" /></span>
    <span v-if="edit == 'false'">ADD NEW <font-awesome-icon icon="fas fa-plus" /></span>
  </button>
  <MDBModal
    id="areaModal"
    tabindex="-1"
    labelledby="exampleModalLabel"
    v-model="areaModal"
  >
    <MDBModalHeader>
      <MDBModalTitle id="exampleModalLabel"> Area modal </MDBModalTitle>
    </MDBModalHeader>
    <MDBModalBody>
      <div class="container">
        <form>
          <div class="form-floating mb-3">
            <input
              v-model="areaName"
              type="text"
              class="form-control"
              id="areaName"
              placeholder="name@gmail.com"
            />
            <label for="areaName">Area name</label>
          </div>
          <div class="form-floating mb-3">
            <input
              v-model="areaAddress"
              type="text"
              class="form-control"
              id="areaAddress"
              placeholder="name@gmail.com"
            />
            <label for="areaAddress">Area address</label>
          </div>
          <div class="form-floating mb-3">
            <input
              v-model="areaLat"
              type="text"
              class="form-control"
              id="areaLat"
              placeholder="name@gmail.com"
            />
            <label for="areaLat">Area latitude</label>
          </div>
          <div class="form-floating mb-3">
            <input
              v-model="areaLon"
              type="text"
              class="form-control"
              id="areaLon"
              placeholder="name@gmail.com"
            />
            <label for="areaLon">Area longtitude</label>
          </div>
        </form>
      </div>
    </MDBModalBody>
    <MDBModalFooter>
      <button class="btn btn-primary" color="secondary" @click="areaModal = false">
        Close
      </button>
      <button class="btn btn-primary" color="primary" @click="saveArea">
        Save changes
      </button>
    </MDBModalFooter>
  </MDBModal>
</template>

<script>
import {
  MDBModal,
  MDBModalHeader,
  MDBModalTitle,
  MDBModalBody,
  MDBModalFooter,
} from "mdb-vue-ui-kit";
import { ref } from "vue";
export default {
  props: ["edit", "areaId", "name", "address", "latitude", "longitude"],
  data() {
    return {
      areaName: this.name || "",
      areaAddress: this.address || "",
      areaLat: this.latitude || "",
      areaLon: this.longitude || "",
    };
  },
  components: {
    MDBModal,
    MDBModalHeader,
    MDBModalTitle,
    MDBModalBody,
    MDBModalFooter,
  },
  mounted() {
  },
  setup() {
    const areaModal = ref(false);
    return {
      areaModal,
    };
  },
  methods: {
    saveArea() {
      let method;
      let payload = {
        areaId: this.areaId,
        areaName: this.areaName,
        address: this.areaAddress,
        latitude: this.areaLat,
        longitude: this.areaLon,
      };
      console.log("payload", payload);

      if (this.edit == "true") {
        // PATCH call to /areas
        console.log("PATCH");
        method = "PATCH";
      } else {
        // POST call to /areas
        console.log("POST");
        method = "POST";
      }

      this.$store
        .dispatch("callAPI", {
          method: method,
          endpoint: "areas",
          body: payload,
        })
        .then((response) => {
          console.log(response);
          this.areas = this.$store.dispatch("getAreas");
          this.areaModal = false;
        });
    },
  },
};
</script>
