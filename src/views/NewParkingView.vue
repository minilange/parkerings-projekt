<template>
  <!-- <TimeDial /> -->
  <div class="container mt-5 mx-auto row">
    <div class="col-lg-7 action-prompt m-auto">
      <h3 class="text-center">NEW PARKING</h3>
      <hr />

      <div id="multi-step-form-container">
        <!-- Step Wise Form Content -->
        <form id="userAccountSetupForm" name="userAccountSetupForm" enctype="multipart/form-data" ref="form">
          <!-- Step 1 Content -->
          <section id="step-1" class="form-step">
            <h2 class="font-normal text-center">Choose an area</h2>
            <!-- Step 1 input fields -->
            <div id="mapContainer" class="mt-5">
              <AreaMap ref="area" />

            </div>
            <div class="form-floating mt-3">
              <select v-model="form.selectedArea" class="form-control" id="areaInput">
                <option v-for="area in areas" :value="area" :key="area">
                  {{ area.areaName }} - {{ area.address }}
                </option>
              </select>
              <!-- CARL SKAL BESLUTTE SIG -->
              <!-- <div v-for="area in areas" :value="area" :key="area">
                <input type="radio" v-model="form.selectedArea" name="areaInput" />
                {{ area.areaName }} {{ area.address }}
              </div> -->

              <label for="areaInput">Area</label>
            </div>
            <div class="mt-3 d-flex justify-content-end">
              <button class="button btn btn-navigate-form-step" type="button" step_number="2"
                :disabled="Object.keys(form.selectedArea) <= 0" @click="navigateToFormStep">
                Next
              </button>
            </div>
          </section>

          <!-- Step 2 Content, default hidden on page load. -->
          <section id="step-2" class="form-step d-none">
            <h2 class="font-normal">Choose car</h2>
            <!-- Step 2 input fields -->
            <div class="form-floating mt-3 gap-2" id="carRow">
              <select v-model="form.selectedCar" class="form-control" id="carInput">
                <option v-for="car in registeredCars" :value="car" :key="car">
                  {{ car.brand }} {{ car.model }} - {{ car.licenseplate }}
                </option>
              </select>
              <label for="carInput">Choose a car...</label>
              <button id="carPlusBtn" class="btn btn-primary btn-dark" @click="$router.push('/register-car')"
                data-toggle="tooltip" data-placement="top" title="Add a new car">
                <font-awesome-icon icon="fa-solid fa-car" />
                <font-awesome-icon id="carPlus" icon="fa-solid fa-plus" />
              </button>
            </div>
            <div class="mt-3 d-flex justify-content-between">
              <button class="button btn btn-navigate-form-step" type="button" step_number="1"
                @click="navigateToFormStep">
                Prev
              </button>
              <button class="button btn btn-navigate-form-step" type="button" step_number="3"
                :disabled="Object.keys(form.selectedCar) <= 0" @click="navigateToFormStep">
                Next
              </button>
            </div>
          </section>

          <!-- Step 3 Content, default hidden on page load. -->
          <section id="step-3" class="form-step d-none">
            <h2 class="font-normal">Set time</h2>
            <!-- Step 3 input fields -->
            <!-- <TimeDial :area="form.selectedArea" :car="form.selectedCar" ref="timeDial" /> -->
            <div class="row mt-3">
              <div class="col-lg-6 dial-col mb-3 lg-mb-0">
                <vue3-slider width="auto" height="6" v-model="form.time" orientation="circular" :max=24 trackColor="#d8956a" color="#000000" :step=0.05 /> <!-- :repeat=true -->
                <input type="number" class="form-control dial-input" v-model="form.time" min="0" step="0.05" />
              </div>
              <div class="col-lg-6">
                <h6>Your parking untill:</h6>
                <p>{{ form.parkingUntil }}</p>
                <hr>
                <h6>Price:</h6>
                <p>{{ form.price }} DKK</p>
                <hr>
                <h6>Car:</h6>
                <p>{{ form.selectedCar.licenseplate }} - {{ form.selectedCar.brand }} {{ form.selectedCar.model }}</p>
                <hr>
                <h6>Area:</h6>
                <p>{{ form.selectedArea.address }}</p>
              </div>
            </div>

            <div class="form-floating mt-3">
            </div>
            <div class="mt-3 d-flex justify-content-between">
              <button class="button btn btn-navigate-form-step" type="button" step_number="2"
                @click="navigateToFormStep">
                Prev
              </button>
              <button class="button btn submit-btn" @click="submit"
                :disabled="form.time == 0">Save</button>
            </div>
          </section>
        </form>

        <!-- Form Steps / Progress Bar -->
        <ul class="form-stepper form-stepper-horizontal text-center mx-auto pl-0">
          <!-- Step 1 -->
          <li class="form-stepper-active text-center form-stepper-list" step="1">
            <btn class="mx-2" step_number="1" id="formStep1Btn">
              <span class="form-stepper-circle" step_number="1">
                <span>1</span>
              </span>
              <div class="label">Choose an area</div>
            </btn>
          </li>
          <!-- Step 2 -->
          <li class="form-stepper-unfinished text-center form-stepper-list" step="2">
            <btn class="mx-2" id="formStep2Btn">
              <span class="form-stepper-circle text-muted" step_number="2">
                <span>2</span>
              </span>
              <div class="label text-muted">Choose a car</div>
            </btn>
          </li>
          <!-- Step 3 -->
          <li class="form-stepper-unfinished text-center form-stepper-list" step="3">
            <btn class="mx-2" id="formStep3Btn">
              <span class="form-stepper-circle text-muted" step_number="3">
                <span>3</span>
              </span>
              <div class="label text-muted">Set time</div>
            </btn>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
