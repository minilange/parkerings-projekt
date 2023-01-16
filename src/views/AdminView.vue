<template>
  <div class="container p-5">
    <div class="row action-prompt" style="height: 100%">
      <div class="col-lg-12">
        <div class="card mb-4 profile">
          <div class="card-body text-center">
            <h5 class="mb-0">Parkings</h5>
            <table class="table table-responsive">
              <thead>
                <tr>
                  <th scope="col">Parking ID</th>
                  <th scope="col">User</th>
                  <th scope="col">Car</th>
                  <th scope="col">Start</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">1</th>
                  <td>Test user</td>
                  <td>Test car</td>
                  <td>12-05-2022</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <div class="col-lg-12">
        <div class="card mb-4">
          <div class="card-body">
            <h5 class="mb-0">Registered cars</h5>
            <table class="table table-responsive">
              <thead>
                <tr>
                  <th scope="col">Number plate</th>
                  <th scope="col">Brand</th>
                  <th scope="col">Model</th>
                  <th scope="col">Year</th>
                  <th scope="col">Type</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="car in $store.state.admin.cars" :key="car">
                  <th scope="row">{{ car.licenseplate }}</th>
                  <td>{{ car.brand }}</td>
                  <td>{{ car.model }}</td>
                  <td>[CAR YEAR]</td>
                  <td>
                    {{ car.type }}
                    <!-- <img :src="require(`../assets/carTypes/${carTypes[car.type]}`)" style="float: right" height="22"
                      width="50" alt="" /> -->
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <div class="col-lg-12">
        <div class="col-md-12">
          <div class="card">
            <div class="card-body">
              <!-- <h5 class="mb-0">Users</h5>

              <table class="table">
                <thead>
                  <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Email</th>
                    <th scope="col">Phone</th>
                    <th scope="col"></th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <th scope="row">Test user</th>
                    <td>test@test.com</td>
                    <td>+45 11223344</td>
                    <td></td>
                  </tr>
                </tbody>
              </table> -->
              <h5 class="mb-0">Areas</h5>

              <table class="table table-responsive">
                <thead>
                  <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Name</th>
                    <th scope="col">Adress</th>
                    <th scope="col">Latitude</th>
                    <th scope="col">Longtitude</th>
                    <th scope="col">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="area in $store.state.admin.areas" :key="area">
                    <th scope="row">{{ area.areaId }}</th>
                    <td>{{ area.areaName }}</td>
                    <td>{{ area.address }}</td>
                    <td>{{ area.latitude }}</td>
                    <td>{{ area.longitude }}</td>
                    <td>
                      <!-- <button class="btn btn-primary" @click="editArea(area.areaId)">
                        EDIT <font-awesome-icon icon="fas fa-edit" />
                      </button> -->
                      <Modal
                        edit="true"
                        :areaId="area.areaId"
                        :name="area.areaName"
                        :address="area.address"
                        :latitude="area.latitude"
                        :longitude="area.longitude"
                      />
                    </td>
                  </tr>

                  <tr>
                    <td colspan="6" class="d-flex justify-content-center">
                      <Modal edit="false" />
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Modal from "@/components/ModalArea.vue";

export default {
  data() {
    return {
      cars: [],
      users: [],
      parkings: [],
      selected: {},
    };
  },
  watch: {},
  components: {
    Modal,
  },
  mounted() {
    this.cars = this.$store.dispatch("getCars");
    this.areas = this.$store.dispatch("getAreas");
    this.parkings = this.$store.dispatch("getParkings");
  },
};
</script>
