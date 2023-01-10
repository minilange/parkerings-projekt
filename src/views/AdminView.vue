<template>
  <div class="container p-5">
    <div class="row action-prompt">
      <div class="col-lg-12">
        <div class="card mb-4 profile">
          <div class="card-body text-center">
            <h5 class="mb-0">Parkings</h5>
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">Parking ID</th>
                  <th scope="col">User</th>
                  <th scope="col">Car</th>
                  <th scope="col">Start</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">1</th>
                  <td>Test user</td>
                  <td>Test car</td>
                  <td>12-05-2022</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <div class="col-lg-12">
        <div class="col-md-12">
          <div class="card">
            <div class="card-body">
              <h5 class="mb-0">Registered cars</h5>

              <table class="table">
                <thead>
                  <tr>
                    <th scope="col">Brand</th>
                    <th scope="col">Model</th>
                    <th scope="col">Year</th>
                    <th scope="col">Type</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <th scope="row">Hyundai</th>
                    <td>I 30</td>
                    <td>2008</td>
                    <td>Hatchback</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

      <div class="col-lg-12">
        <div class="col-md-12">
          <div class="card">
            <div class="card-body">
              <h5 class="mb-0">Users</h5>

              <table class="table">
                <thead>
                  <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Email</th>
                    <th scope="col">Phone</th>
                    <th scope="col"></th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <th scope="row">Test user</th>
                    <td>test@test.com</td>
                    <td>+45 11223344</td>
                    <td></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  watch: {},
};
</script>
