<template>
  <!-- Button trigger modal -->
  <MDBBtn color="primary" aria-controls="areaModal" @click="areaModal = true">
    ADD NEW <font-awesome-icon icon="fas fa-plus" />
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
            <!-- <input v-model="form.email" type="email" class="form-control" id="floatingEmail" placeholder="name@gmail.com">
          <label for="floatingEmail">Email address</label> -->
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
  components: {
    MDBModal,
    MDBModalHeader,
    MDBModalTitle,
    MDBModalBody,
    MDBModalFooter,
    MDBBtn,
  },
  setup() {
    const areaModal = ref(false);
    return {
      areaModal,
    };
  },
};
</script>
