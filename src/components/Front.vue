<template>
  <div class="container">
    <div class="mx-auto circle1">
      <button id="parkingBtn" class="btn btn-transparent"><b>REGISTER PARKING</b></button>
      <div class="circle2">
        <button id="carBtn" class="btn btn-transparent"><b>REGISTER CAR</b></button>
      </div>
    </div>

    <div class="row mt-5">
      <div class="col-lg-7 pt-5">
        <h1 class="display-1 fw-bold">Better solution <br>for parking.</h1>
        <h2 class="fw-light mt-4">Parking doesn't need to be <span class="text-decoration-line-through">hard</span>, <br>our focus is making parking <span class="text-decoration-underline">easier</span>.</h2>
        <router-link class="btn mt-4 btn-light" to="/about"><span >Get to know us</span></router-link>
      </div>
      <div class="col-lg-5 mt-5 mt-lg-0 action-prompt">
        <div class="mx-auto row h-100">
          <div class="row d-flex justify-content-center text-center">
            <h3>Welcome!</h3>
            <p>
              EasierPark makes it <b>easy</b> to park. Just register a car, and get
              started with your first parking 👋
            </p>
            <div>
              <img class="img-container" src="../assets/parking.png" />
            </div>

            <!-- <p>[PARKING INFO?]</p> -->
          </div>

          <div class="col-xl-12 d-flex justify-content-around front-actions mt-auto">
            <button
              id="parkingBtn"
              class="btn btn-primary btn-dark"
              @click="$router.push('/new-parking')"
              data-toggle="tooltip" data-placement="top" title="Register a new parking"
            >
              NEW PARKING
            </button>
            <button
              id="carPlusBtn"
              class="btn btn-primary btn-dark"
              @click="$router.push('/register-car')"
              data-toggle="tooltip" data-placement="top" title="Add a new car"
            >
              <font-awesome-icon icon="fa-solid fa-car" />
              <font-awesome-icon id="carPlus" icon="fa-solid fa-plus" />
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
  max-height: 60px;
  margin-bottom: 35px;
}

.img-container {
  max-width: 60%;
  border: 0x solid black;
  border-radius: 10px;
}

.action-prompt {
  /* border: 1px solid white; */
  border-radius: 12px;
  height: 80vh;
  padding: 20px;
  color: black;
  background-color: #f2f1ed;
  box-shadow: 0px 0px 50px 12px black;
}

.circle1 {
  display: none;
  background-color: black;
  border-radius: 50%;
  height: 200px;
  width: 200px;
  position: relative;
  border: 5px solid white;
  line-height: 175px;
  text-align: center;
  color: white;
  transition: 0.4s;
}
.circle2 {
  border: 5px solid white;
  background-color: black;
  border-radius: 50%;
  height: 125px;
  width: 125px;
  position: absolute;
  bottom: -30%;
  right: -10%;
  line-height: 115px;
  text-align: center;
  transition: 0.4s;
}
.btn-transparent {
  background: transparent;
  color: white;
  width: 100%;
  height: 100%;
  border-radius: 50%;
}
.circle1:hover {
  background-color: gray;
}
.circle2:hover {
  background-color: gray;
}
</style>