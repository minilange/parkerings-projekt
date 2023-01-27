<template>
  <div class="container mt-5">
    <div class="action-prompt m-auto">
      <h3 class="text-center">LOGIN</h3>
      <hr />
      <form>
        <div class="form-floating mb-3">
          <input v-model="form.email" type="email" class="form-control" id="floatingEmail"
            placeholder="name@gmail.com" />
          <label for="floatingEmail">Email address</label>
        </div>
        <div class="form-floating mb-3">
          <input v-model="form.password" type="password" class="form-control" id="floatingPassword"
            placeholder="Password" />
          <label for="floatingPassword">Password</label>
        </div>
      </form>
      <button v-on:click="loginUser()" class="btn-transparent btn btn-dark" :disabled="$store.state.searching == true">Login</button>
      <div v-if="$store.state.searching == true" id="searchStatus" class="mt-4 d-flex">
        <span>Searching...</span>
        <div class="loader"></div>

      </div>

      <router-link class="text-center nav-link text-white" to="/register"><span>Need an account?</span></router-link>
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
  .action-prompt {
    width: 80%;
  }
}
</style>

<script>
import { SHA256 } from "crypto-js";

export default {
  data() {
    return {
      form: {
        email: "",
        password: "",
      },
    };
  },
  mounted() {
    // Check if user is already logged in local storage
    if (localStorage.getItem("user")) {
      this.$store.commit("setUser", JSON.parse(localStorage.getItem("user")));
      alert("You are already logged in!")
      this.$router.push("/");
    }
  },
  methods: {
    loginUser: function () {
      console.log('loginUser')
      this.$store.dispatch("loginUser", {
        params: {
          email: this.form.email,
          password: SHA256(this.form.password, this.$store.state.secret).toString(),
          userId: this.$store.state.user.userId,
          token: this.$store.state.user.token,
        },
      })
    },
  },
};
</script>
