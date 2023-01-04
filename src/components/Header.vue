<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
      <a href="" class="d-lg-none navbar-brand">Login</a>
          <router-link class="navbar-brand fw-bold text-white" to="/">EASIER<span class="text-secondary fw-bold">PARK</span></router-link>
          <button type="button" class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
              <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse navbar-right" id="navbarCollapse">
              <div class="navbar-nav ms-auto gap-lg-5 fw-bold">
                <router-link class="nav-item nav-link text-white d-none d-lg-block" to="/login">LOGIN</router-link>
                <router-link class="nav-item nav-link text-white" to="/park">PARK</router-link>
                <router-link class="nav-item nav-link text-white" to="/areas">AREAS</router-link>
                <router-link class="nav-item nav-link text-white" to="/about">ABOUT US</router-link>
              </div>
          </div>
      </div>
    </nav>
</template>

<script>
export default {
  name: 'HeaderFront',
}
</script>

<style scoped>
@media (max-width: 991px) {
  .navbar-collapse {
    position: fixed;
    height: 100vh;
    width: 240px;
    top: 55px;
    right: 0;
    padding-left: 15px;
    padding-right: 15px;
    padding-bottom: 15px;
    background-color: #212529;
    z-index: 9999;
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