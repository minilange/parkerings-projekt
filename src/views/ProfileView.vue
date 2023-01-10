<template>
  <div class="container p-5">
    <div class="row action-prompt">
      <div class="col-lg-4">
        <div class="card mb-4 profile">
          <div class="card-body text-center">
            <img
              src="../assets/user-icon.png"
              alt="avatar"
              class="rounded-circle img-fluid"
              style="width: 154px"
            />
            <h5 class="my-2">[Name]</h5>
          </div>
        </div>
        <div class="card mb-4 mb-lg-0 registered-cars">
          <div class="card-body p-0">
            <ul class="list-group list-group-flush rounded-3">
              <li class="list-group-item text-center align-items-center p-3">
                <i class="fas fa-globe fa-lg text-warning"></i>
                <h5 class="mb-0">REGISTERED CARS:</h5>
              </li>
              <div v-if="registeredCars.length > 0">
                <li class="list-group-item p-3" v-for="car in registeredCars" :key="car">
                  <p class="mb-0">
                    {{ car.brand }} - {{ car.model }} - {{ car.licenseplate }}
                    <img
                      :src="require(`../assets/carTypes/${carTypes[car.type]}`)"
                      style="float: right"
                      height="22"
                      width="50"
                      alt=""
                    />
                  </p>
                </li>
              </div>
              <div v-else>
                <li class="list-group-item p-3">
                  <p class="mb-0">You don't have any registered cars yet...</p>
                </li>
              </div>
            </ul>
          </div>
        </div>
      </div>
      <div class="col-lg-8">
        <div class="card mb-4">
          <div class="card-body">
            <div class="row">
              <div class="col-sm-3">
                <p class="mb-0">First Name:</p>
              </div>
              <div class="col-sm-9">
                <p class="mb-0">{{ user.firstname }}</p>
              </div>
            </div>
            <hr />
            <div class="row">
              <div class="col-sm-3">
                <p class="mb-0">Last Name:</p>
              </div>
              <div class="col-sm-9">
                <p class="mb-0">{{ user.lastname }}</p>
              </div>
            </div>
            <hr />
            <div class="row">
              <div class="col-sm-3">
                <p class="mb-0">Email:</p>
              </div>
              <div class="col-sm-9">
                <p class="mb-0">{{ user.email }}</p>
              </div>
            </div>
            <hr />
            <div class="row">
              <div class="col-sm-3">
                <p class="mb-0">Mobil:</p>
              </div>
              <div class="col-sm-9">
                <p class="mb-0">{{ user.mobile }}</p>
              </div>
            </div>
          </div>
        </div>

        <div class="col-md-12">
          <div class="card">
            <div class="card-body">
              <h5 class="mb-0">LATEST PARKING:</h5>
              <div v-if="latestParking.date != ''">
                <li class="list-group-item py-3">
                  <p class="mb-0">Date:</p>
                  <p class="mb-0">{{ latestParking.date }}</p>
                </li>
                <li class="list-group-item py-3">
                  <p class="mb-0">Location:</p>
                  <p class="mb-0">{{ latestParking.location }}</p>
                </li>
                <li class="list-group-item py-3">
                  <p class="mb-0">Cost:</p>
                  <p class="mb-0">{{ latestParking.date }}</p>
                </li>
              </div>
              <div v-else>
                <p class="my-3">You don't have any parkings yet...</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
h5,
p {
  color: black !important;
}

@media (max-width: 991px) {
}

.action-prompt {
  height: auto;
}
</style>

<script>
import axios from "axios";

export default {
  data() {
    return {
      user: {
        firstname: "",
        lastname: "",
        email: "",
        mobile: "",
        address: "",
      },
      registeredCars: [],
      latestParking: {
        date: "",
        location: "",
        cost: "",
      },
      carTypes: {
        Stationcar: "Stationcar.png",
        Hatchback: "Hatchback.png",
        Sedan: "Sedan.png",
        Cabriolet: "Cabriolet.png",
        Coupe: "Sedan.png",
        "3-hjulet, åben": "Sedan.png",
        "3-hjulet, lukket": "Sedan.png",
        "Stationcar-picup": "Stationcar.png",
        "Uden karrosseri": "Sedan.png",
        Undefined: "Sedan.png",
      },
    };
  },
  watch: {},

  mounted() {
    axios
      .get(this.$store.state.api + "/userLicenseplates/", {
        params: {
          userId: 1,
        },
      })
      .then((response) => {
        this.registeredCars = response.data;
      })
      .catch((error) => {
        console.warn("userLicenseplates", error);
      });
  },
};
</script>
