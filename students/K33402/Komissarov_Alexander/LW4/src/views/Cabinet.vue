<template>
    <main class="main-bg">
        <h1 class="main-h1">
            Закрепленные города:
        </h1>
        <template v-if="userCity">
            <div class="container" v-for="(el, index) in userCity" :key="index">
                <p class="text">{{el.city.name}}</p>
                <button class="button" v-on:click="removeCity(el.id)">Открепить</button>
            </div>
        </template>
        <div v-else>
            <p>Вы еще не закрепили не один город</p>
        </div>

        <h1 class="main-h1">
            Вашего города нет в списке? Добавьте его:
        </h1>
        <select v-model="city" class="select">
            <option></option>
            <option v-for="(el, index) in cities" :key="index" :value="el.id">{{el.name}}</option>
        </select>
        <button class="button" v-on:click="addCity(city)">Добавить</button>
    </main>
</template>

<script>
    import {mapGetters} from "vuex";

    export default {
        name: "Cabinet",
        data() {
            return {
                city: 0
            };
        },
        computed: {
            ...mapGetters({
                userCity: 'userCity',
                cities: 'cities',
            })
        },
        mounted() {
            this.$store.dispatch('getUserCities')
            this.$store.dispatch('getCities')
        },
        methods: {
            removeCity(val) {
                this.$store.dispatch('delUserCity', val)
            },
            addCity(val) {
                this.$store.dispatch('addUserCity', {city: val})
            }
        },
    }
</script>

<style scoped>
    .container {
        display: flex;
        align-items: center;
        gap: 10px;
        height: 30px;
        margin-top: 10px;
        margin-bottom: 10px;
    }
.text {
    font-size: 20px;
    color: #e4e4e4;
}
</style>