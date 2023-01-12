<template>
  <!-- Button trigger modal -->
  <MDBBtn color="primary" aria-controls="areaModal" @click="areaModal = true">
    <span v-if="edit == 'true'">EDIT <font-awesome-icon icon="fas fa-edit" /></span>
    <span v-if="edit == 'false'">ADD NEW <font-awesome-icon icon="fas fa-plus" /></span>
  </MDBBtn>
  <MDBModal
    id="areaModal"
    tabindex="-1"
    labelledby="exampleModalLabel"
    v-model="areaModal"
  >
    <MDBModalHeader>
      <MDBModalTitle id="exampleModalLabel"> Modal title </MDBModalTitle>
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
      <MDBBtn color="secondary" @click="areaModal = false">Close</MDBBtn>
      <MDBBtn color="primary">Save changes</MDBBtn>
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
  MDBBtn,
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
    MDBBtn,
  },
  mounted() {
    console.log(this.areaId);
  },
  setup() {
    const areaModal = ref(false);
    return {
      areaModal,
    };
  },
};
</script>
