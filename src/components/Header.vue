<template>
  <!-- <div id="navbarShadow" class="navbar-gradient-shadow navbar-top"></div> -->
  <nav class="navbar navbar-expand-lg navbar-dark navbar-top">
    <div class="container-fluid container">
      <div v-if="!this.$store.state.user.hasOwnProperty('userId')">
        <router-link class="navbar-brand d-lg-none fw-bold text-white" to="/login">Login</router-link>
      </div>
      <router-link class="navbar-brand fw-bold text-white" to="/">
        <!-- EASIER<span class="text-secondary fw-bold">PARK</span> -->
        <img src="../assets/easierpark-logo.webp" height="25" width="186" alt="EASIERPARK LOGO" />
      </router-link>
      <button type="button" id="navbarBtn" aria-label="Navbar button" class="navbar-toggler on-top"
        data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse navbar-right navbar-side" id="navbarCollapse">
        <div class="navbar-nav ms-auto gap-lg-5 fw-bold">
          <router-link v-if="this.$store.state.user.hasOwnProperty('userId')"
            class="nav-item nav-link text-white d-none d-lg-block" to="/new-parking"><span>NEW
              PARKING</span></router-link>
          <router-link v-if="!this.$store.state.user.hasOwnProperty('userId')"
            class="nav-item nav-link text-white d-none d-lg-block" to="/login"><span>LOGIN</span></router-link>
          <!-- <router-link class="nav-item nav-link text-white" to="/areas"><span>AREAS</span></router-link> -->
          <router-link class="nav-item nav-link text-white" to="/about"><span>ABOUT US</span></router-link>
          <router-link v-if="this.$store.state.user.hasOwnProperty('userId')" class="nav-item nav-link text-white"
            to="/profile"><span>PROFILE</span></router-link>
          <router-link v-if="this.$store.state.user.hasOwnProperty('userId')" class="nav-item nav-link text-white"
            to="/old-parkings"><span>MY PARKINGS</span></router-link>
          <a v-if="this.$store.state.user.hasOwnProperty('userId')" @click="this.logOut"
            class="nav-item nav-link text-white"><span>LOG OUT</span></a>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'HeaderFront',
  methods: {
    logOut() {
      this.$store.dispatch("logOut");
      // Remove local storage
      localStorage.removeItem("userInfo");
      this.$router.push("/login");
    }
  },
  mounted() {

    // Get userInfo from localStorage, if it exists
    const userInfo = localStorage.getItem("userInfo")
      ? JSON.parse(localStorage.getItem("userInfo"))
      : null;

    // If userInfo exists, verify that token has not expired
    if (userInfo) {
      const tokenExpiration = userInfo.tokenExpiration;
      const now = new Date();
      if (now.getTime() > tokenExpiration) {
        localStorage.removeItem("userInfo");
        alert("Your session has expired. Please log in again.");
        window.location.href = "/login";
      } else {
        this.$store.dispatch("setUserInfoFromLocalStorage");
      }
    }
  }
}


</script>

<style scoped>
.on-top {
  z-index: 99999;
}

.navbar-brand>img {
  margin-left: 20px;
}

@media (max-width: 991px) {
  .navbar-collapse {
    position: fixed;
    height: 100vh;
    width: 240px;
    font-size: 24px;
    padding-top: 55px;
    top: 0;
    right: 0;
    padding-left: 15px;
    padding-right: 15px;
    padding-bottom: 15px;
    background-color: #212529;
    z-index: 9999;
  }

  .navbar-brand>img {
    margin-left: 0px;
  }

  .navbar-collapse.collapsing {
    right: -100%;
    transition: height 0s ease;
  }

  .navbar-collapse.show {
    right: 0;
    transition: right 300ms ease-in-out;
  }

  .navbar-toggler.collapsed~.navbar-collapse {
    transition: right 500ms ease-in-out;
  }
}
</style>