<template>
  <div class="container">


    <div class="row mt-5">
      <div class="col-lg-7 pt-5">
        <h1 class="display-1 fw-bold">Better solution <br>for parking.</h1>
        <h2 class="fw-light mt-4">Parking doesn't need to be <span class="text-decoration-line-through">hard</span>,
          <br>our focus is making parking <span class="text-decoration-underline">easier</span>.
        </h2>
        <router-link class="btn mt-4 btn-light" to="/about"><span>Get to know us</span></router-link>
      </div>
      <div class="col-lg-5 mt-5 mt-lg-0 action-prompt">
        <div class="mx-auto row h-100">
          <div class="row d-flex justify-content-center text-center">
            <h3 v-if="!$store.state.user.userId">Welcome!</h3>
            <h3 v-if="$store.state.user.userId">Welcome {{ $store.state.user.firstname }}!</h3>
            <p>
              EasierPark makes it <b>easy</b> to park. Just register a car, and get
              started with your first parking 👋
            </p>
            <div>
              <img class="img-container" src="../assets/parking.webp" alt="carParking" />
            </div>

            <!-- <p>[PARKING INFO?]</p> -->
          </div>


            <div v-if="$store.state.user.userId" class="col-xl-12 d-flex justify-content-around front-actions mt-auto">
              <button id="parkingBtn" class="btn btn-primary btn-dark" @click="$router.push('/new-parking')"
                data-toggle="tooltip" data-placement="top" title="Register a new parking">
                NEW PARKING
              </button>
              <button id="carPlusBtn" class="btn btn-primary btn-dark" @click="$router.push('/register-car')"
                data-toggle="tooltip" data-placement="top" title="Add a new car">
                <font-awesome-icon icon="fa-solid fa-car" />
                <font-awesome-icon id="carPlus" icon="fa-solid fa-plus" />
              </button>
            </div>

            <div v-if="!$store.state.user.userId" class="col-xl-12 d-flex flex-wrap justify-content-around front-actions mt-auto">
              <h4 class="col-xl-12 text-center" v-if="!$store.state.user.userId">Log in or register to get started!</h4>
              <br />
              <button class="col-xl-5 btn btn-primary" @click="$router.push('/login')">
                LOGIN
              </button>
              <button class="col-xl-5 btn btn-primary" @click="$router.push('/register')">
                REGISTER
              </button>
            </div>

        </div>



      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FrontPage",
};
</script>

<style scoped>
#parkingBtn {
  width: 80%;
  border-radius: 12px;
}

#carPlusBtn {
  width: 56px;
  height: 56px;
  border-radius: 50%;
}

#carPlus {
  bottom: 8px;
}

.front-actions {
  max-height: 80px;
  margin-bottom: 35px;
}

.front-actions button {
  border-radius: 12px;
  height: 60px;
}

.img-container {
  max-width: 60%;
  border: 0x solid black;
  border-radius: 10px;
}

</style>