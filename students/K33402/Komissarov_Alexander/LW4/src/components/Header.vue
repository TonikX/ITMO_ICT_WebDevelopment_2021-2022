<template>
    <header class="nav-bg">
        <ul class="nav-group" align="center">
            <li style="display:inline">
                <img src="../assets/main.svg">
            </li>
            <router-link to="/" style="display:inline" class="nav-text">
                Главная
            </router-link>
            <router-link to="/cabinet" style="display:inline" class="nav-text" >
                Мои города
            </router-link>
            <router-link to="/login" style="display:inline" class="nav-text" >
                Вход
            </router-link>
            <router-link to="/registration" style="display:inline" class="nav-text" >
                Регистрация
            </router-link>
        </ul>
    </header>
</template>

<script>
    export default {
        name: "Header"
    }
</script>

<style scoped>

</style>