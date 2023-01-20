import Vuex from "vuex"
import axios from "axios"

// axios.interceptors.request.use(function (config) {
//   // Do something before request is sent
//   console.log(config)
//   return config;
// }, function (error) {
//   // Do something with request error
//   return Promise.reject(error);
// });

// axios.interceptors.response.use(function())


export default new Vuex.Store({
  state: {
    searching: false,
    carInfo: {},
    admin: {},
    api: "https://parking-project-api.azurewebsites.net/api",
    user: {},
    time: {
      hours: 0,
      minutes: 0
    },
    secret: "Th1s1s4S3cr3t"
  },
  getters: {
    getCarInfo: (state) => state.carInfo,
    getAdminInfo: (state) => state.admin,
    getUserInfo: (state) => state.user,
    getParkingTime: (state) => state.time
  },
  mutations: {
    SET_CAR(state, carInfo) {
      state.carInfo = carInfo
    },
    SET_ADMIN_INFO(state, payload) {
      state.admin[payload.key] = payload.data
    },
    SET_USER_INFO(state, userInfo) {
      state.user = userInfo
    },
    SET_SEARCHING(state, searching) {
      state.searching = searching
    },
    SET_PARKING_TIME(state, time) {
      state.time = time
    }
  },
  actions: {
    async licensePlateLookup(state, licensePlate) {
      // Call Python backend to get car info from NummerpladeAPI.dk

      try {
        this.commit('SET_SEARCHING', true) // Set searching to true
        await axios.get(this.state.api + "/licenseplateLookup/?licenseplate=" + licensePlate)
          .then((response) => {
            this.commit('SET_CAR', response.data) // Set car in state
          })
          .catch((error) => {
            console.error(error)
          })
          
        this.commit('SET_SEARCHING', false) // Set searching to false

      } catch (error) {
        console.log('licensePlateLookup: ' + error)
      }
    },
    async callAPI(state, payload) {
      const method = payload.method;
      const endpoint = payload.endpoint;
      let body;
      let params;
      try {
        body = payload.body
      } catch (error) {
        body = '';
        console.log('callAPI: ' + error)
      }
      try {
        params = payload.params
      } catch (error) {
        params = '/';
        console.log('callAPI: ' + error)
      }

      if(method == "GET") {
        await axios.get(this.state.api + "/" + endpoint + "/")
        .then((response) => {
          console.log(response);
        }).catch((error) => {
          console.warn("GET", error);
        })
      } else if(method == "POST") {
        // this.form.apiSend = {firstname: this.form.firstname, lastname: this.form.lastname, email: this.form.email, phone: this.form.phone, password: SHA256(this.form.password, this.$store.state.secret).toString(), ccCode: this.form.ccCode.code}
        console.log("TESTAPI:", endpoint, params)
        axios.post(this.state.api + "/" + endpoint + "/", body)
          .then((response) => {
            console.log(response);
          })
          .catch((error) => {
            console.warn("POST", error);
          });
      } else if(method == "PATCH") {
        axios.patch(this.state.api + "/" + endpoint + "/", body)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.warn("PATCH", error);
        });
      }
    },
    async getCars() {
      await axios.get(this.state.api + "/regLicenseplates/")
        .then((response) => {
          this.commit('SET_ADMIN_INFO', { "data": response.data, "key": 'cars' })
          return response.data
        }).catch((error) => {
          console.log(error)
        })

    },
    async getAreas() {
      await axios.get(this.state.api + "/areas/")
        .then((response) => {
          this.commit('SET_ADMIN_INFO', { "data": response.data, "key": 'areas' })
          return response.data
        }).catch((error) => {
          console.log(error)
        })
    },
    async getParkings() {
      // INCLUDE USERID?
      // console.log('getParkings');
      //   await axios.get(this.state.api + "/parkings/")
      //   .then((response) => {
      //     console.log(response)
      //     this.commit('SET_ADMIN_INFO', {"data": response.data, "key": 'parkings'})
      //     return response.data
      //   }).catch((error) => {
      //     console.log(error)
      //   })
    },
    async logOut() {
      if (Object.keys(this.state.user).length > 0){
        this.state.user = {}
      } else {
        console.warn("You can't logout, without being logged in")
      }
    }
  },
})
