<template>
  <div class="container">
    <div class="mt-5 action-prompt">
      <table v-if="registeredParkings.length > -1" class="table table-striped">
        <thead>
          <tr>
            <th scope="col">Licenseplate:</th>
            <th scope="col">Minutes:</th>
            <th scope="col">Cost:</th>
            <th scope="col">State:</th>
            <th scope="col">Timestamp:</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="parking in registeredParkings" :key="parking">
            <td>{{ parking.licenseplate }}</td>
            <td>{{ parking.minutes }}</td>
            <td>{{ parking.price }}</td>
            <td>{{ parking.state }}</td>
            <td>{{ parking.timestamp }}</td>
          </tr>
        </tbody>
      </table>
      <div v-else class="mt-5 action-prompt">
        <h1>You don't have any registered parkings yet...</h1>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      registeredParkings: [{licenseplate: "HG29559", minutes: "10", price: "20", state:"DK", timestamp:"2023/17/01"},{licenseplate: "HG29559", minutes: "10", price: "20", state:"DK", timestamp:"2023/17/01"}]
    };
  },
  mounted() {
    // Parkings
    axios
      .get(this.$store.state.api + "/parkings/", {
        params: {
          userId: this.$store.state.user.userId,
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
