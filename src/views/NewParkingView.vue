<template>
  <!-- <TimeDial /> -->
  <div class="container mt-5 mx-auto row">
    <div class="col-lg-7 action-prompt m-auto">
      <h3 class="text-center">NEW PARKING</h3>
      <hr />

      <div id="multi-step-form-container">
        <!-- Step Wise Form Content -->
        <form id="userAccountSetupForm" name="userAccountSetupForm" enctype="multipart/form-data" method="POST">
          <!-- Step 1 Content -->
          <section id="step-1" class="form-step">
            <h2 class="font-normal">Choose an area</h2>
            <!-- Step 1 input fields -->
            <p>[SHOW MAP HERE]</p>
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
            <TimeDial :area="form.selectedArea" :car="form.selectedCar" />

            <div class="form-floating mt-3">
            </div>
            <div class="mt-3 d-flex justify-content-between">
              <button class="button btn btn-navigate-form-step" type="button" step_number="2"
                @click="navigateToFormStep">
                Prev
              </button>
              <button class="button btn submit-btn" type="submit"
                :disabled="$store.state.time.hours == 0 && $store.state.time.minutes == 0">Save</button>
            </div>
          </section>
        </form>

        <!-- Form Steps / Progress Bar -->
        <ul class="form-stepper form-stepper-horizontal text-center mx-auto pl-0">
          <!-- Step 1 -->
          <li class="form-stepper-active text-center form-stepper-list" step="1">
            <a class="mx-2" step_number="1">
              <span class="form-stepper-circle" step_number="1">
                <span>1</span>
              </span>
              <div class="label">Choose an area</div>
            </a>
          </li>
          <!-- Step 2 -->
          <li class="form-stepper-unfinished text-center form-stepper-list" step="2">
            <a class="mx-2">
              <span class="form-stepper-circle text-muted" step_number="2">
                <span>2</span>
              </span>
              <div class="label text-muted">Choose a car</div>
            </a>
          </li>
          <!-- Step 3 -->
          <li class="form-stepper-unfinished text-center form-stepper-list" step="3">
            <a class="mx-2">
              <span class="form-stepper-circle text-muted" step_number="3">
                <span>3</span>
              </span>
              <div class="label text-muted">Set time</div>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import TimeDial from "@/components/TimeDial.vue";

export default {
  components: {
    TimeDial
  },
  data() {
    return {
      form: {
        selectedCar: {},
        selectedArea: {},
      },
      registeredCars: [],
      areas: [],
      myNumber: "1",
    };
  },
  methods: {
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
  },
  mounted() {
    axios
      .get(this.$store.state.api + "/userLicenseplates/", {
        params: {
          userId: 1,
        },
      })
      .then((response) => {
        this.registeredCars = response.data;
        console.log("registeredCars:", this.registeredCars)
      })
      .catch((error) => {
        console.warn("userLicenseplates", error);
      });

    axios
      .get(this.$store.state.api + "/areas/")
      .then((response) => {
        this.areas = response.data;
        console.log(this.areas);
      })
      .catch((error) => {
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


.action-prompt {
  height: 80vh;
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

#multi-step-form-container {
  height: 75%;
  border: 0;
  margin-top: 0;
}

.text-center {
  text-align: center;
}

.mx-auto {
  margin-left: auto;
  margin-right: auto;
}

.pl-0 {
  padding-left: 0;
}

.button {
  padding: 0.7rem 1.5rem;
  border: 1px solid #5e5e5e;
  background-color: #4361ee;
  color: #fff;
  border-radius: 5px;
  cursor: pointer;
}

.submit-btn {
  border: 1px solid #0e9594;
  background-color: #0e9594;
}

.mt-3 {
  margin-top: 2rem;
}

.d-none {
  display: none;
}

.form-step {
  /* border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 20px; */
  border: 0;
  padding: 3rem;
}

.font-normal {
  font-weight: normal;
}

ul.form-stepper {
  counter-reset: section;
  margin-bottom: 3rem;

}

ul.form-stepper .form-stepper-circle {
  position: relative;
}

ul.form-stepper .form-stepper-circle span {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translateY(-50%) translateX(-50%);
}

.form-stepper-horizontal {
  position: relative;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
}

ul.form-stepper>li:not(:last-of-type) {
  margin-bottom: 0.625rem;
  -webkit-transition: margin-bottom 0.4s;
  -o-transition: margin-bottom 0.4s;
  transition: margin-bottom 0.4s;
}

.form-stepper-horizontal>li:not(:last-of-type) {
  margin-bottom: 0 !important;
}

.form-stepper-horizontal li {
  position: relative;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-flex: 1;
  -ms-flex: 1;
  flex: 1;
  -webkit-box-align: start;
  -ms-flex-align: start;
  align-items: start;
  -webkit-transition: 0.5s;
  transition: 0.5s;
}

.form-stepper-horizontal li:not(:last-child):after {
  position: relative;
  -webkit-box-flex: 1;
  -ms-flex: 1;
  flex: 1;
  height: 1px;
  content: "";
  top: 32%;
}

.form-stepper-horizontal li:after {
  background-color: #dee2e6;
}

.form-stepper-horizontal li.form-stepper-completed:after {
  background-color: #5e5e5e;
}

.form-stepper-horizontal li:last-child {
  flex: unset;
}

ul.form-stepper li a .form-stepper-circle {
  display: inline-block;
  width: 40px;
  height: 40px;
  margin-right: 0;
  line-height: 1.7rem;
  text-align: center;
  background: rgba(0, 0, 0, 0.38);
  border-radius: 50%;
}

.form-stepper .form-stepper-active .form-stepper-circle {
  background-color: #d8956a !important;
  color: #fff;
  transition: 0.5s;
}

.form-stepper .form-stepper-active .label {
  color: black !important;
}

.form-stepper .form-stepper-active .form-stepper-circle:hover {
  background-color: black !important;
  color: #fff !important;
}

.form-stepper .form-stepper-unfinished .form-stepper-circle {
  background-color: #f8f7ff;
}

.form-stepper .form-stepper-completed .form-stepper-circle {
  background-color: #5e5e5e !important;
  color: #fff;
  transition: 0.5s;
}

.form-stepper .form-stepper-completed .label {
  color: #5e5e5e !important;
}

.form-stepper .form-stepper-completed .form-stepper-circle:hover {
  background-color: black !important;
  color: #fff !important;
}

.form-stepper .form-stepper-active span.text-muted {
  color: #fff !important;
}

.form-stepper .form-stepper-completed span.text-muted {
  color: #fff !important;
}

.form-stepper .label {
  font-size: 1rem;
  margin-top: 0.5rem;
}

.form-stepper a {
  text-decoration: none;
  cursor: default;
}
</style>
