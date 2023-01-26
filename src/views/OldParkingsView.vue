<template>
  <div class="container">
    <div class="mt-5 action-prompt h-auto">
      <p class="display-6">My parkings</p>
      <hr>
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">Licenseplate</th>
            <th scope="col">Minutes</th>
            <th scope="col">Cost</th>
            <th scope="col">State</th>
            <th scope="col">Timestamp</th>
          </tr>
        </thead>
        <tbody v-if="registeredParkings.length > 0">
          <tr v-for="parking in registeredParkings" :key="parking">
            <td>{{ parking.licenseplate }}</td>
            <td>{{ parking.minutes }}</td>
            <td>{{ parking.price }}</td>
            <td>{{ parking.state }}</td>
            <td>{{ parking.timestamp }}</td>
          </tr>
        </tbody>
        <tbody v-else>
          <tr>
            <td colspan="5">You don't have any parkings yet..</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      registeredParkings: [],
    };
  },
  mounted() {
    // Parkings
    axios
      .get(this.$store.state.api + "/parkings/", {
        params: {
          userId: this.$store.state.user.userId,
          token: this.$store.state.user.token,
        },
      })
      .then((response) => {
        this.registeredParkings = response.data
        console.log("TEST", response.data)
      })
      .catch((error) => {
        console.warn("parkings", error);
      });
  }
}
</script>

<style>
tr th {
  font-weight: 700;
}
</style>
