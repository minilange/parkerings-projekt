<template>
  <div class="container mt-5">
    <div class="action-prompt m-auto">
      <h3 class="text-center">LOGIN</h3>
      <hr />
      <form>
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
      </form>
      <button v-on:click="loginUser()" class="btn-transparent btn btn-dark">Login</button>
      <router-link class="text-center nav-link text-white" to="/register"
        ><span>Need an account?</span></router-link
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

@media (max-width: 991px) {
  .action-prompt{
    width: 80%;
  }
}

</style>

<script>
import axios from "axios";
import SHA256 from "crypto-js/sha256";

export default {
  data() {
    return {
      form: {
        email: "",
        password: "",
      },
    };
  },
  methods: {
    loginUser: function () {
      axios
        .get(this.$store.state.api + "/login/", {
          params: {
            email: this.form.email,
            password: SHA256(this.form.password, this.$store.state.secret).toString(),
          },
        })
        .then((response) => {
          this.$store.commit("SET_USER_INFO", response.data);
          this.$router.push('/')
        })
        .catch((error) => {
          console.warn("login", error);
        });
    },
  },
};
</script>
