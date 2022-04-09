<template>
    <footer class="footer-bg">
        <nav class="footer-group">
            <router-link to="/about" style="display:inline" class="nav-text">
                О сайте
            </router-link>
            <router-link to="/author" style="display:inline" class="nav-text">
                Об авторе
            </router-link>
        </nav>
    </footer>
</template>

<script>
    export default {
        name: "Footer"
    }
</script>

<style scoped>

</style>