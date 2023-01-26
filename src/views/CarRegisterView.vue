<template>
  <div class="container mt-5 mx-auto row">
    <div class="col-lg-7"></div>
    <div class="col-lg-5 action-prompt m-auto">
      <h3 class="text-center">NEW CAR</h3>
      <hr />
      <!-- <form action="imageUploaded" enctype="multipart/form-data"> -->
      <div id="imageInput">
        <p>Simply scan your car's license plate, and have it registered automatically!</p>
        <input id="plateImage" class="form-control" type="file" accept="image/*" @change="imageUploaded" />

        <img id="previewImg" src="" width="200" alt="Plate picture" />
      </div>

      <!-- </form> -->
      <form ref="newCarForm">

        <div id="manualInput">
          <p>Or manually input the info here:</p>
          <label for="numberPlate">Number plate</label>
          <br />
          <input name="numberPlate" id="numberPlate" class="form-control" type="text" pattern="[A-Z]{2}[0-9]{5}"
            title="Please follow Danish number plate structure" v-model="inputNumberplate" />
        </div>

        <!-- <button class="btn btn-primary" @click="getPlateInput">Search for car</button> -->

        <div v-if="$store.state.searching == true" id="searchStatus" class="mt-4 d-flex">
          <span>Searching...</span>
          <div class="loader"></div>

        </div>

        <br />

        <div v-if="$store.state.carInfo.data && $store.state.searching == false" id="carInfo">
          <p>Brand: {{ $store.state.carInfo.data.brand }}</p>
          <p>Model: {{ $store.state.carInfo.data.model }}</p>
          <p v-if="$store.state.carInfo.data.body_type">Type: {{ $store.state.carInfo.data.body_type.name }}</p>
        </div>

        <button class="btn btn-primary" @click="submitNewCar" :disabled="$store.state.searching == true">Submit</button>
      </form>
    </div>
  </div>
</template>

<style scoped>
#previewImg {
  display: none;
}
</style>

<script>
export default {
  data() {
    return {
      inputNumberplate: "",
      carModel: "",
      carBrand: "",
      response: "",
      numberPlatePattern: /[A-Z]{2}[0-9]{5}/g,
    };
  },
  watch: {
    inputNumberplate(newNumber) {
      // When manual input of numberplate changes
      this.inputNumberplate = this.inputNumberplate.toUpperCase();

      if (this.numberPlatePattern.test(newNumber) === true) {
        this.$store.dispatch('licensePlateLookup', newNumber);


      } else {
        console.log("NOT RIGHT PATTERN");
        this.$store.state.carInfo = {};
      }
    },
  },
  methods: {

    imageUploaded() {
      // let blob = e.target.files[0];
      let image = document.querySelector('#plateImage').files[0];
      this.$store.dispatch('detectLicensePlate', image);
    },
    submitNewCar() {
      let payloads = [
        {
          method: "POST",
          endpoint: "regLicenseplates",
          body: {
            licenseplate: this.inputNumberplate,
            brand: this.$store.state.carInfo.data.brand,
            model: this.$store.state.carInfo.data.model,
            type: ""
          }
        },
        {
          method: "POST",
          endpoint: "userLicenseplates",
          body: {
            userId: this.$store.state.user.userId,
            token: this.$store.state.user.token,
            licenseplate: this.inputNumberplate,
          }
        }
      ]

      // Not all cars have a body type
      try {
        payloads[0].body.type = this.$store.state.carInfo.data.body_type.name;
      } catch (error) {
        console.log("No body type");
        payloads[0].body.type = "Undefined";
      }

      payloads.forEach(payload => {
        this.$store.dispatch('callAPI', payload) // Post new car to API
        .then(() => {
          // this.$router.push({ name: "Home" });
          console.log("Car added", payload);
        })
        .catch((error) => {
          console.log(error);
        });
      });      
    }
  }
};
</script>