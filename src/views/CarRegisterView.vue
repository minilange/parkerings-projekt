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

        <img id="previewImg" src="" width="200" />
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

        <button class="btn btn-primary" @click="submitNewCar">Submit</button>
      </form>
    </div>
  </div>
</template>

<script>
// import { mapActions } from "vuex";

// const fileTypes = [
//   "image/apng",
//   "image/bmp",
//   "image/gif",
//   "image/jpeg",
//   "image/pjpeg",
//   "image/png",
//   "image/svg+xml",
//   "image/tiff",
//   "image/webp",
//   "image/x-icon",
// ];

// function validFileType(file) {
//   return fileTypes.includes(file.type);
// }
// async getPlateInput() {
//       CALL API WITH event.target.value as parameter
//       this.response = "Searching";
//       this.carBrand = "";
//       this.carModel = "";

//       console.log(event.target.value);
//       try {
//         const res = await fetch("");
//         this.response = (await res.json()).answer;
//         this.response = "SEARCH COMPLETED";
//         this.carBrand = "TEST BRAND";
//         this.carModel = "TEST MODEL";
//         console.log(this.response);
//       } catch (error) {
//         console.log(error);
//         this.response = "Error: " + error;
//       }
//     },
//     getPlate(event) {
//       try {
//         const picture = document.getElementById("plateImage");
//         console.log(picture);

//         if (picture.value != "") {
//           const curFiles = picture.files;
//           console.log(curFiles);
//           if (curFiles.length === 0) {
//             console.log("No files currently selected for upload");
//           } else {
//             for (const file of curFiles) {
//               if (validFileType(file)) {
//                 CALL API!

//                 let img = document.getElementById("previewImg");
//                 img.src = URL.createObjectURL(file);
//                 console.log(file);
//               } else {
//                 console.log("NOT A VALID FILE");
//               }
//             }
//           }
//         } else {
//           alert("Please select a picture of your number plate");
//         }
//       } catch (error) {
//         console.log("Input picture: " + error);
//       }

//       console.log(event.target.name);
//     },
//   },


import axios from "axios";

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

    imageUploaded(e) {
      console.log(e)
      // let blob = e.target.files[0];
      let blob = document.querySelector('#plateImage').files[0];
      console.log(blob)
      let formData = new FormData();
      formData.append("fileToUpload", blob);

      // Call API
      console.log(formData);
      formData.append("file", blob);
      axios.post("/api/uploadFile", formData)
        .then(function (result) {
          console.log(result);
        }, function (error) {
          console.log(error);
        });
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