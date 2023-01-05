<template>
  <div class="container mt-5">
    <div class="action-prompt m-auto">
      <h3 class="text-center">LOGIN</h3>
      <hr>
      <form>
        <div class="form-floating mb-3">
          <input type="email" class="form-control" id="floatingEmail" placeholder="name@gmail.com">
          <label for="floatingEmail">Email address</label>
        </div>
        <div class="form-floating mb-3">
          <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
          <label for="floatingPassword">Password</label>
        </div>
        <button type="submit" class=" btn-transparent btn btn-primary">Login</button>
      </form>
      <router-link class="text-center nav-link text-white" to="/register"><span>Need an account?</span></router-link>
    </div>
  </div>
</template>

<style scoped>
  .action-prompt {
    border: 1px solid white;
    border-radius: 12px;
    padding: 15px;
    height: 50%;
    width: 50%;
    position: relative;
    background: rgba(0, 0, 0, 0.4);
  }

  .btn-transparent {
    background: transparent;
    color: white;
    border-color: white;
  }

  .btn-transparent:hover {
    background: white;
    color: black;
  }

  .form-floating > label{
    color:black !important;
  }
</style>