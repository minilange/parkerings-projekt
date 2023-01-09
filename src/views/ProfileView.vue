<template>
    <div class="container py-5">
        <div class="row">
            <div class="col-lg-4">
                <div class="card mb-4">
                    <div class="card-body text-center">
                        <img src="../assets/user-icon.png" alt="avatar" class="rounded-circle img-fluid"
                            style="width: 150px;">
                        <h5 class="my-3">[Name]</h5>
                    </div>
                </div>
                <div class="card mb-4 mb-lg-0">
                    <div class="card-body p-0">
                        <ul class="list-group list-group-flush rounded-3">
                            <li class="list-group-item text-center align-items-center p-3">
                                <i class="fas fa-globe fa-lg text-warning"></i>
                                <h5 class="mb-0">REGISTERED CARS:</h5>
                            </li>
                            <div v-if="registeredCars.length > 0">
                                <li class="list-group-item p-3" v-for="numberplate in registeredCars" :key="numberplate">
                                    <p class="mb-0">{{ numberplate }}</p>
                                </li>
                            </div>
                            <div v-else>
                                <li class="list-group-item p-3">
                                    <p class="mb-0">You don't have any registered cars yet...</p>
                                </li>
                            </div>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="col-lg-8">
                <div class="card mb-4">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-sm-3">
                                <p class="mb-0">First Name:</p>
                            </div>
                            <div class="col-sm-9">
                                <p class="mb-0">{{user.firstname}}</p>
                            </div>
                        </div>
                        <hr>
                        <div class="row">
                            <div class="col-sm-3">
                                <p class="mb-0">Last Name:</p>
                            </div>
                            <div class="col-sm-9">
                                <p class="mb-0">{{user.lastname}}</p>
                            </div>
                        </div>
                        <hr>
                        <div class="row">
                            <div class="col-sm-3">
                                <p class="mb-0">Email:</p>
                            </div>
                            <div class="col-sm-9">
                                <p class="mb-0">{{user.email}}</p>
                            </div>
                        </div>
                        <hr>
                        <div class="row">
                            <div class="col-sm-3">
                                <p class="mb-0">Mobil:</p>
                            </div>
                            <div class="col-sm-9">
                                <p class="mb-0">{{user.mobile}}</p>
                            </div>
                        </div>
                        <hr>
                        <div class="row">
                            <div class="col-sm-3">
                                <p class="mb-0">Address:</p>
                            </div>
                            <div class="col-sm-9">
                                <p class="mb-0">{{user.address}}</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-md-6">
                        <div class="card mb-4 mb-md-0">
                            <div class="card-body">
                                <h5 class="mb-0">LATEST PARKING:</h5>
                                <div v-if="latestParking.date != ''">
                                    <li class="list-group-item py-3">
                                        <p class="mb-0">
                                            Date:
                                        </p>
                                        <p class="mb-0">{{latestParking.date}}</p>
                                    </li>
                                    <li class="list-group-item py-3">
                                        <p class="mb-0">
                                            Location:
                                        </p>
                                        <p class="mb-0">{{latestParking.location}}</p>
                                    </li>
                                    <li class="list-group-item py-3">
                                        <p class="mb-0">
                                            Cost:
                                        </p>
                                        <p class="mb-0">{{latestParking.date}}</p>
                                        </li>
                                </div>
                                <div v-else>
                                    <p class="my-3">
                                        You don't have any parkings yet...
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<style scoped>
h5,
p {
    color: black !important;
}
</style>

<script>
import axios from 'axios'

export default {
  data() {
    return {
        user:{
            firstname: "",
            lastname: "",
            email: "",
            mobile: "",
            address: "",
        },
        registeredCars: [],
        latestParking:{
            date: "",
            location: "",
            cost: ""
        }
    }
  },
  watch: {
  },
  methods:{
    getNumberplates: function() {
      axios.get( '/api/userLicenseplates', {
        params: {
            userLicenseplates: "username"
        }
      })
      .then( response => {
        this.registeredCars = response;
      console.log(response);
      })
      .catch( error => {
        console.warn('userLicenseplates', error )
      });
    },
  },
  mounted() {
    console.log(this.msg) // 'hello'
  }
}


</script>
