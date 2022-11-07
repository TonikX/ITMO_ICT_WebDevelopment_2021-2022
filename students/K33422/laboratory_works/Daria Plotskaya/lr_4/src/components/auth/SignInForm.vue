<template>
    <b-form @submit.prevent="onSubmit(form)">
        <div class="form-group">
            <label for="username">Логин:</label>
            <b-input v-model="form.username" type="text" id="username" placeholder="Логин..."></b-input>
        </div>
        <div class="form-group">
            <label for="password">Пароль:</label>
            <b-input v-model="form.password" type="password" id="password" placeholder="Пароль..."></b-input>
        </div>
        <b-button variant="primary" type="submit">Войти</b-button>
        <p class="mt-3">Ещё не зарегистрированы?
            <router-link to="/signup">Регистрация</router-link>
        </p>
    </b-form>
</template>

<script>
    export default {
        name: "SignInForm",
        data() {
            return {
                form: {
                    username: "",
                    password: "",
                }
            };
        },
        methods: {
            onSubmit(form) {
                this.$store.dispatch('Login', form)
            }
        },

    };
</script>

<style scoped>
    .form-group {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        margin-bottom: 20px;
        margin-top: 20px;
    }
</style>