import Vuex from "vuex"
import axios from "axios"

axios.interceptors.request.use(function (config) {
  // Do something before request is sent
  console.log('axioes interceptor')
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
    api: "https://parking-project-api.azurewebsites.net/api"
  },
  getters: {
    getCarInfo: (state) => state.carInfo,
  },
  mutations: {
    SET_CAR(state, carInfo) {
      state.carInfo = carInfo
    }
  },
  actions: {
    async numberPlateLookup(state, numberPlate) {
      try {
        // Call PHP backend
        console.log(numberPlate);
        axios.get('numberPlateAPI.php')
        .then((response) => {
          console.log(response)
        })
        .catch((error) => {
          console.error(error)
        })
        // const response = fetch(/* PHP Endpoint */)
        
      } catch (error) {
        console.log('numberPlateLookup: ' + error)
      }
    },
    
  },
})
