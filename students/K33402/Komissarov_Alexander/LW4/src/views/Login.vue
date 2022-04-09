<template>
    <main class="main-bg">
        <form @submit.prevent="login">
            <div class="form-group">
                <label class="main-h1">
                    Логин:
                </label>
                <input v-model="form.username" type="text" class="input-user" id="username"
                       placeholder="Введите ваш логин"/>
            </div>
            <div class="form-group">
                <label for="Password" class="main-h1">
                    Пароль:
                </label>
                <input v-model="form.password" type="password" id="Password" placeholder="Введите пароль"
                       class="input-user"/>
            </div>
            <button class="button-user">Вход</button>
        </form>
    </main>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                form: {
                    username: "",
                    password: ""
                }
            };
        },
        methods: {
            login() {
                this.$store.dispatch('Login', this.form);
            }
        }
    }
</script>

<style scoped>

</style>