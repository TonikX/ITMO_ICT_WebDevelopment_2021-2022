<template>
    <main class="main-bg">
        <h1 class="main-h1">
            Выберите ваш город:
        </h1>
        <select v-model="city" class="select" v-on:change="getWeather()">
            <option></option>
            <option style="color: #e4e4e4" v-for="(el, index) in userCity" :key="index" :value="el.city">{{el.city.name}}</option>
        </select>

        <h1 class="main-h1">
            Показать прогноз:
        </h1>
        <div>
            <button class="button" v-on:click="setCount(1)">Сейчас</button>
            <button class="button" v-on:click="setCount(5)">На 5 дней</button>
            <button class="button" v-on:click="setCount(8)">На 8 дней</button>
            <button v-if="count > 0" class="button" v-on:click="setCount(0)">Скрыть</button>
        </div>
        <div class="container-weather">
            <div v-for="(el, index) in weatherApiData" :key="index">
                <WeatherOneday :weather="el" v-if="index < count"/>
            </div>
        </div>
    </main>
</template>

<script>
    import {mapGetters} from "vuex";
    import WeatherOneday from "@/components/WeatherOneday";

    export default {
        name: "Main",
        components: {WeatherOneday},
        data() {
            return {
                city: 0,
                count: 0
            };
        },
        computed: {
            ...mapGetters({
                userCity: 'userCity',
                weatherApiData: 'weatherApiData',
            })
        },
        mounted() {
            this.$store.dispatch('getUserCities')
        },
        methods: {
            setCount(val) {
                this.count = val
            },
            getWeather() {
                this.$store.dispatch('getWeatherApiData', this.city)
            }
        },
    }
</script>

<style scoped>

</style>