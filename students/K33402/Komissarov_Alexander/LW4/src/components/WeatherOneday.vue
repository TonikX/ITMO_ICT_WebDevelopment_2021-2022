<template>
    <div class="t1" id="i1">
        <h3 class="date">
            Дата: {{ new Date(weather.dt * 1000).toLocaleDateString("en-US") }}
        </h3>
        <h3 class="max">
            Макс: {{ weather.temp.max }}°C
        </h3>
        <h3 class="min">
            Мин: {{ weather.temp.min }}°C
        </h3>
        <h3 class="wind">
            Ветер: {{ weather.wind_speed }} м/с
        </h3>
    </div>
</template>

<script>
    export default {
        name: "WeatherOneday",
        props: ['weather'],
    }
</script>

<style scoped>

</style>