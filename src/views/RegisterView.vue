<template>
  <div class="container mt-5">
    <div class="action-prompt m-auto">
      <h3 class="text-center">REGISTER</h3>
      <hr />
      <form>
        <!-- Firstname -->
        <div class="form-floating mb-3">
          <input
            v-model="form.firstname"
            type="text"
            class="form-control"
            id="floatingFirstname"
            placeholder="Your First name"
          />
          <label for="floatingName">First name</label>
        </div>
        <!-- Lastname -->
        <div class="form-floating mb-3">
          <input
            v-model="form.lastname"
            type="text"
            class="form-control"
            id="floatingLastname"
            placeholder="Your Last name"
          />
          <label for="floatingName">Last name</label>
        </div>
        <!-- Email -->
        <div class="form-floating mb-3">
          <input
            v-model="form.email"
            type="email"
            class="form-control"
            id="floatingEmail"
            placeholder="name@gmail.com"
          />
          <label for="floatingEmail">Email address</label>
        </div>
        <div class="row">
          <!-- CC_Code -->
          <div class="col-lg-3">
            <div class="form-floating mb-3">
              <select
                v-model="form.ccCode"
                class="form-control"
                id="floatingCC-code"
              >
                <option v-for="code in cc_codes" :value="code" :key="code">
                  {{ code.dial_code }}, {{ code.code }}
                </option>
              </select>
              <label for="floatingCC-Code">CC Code</label>
            </div>
          </div>
          <!-- Telephone number -->
          <div class="col-lg-9">
            <div class="form-floating mb-3">
              <input
                v-model="form.phone"
                type="tel"
                class="form-control"
                id="floatingTelephone"
                placeholder="Telephone Number"
              />
              <label for="floatingTelephone">Telephone Number</label>
            </div>
          </div>
        </div>
        <!-- Password -->
        <div class="form-floating mb-3">
          <input
            v-model="form.password"
            type="password"
            class="form-control"
            id="floatingPassword"
            placeholder="Password"
          />
          <label for="floatingPassword">Password</label>
        </div>
        <!-- Repeat Password -->
        <div class="form-floating mb-3">
          <input
            v-model="form.repeatPassword"
            type="password"
            class="form-control"
            id="floatingRepeatPassword"
            placeholder="Repeat Password"
          />
          <label for="floatingRepeatPassword">Repeat Password</label>
        </div>
        <h5 class="text-danger" v-if="form.password != form.repeatPassword">
          Passwords doesn't match!
        </h5>
        <button
          v-on:click="registerUser()"
          class="btn-transparent btn btn-dark"
        >
          Register
        </button>
      </form>
      <router-link class="text-center nav-link text-white" to="/login"
        ><span>Already have an account?</span></router-link
      >
    </div>
  </div>
</template>

<style scoped>
.action-prompt {
  height: 50%;
  width: 50%;
}

span {
  color: black;
}

.form-floating > label {
  color: black !important;
}
</style>

<script>
import json from "@/assets/CountryCodes.json";
import axios from "axios";

export default {
  data() {
    return {
      form: {
        firstname: "",
        lastname: "",
        email: "",
        password: "",
        phone: "",
        ccCode: "",
        repeatPassword: "",
      },
      cc_codes: json.sort(this.compareDialCode),
    };
  },
  watch: {},
  methods: {
    compareDialCode: function (a, b) {
      return a.dial_code - b.dial_code;
    },
    registerUser: function () {
      axios
        .post("/register", this.form)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.warn("register", error);
        });
    },
  },
};
</script>