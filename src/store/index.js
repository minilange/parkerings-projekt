import Vuex from "vuex"
import axios from "axios"

axios.interceptors.request.use(function (config) {
  // Do something before request is sent
  console.log(config)
  return config;
}, function (error) {
  // Do something with request error
  return Promise.reject(error);
});

// axios.interceptors.response.use(function())


export default new Vuex.Store({
  state: {
    carInfo: {},
    admin: {},
    api: "https://parking-project-api.azurewebsites.net/api",
    user: {},
    secret: "Th1s1s4S3cr3t"
  },
  getters: {
    getCarInfo: (state) => state.carInfo,
    getAdminInfo: (state) => state.admin,
    getUserInfo: (state) => state.user,
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
    }
  },
  actions: {
    async numberPlateLookup(state, numberPlate) {
      try {
        // Call Python backend
        console.log(numberPlate);
        await axios.get(state.api + "/numberPlateLookup")
          .then((response) => {
            console.log(response)
            return response;
          })
          .catch((error) => {
            console.error(error)
          })


      } catch (error) {
        console.log('numberPlateLookup: ' + error)
      }
    },
    async callAPI(state, payload) {
      const method = payload.method;
      const endpoint = payload.endpoint;
      const body = payload.body

      if(method == "GET") {
        await axios.get(this.state.api + "/" + endpoint + "/")
        .then((response) => {
          console.log(response);
        }).catch((error) => {
          console.warn(error);
        })
        
      } else if(method == "POST") {
        // this.form.apiSend = {firstname: this.form.firstname, lastname: this.form.lastname, email: this.form.email, phone: this.form.phone, password: SHA256(this.form.password, this.$store.state.secret).toString(), ccCode: this.form.ccCode.code}

        axios.post(this.state.api + "/" + endpoint + "/", body)
          .then((response) => {
            console.log(response);
          })
          .catch((error) => {
            console.warn("register", error);
          });
      } else if(method == "PATCH") {
        /**** AXIOS PATCH ****/
        console.log('PATCH');
      }
    },
    async getCars() {
      console.log('** ' + this.state.api);
      await axios.get(this.state.api + "/regLicenseplates/")
        .then((response) => {
          console.log(response)
          this.commit('SET_ADMIN_INFO', { "data": response.data, "key": 'cars' })
          return response.data
        }).catch((error) => {
          console.log(error)
        })

    },
    async getAreas() {
      console.log('** ' + this.state.api);
      await axios.get(this.state.api + "/areas/")
        .then((response) => {
          console.log(response)
          this.commit('SET_ADMIN_INFO', { "data": response.data, "key": 'areas' })
          return response.data
        }).catch((error) => {
          console.log(error)
        })
    },
    async getParkings() {
      // INCLUDE USERID?
      console.log('getParkings');
      //   await axios.get(this.state.api + "/parkings/")
      //   .then((response) => {
      //     console.log(response)
      //     this.commit('SET_ADMIN_INFO', {"data": response.data, "key": 'parkings'})
      //     return response.data
      //   }).catch((error) => {
      //     console.log(error)
      //   })
    },

  },
})