// import TimeDial from "@/components/TimeDial.vue";
import slider from "vue3-slider"
import AreaMap from "@/components/AreaMap.vue";
import axios from "axios";
import moment from "moment";
// import { TypedChainedSet } from "webpack-chain";

export default {
  components: {
    "vue3-slider": slider,
    AreaMap
  },
  data() {
    return {
      form: {
        time: 0,
        price: 0,
        parkingUntil: "No Time Selected",
        selectedCar: {},
        selectedArea: {},
      },
      registeredCars: [],
      areas: [],
      myNumber: "1",
    };
  },
  watch: {
    'form.selectedArea': function (value) {
      // Set marker on map
      let coords = {
        "coordinates": [value.longitude, value.latitude],
      }
      let areaMap = this.$refs.area;
      areaMap.plotResult(coords);
    },
    'form.time': function (value) {
      console.log(value);
        let minutes = Math.floor((value * 60))
        this.form.price = Math.floor((minutes * 0.15) * 100) / 100
        this.form.parkingUntil = moment().add(minutes, 'minutes').format('DD/MM/YYYY, h:mm');
        this.form.time = Math.floor((minutes / 60) * 100 ) / 100
    }
  
  },
  methods: {
    setArea() {
      console.log(this.form.selectedArea);
    },
    getNumberPlate(plateNumber) {
      // Python image recognition call
      console.log(plateNumber);
    },
    navigateToFormStep(stepNumber) {
      console.log('stepNumber: ' + stepNumber);
      if (stepNumber.target) // If event is triggered by button click
        stepNumber = stepNumber.target.attributes.step_number.value; // Get target step value

      document.querySelectorAll(".form-step").forEach((formStepElement) => {
        formStepElement.classList.add("d-none");
      });

      // Make all steps unfinished
      document.querySelectorAll(".form-stepper-list").forEach((formStepHeader) => {
        formStepHeader.classList.add("form-stepper-unfinished");
        formStepHeader.classList.remove("form-stepper-active", "form-stepper-completed");
      });

      document.querySelector("#step-" + stepNumber).classList.remove("d-none");
      const formStepCircle = document.querySelector('li[step="' + stepNumber + '"]');
      // Make current form step active
      formStepCircle.classList.remove(
        "form-stepper-unfinished",
        "form-stepper-completed"
      );
      formStepCircle.classList.add("form-stepper-active");
      // Loop through form step circles up to the current step
      for (let index = 0; index < stepNumber; index++) {
        const formStepCircle = document.querySelector('li[step="' + index + '"]');
        if (formStepCircle) {
          // Mark old step as completed
          formStepCircle.classList.remove(
            "form-stepper-unfinished",
            "form-stepper-active"
          );
          formStepCircle.classList.add("form-stepper-completed");
        }
      }
    },
    submit() {
      // console.log('SUBMITTING');
      // console.log(this.$refs.form);

      console.log("FORM", this.form.selectedArea)

      // POST parking to API
      this.$store.dispatch("callAPI", {
        method: "POST",
        endpoint: "parkings",
        body: {
          licenseplate: this.form.selectedCar.licenseplate,
          userId: this.$store.getters.getUserInfo.userId,
          token: this.$store.getters.getUserInfo.token,
          areaId: this.form.selectedArea.areaId,
          state: "active",
          // NEW TIME DIAL:
          minutes: this.form.time * 60,
          price: this.form.price,
          timestamp: this.form.parkingUntil
          // OLD TIME DIAL:
          // minutes: this.$store.getters.getParkingTimeMinutes,
          // price: this.$refs.timeDial.price,
          // timestamp: this.$refs.timeDial.parkingUntil, 
        },
      }).then((response) => {
        console.log(response);
        this.$router.push({ name: "Home" });
      }).catch((error) => {
        console.warn("parkings", error);
      }
      );



    }
  },
  mounted() {
    // Get registered cars

    axios.get(this.$store.state.api + "/userLicenseplates/", { params: { userId: this.$store.getters.getUserInfo.userId, token: this.$store.getters.getUserInfo.token } }).then((response) => {
      this.registeredCars = response.data;
      console.log("registeredCars:", this.registeredCars)
    }).catch((error) => {
      console.warn("userLicenseplates", error);
    });

    // Get areas
    axios.get(this.$store.state.api + "/areas/", { params: { token: this.$store.getters.getUserInfo.token } }).then((response) => {
      this.areas = response.data;
      console.log(this.areas);
    }).catch((error) => {
      console.warn("areas", error);
    });

    document
      .querySelectorAll(".form-stepper-list a .form-stepper-circle")
      .forEach((circle) => {
        circle.addEventListener("click", () => {
          console.log(circle);
          let classList = circle.parentElement.parentElement.classList;
          console.log(classList);

          if (
            classList.contains("form-stepper-active") !== true &&
            classList.contains("form-stepper-unfinished") !== true
          ) {
            const circleNumber = circle.getAttribute("step_number");
            console.log("CHANGING TO: " + circleNumber);
            this.navigateToFormStep(circleNumber);
          }
        });
      });


  },
};
</script>

<style scoped>
/* Hide arrows from parking dial input */
/* Chrome, Safari, Edge, Opera */
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

/* Firefox */
input[type=number] {
  -moz-appearance: textfield;
}
.dial-input {
  position: absolute;
  max-width: 70%;
  text-align: center;
}

.dial-col {
  display: flex;
  justify-content: center;
  align-items: center;
}

.action-prompt {
  height: auto
}

#carRow {
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
}

#carPlusBtn {
  display: flex;
  align-items: center;
  width: 56px;
  height: 56px;
  border-radius: 50%;
}

#carPlus {
  bottom: 8px;
}

#container {
  position: absolute;
  top: 50px;
  left: 50px;
  width: 400px;
  height: 400px;
  background: #ddd;
  border: 1px solid #999;
  border-radius: 1000px;
}

#slider {
  position: relative;
  height: 40px;
  width: 40px;
  left: 180px;
  top: -20px;
  background: red no-repeat center 20px;
  border-radius: 20px;
}

#userAccountSetupForm {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

h1 {
  text-align: center;
}

h2 {
  margin: 0;
}
</style>
