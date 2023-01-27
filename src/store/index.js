import Vuex from "vuex"
import axios from "axios"
import router from "../router"

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
    getParkingTime: (state) => state.time,
    getParkingTimeMinutes: (state) => state.time.hours * 60 + state.time.minutes
  },
  mutations: {
    SET_CAR(state, carInfo) {
      state.carInfo = carInfo
    },
    SET_ADMIN_INFO(state, payload) {
      state.admin[payload.key] = payload.data
    },
    SET_USER_INFO(state, userInfo) {
      try {
        // Expiry two days from now
        userInfo.tokenExpiration = new Date(new Date().getTime() + 2 * 24 * 60 * 60 * 1000)
      } catch (error) {
        console.warn(error)
      }
      state.user = userInfo
      // Save token and userId in local storage
      localStorage.setItem('userInfo', JSON.stringify(userInfo))
    },
    SET_SEARCHING(state, searching) {
      state.searching = searching
    },
    SET_PARKING_TIME(state, time) {
      state.time = time
    }
  },
  actions: {
    setUserInfoFromLocalStorage() {
      let userInfo = JSON.parse(localStorage.getItem('userInfo'))
      if (userInfo) {
        this.commit('SET_USER_INFO', userInfo)
      }
    },
    async licensePlateLookup(state, licensePlate) {
      // Call Python backend to get car info from NummerpladeAPI.dk

      try {
        this.commit('SET_SEARCHING', true) // Set searching to true
        await axios.get(this.state.api + "/licenseplateLookup/", { params: {token: this.state.user.token, userId: this.state.user.userId, licenseplate: licensePlate}})
          .then((response) => {
            this.commit('SET_CAR', response.data) // Set car in state
          })
          .catch((error) => {
            console.warn(error)
          })
          
        this.commit('SET_SEARCHING', false) // Set searching to false

      } catch (error) {
        console.warn('licensePlateLookup: ' + error)
      }
    },
    async detectLicensePlate(state, image) {
      let formData = new FormData();
      formData.append('file', image);
      let result = '';

      try {
        this.commit('SET_SEARCHING', true) // Set searching to true
        await axios.post(this.state.api + "/detectLicenseplate/", formData, { headers: { 'Content-Type': 'multipart/form-data' }})
          .then((response) => {
            this.commit('SET_SEARCHING', false) // Set searching to false
            result = response.data.licenseplate;
          })
          .catch((error) => {
            console.warn(error)
          })

        this.commit('SET_SEARCHING', false) // Set searching to false
        return result;
          

      } catch (error) {
        console.warn('licensePlateLookup: ' + error)
      }
    },
    async loginUser(state, payload) {
      this.commit('SET_SEARCHING', true)
      await axios
        .get(this.state.api + "/login/", payload)
        .then((response) => {
          this.commit("SET_USER_INFO", response.data);
          router.push('/')
        })
        .catch((error) => {
          console.warn("login", error);
          alert('Wrong email or password')
        });

      this.commit('SET_SEARCHING', false)
    },

    async callAPI(state, payload) {
      const method = payload.method;
      const endpoint = payload.endpoint;
      
      if(!this.state.user.token || !this.state.user.userId) {
        return console.log("No token or userId");
      } 
      
      const token = this.state.user.token;
      const userId = this.state.user.userId;

      let body;
      let params;
      try {
        body = payload.body
      } catch (error) {
        body = '';
        console.warn('callAPI: ' + error)
      }
      try {
        params = payload.params;
      } catch (error) {
        params = '/';
        console.warn('callAPI: ' + error)
      }

      this.commit('SET_SEARCHING', true) // Set searching to true
      let result = '';

      if(method == "GET") {
        await axios.get(this.state.api + "/" + endpoint + "/", { params: {token: token, userId: userId}})
        .then((response) => {
          result = response.data;
          this.commit('SET_SEARCHING', false)
        }).catch((error) => {
          console.warn("GET", error);
        })
      } else if(method == "POST") {
        // this.form.apiSend = {firstname: this.form.firstname, lastname: this.form.lastname, email: this.form.email, phone: this.form.phone, password: SHA256(this.form.password, this.$store.state.secret).toString(), ccCode: this.form.ccCode.code}
        console.log("TESTAPI:", endpoint, params)
        await axios.post(this.state.api + "/" + endpoint + "/", body)
          .then((response) => {
            result = response.data;
          })
          .catch((error) => {
            console.warn("POST", error);
          });
      } else if(method == "PATCH") {
        await axios.patch(this.state.api + "/" + endpoint + "/", body)
        .then((response) => {
          result = response.data;
        })
        .catch((error) => {
          console.warn("PATCH", error);
        });
      }

      this.commit('SET_SEARCHING', false)
      return result;
    },
    async getCars() {
      await axios.get(this.state.api + "/regLicenseplates/", { params: {token: this.state.user.token, userId: this.state.user.userId } })
        .then((response) => {
          this.commit('SET_ADMIN_INFO', { "data": response.data, "key": 'cars' })
          return response.data
        }).catch((error) => {
          console.log(error);
        })

    },
    async getAreas() {
      await axios.get(this.state.api + "/areas/", { params: {token: this.state.user.token, userId: this.state.user.userId } })
        .then((response) => {
          this.commit('SET_ADMIN_INFO', { "data": response.data, "key": 'areas' })
          return response.data
        }).catch((error) => {
          console.warn(error)
        })
    },
    async getParkings() {
        await axios.get(this.state.api + "/parkings/", { params: {token: this.state.user.token, userId: this.state.user.userId } })
        .then((response) => {
          this.commit('SET_ADMIN_INFO', {"data": response.data, "key": 'parkings'})
          return response.data
        }).catch((error) => {
          console.warn(error)
        })
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