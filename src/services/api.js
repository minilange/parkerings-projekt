let _this;
export default function({ app }, inject) {
    _this = app
    inject('ApiService', ApiService)
}

const ApiService = {
    post(resource, params) {
        return _this.$axios.$post(`${resource}`, params)
    }
}