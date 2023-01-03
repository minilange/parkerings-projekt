<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark ">
    <div class="container-fluid">
        <a href="" class="navbar-brand fw-bold">EASIER<span class="text-secondary fw-bold">PARK</span></a>
        <button type="button" class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse navbar-right" id="navbarCollapse">
            <div class="navbar-nav ms-auto gap-lg-5 fw-bold">
                <a href="#" class="nav-item nav-link text-white">PARK</a>
                <a href="#" class="nav-item nav-link text-white">AREAS</a>
                <a href="#" class="nav-item nav-link text-white">ABOUT US</a>
            </div>
        </div>
    </div>
  </nav>
</template>

<style scoped>
@media (max-width: 991px) {
  .navbar-collapse {
  position: fixed;
  height: 100vh;
  width: 100%;
  top: 55px;
  right: 0;
  padding-left: 15px;
  padding-right: 15px;
  padding-bottom: 15px;
  background-color: #212529;
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