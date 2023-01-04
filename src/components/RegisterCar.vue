<template>
  <div class="container">
    <div class="mx-auto circle1">
      <button id="parkingBtn" class="btn btn-transparent"><b>REGISTER PARKING</b></button>
      <div class="circle2">
        <button id="carBtn" class="btn btn-transparent"><b>REGISTER CAR</b></button>
      </div>
    </div>

    <div class="row">
      <div class="col-lg-6 intro-text">
        <h2>Intro text here</h2>
      </div>
      <div class="col-lg-6 action-prompt">
        <button class="btn btn-primary">REGISTER PARKING</button>
        <button class="btn btn-primary">REGISTER CAR</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RegisterCar',
}
</script>

<style scoped>
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
.action-prompt {
  border: 1px solid white;
  border-radius: 12px;
  height: 80vh;
  background: rgba(0, 0, 0, 0.4);
}
</style>
