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
    api: "https://parking-project-api.azurewebsites.net/api"
  },
  getters: {
    getCarInfo: (state) => state.carInfo,
    getAdminInfo: (state) => state.carInfo
  },
  mutations: {
    SET_CAR(state, carInfo) {
      state.carInfo = carInfo
    },
    SET_ADMIN_INFO(state, payload) {
      state.admin[payload.key] = payload.data
    }
  },
  actions: {
    async numberPlateLookup(state, numberPlate) {
      try {
        // Call PHP backend
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
    async callAPI(state, input, method) {
      try {
        console.log(state, input, method)
      } catch (error) {
        console.log('callAPI: ' + error)
      }
    },
    async getCars() {
      console.log('** ' + this.state.api);
      await axios.get(this.state.api + "/regLicenseplates/")
      .then((response) => {
        console.log(response)
        this.commit('SET_ADMIN_INFO', {"data": response.data, "key": 'cars'})
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
        this.commit('SET_ADMIN_INFO', {"data": response.data, "key": 'areas'})
        return response.data
      }).catch((error) => {
        console.log(error)
      })

    },
    
  },
})
