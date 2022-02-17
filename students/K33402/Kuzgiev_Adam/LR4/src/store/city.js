import {instance} from "@/store/index";

export const CityModule = {
    state: () => ({
        data: []
    }),
    getters: {

    },
    mutations: {
        ADD_CITY_MODULE: (state, data) => {
            state.data = data
        },
    },
    actions: {
        ADD_CITY: (state, payload) => {
            instance.post(`/cities/${payload}/`, {city_id: payload},{
                headers: {
                    Authorization: `Bearer ${JSON.parse(localStorage.getItem('token'))?.access}`
                }
            }).then(function (data) {
                    if (200 <= data.status < 300) {
                        return data.data;
                    }
                    return Promise.reject(data.status);
                })
                .then(state.dispatch('GET_USER'))
        },
        REMOVE_CITY: ({dispatch}, payload) => {
            instance.delete(`/cities/${payload}/`, {
                headers: {
                    Authorization: `Bearer ${JSON.parse(localStorage.getItem('token'))?.access}`
                }
            }).finally( () => {
                setTimeout(() =>{
                    dispatch('GET_USER')
                }, 2000)
            })
        }
    }
}
