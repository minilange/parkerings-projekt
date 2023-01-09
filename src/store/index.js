import Vuex from "vuex"

export default new Vuex.Store({
  state: {
    statePokemonDataList: [],
    stateFavoritePokemonList: [],
  },
  mutations: {
    setPokemonData(state, list){
      state.statePokemonDataList = list;
    }
  },
  actions: {
    setPokemonData(context, payload) {
      context.commit("setPokemonData", payload);
    }
  },
})
