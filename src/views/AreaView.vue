<template>
  <div class="container mt-5">
    <div class="action-prompt">
      <div class="row h-100 overflow-hidden">
        <div class="col-lg-6">
          <h3>AREAS MAP:</h3>

        </div>
        <div class="col-lg-6">
          <h3>AREAS LIST:</h3>
          <div class="area-list">
            <select class="form-control" id="area">
              <option selected disabled>Select an area</option>
              <option>2398 W. Maple St.</option>
              <option>1750 N. Main Ave.</option>
              <option>1475 S. Third St.</option>
              <option>3298 E. Oak St.</option>
              <option>754 N. Fifth Ave.</option>
              <option>4567 W. Pine St.</option>
              <option>6109 E. Maple Ave.</option>
              <option>836 S. Fourth St.</option>
              <option>952 N. Main St.</option>
              <option>2731 E. Pine Ave.</option>
              <option>1039 S. Fifth Ave.</option>
              <option>2745 E. Oak St.</option>
              <option>3579 N. Main Ave.</option>
              <option>4296 W. Maple St.</option>
              <option>5608 N. Third St.</option>
              <option>6708 E. Pine Ave.</option>
              <option>7254 S. Fourth St.</option>
              <option>8091 W. Oak St.</option>
              <option>9170 N. Fifth Ave.</option>
              <option>1025 E. Maple Ave.</option>
              <option>1134 S. Main St.</option>
              <option>1247 W. Pine St.</option>
              <option>1356 N. Third St.</option>
              <option>1467 E. Oak Ave.</option>
            </select>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.action-prompt {
  border: 1px solid white;
  border-radius: 12px;
  padding: 15px;
  height: 70vh;
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
</style>

<script>

export default {
  components: {
  },
  data() {
    return {

    };
  },
};
</script>