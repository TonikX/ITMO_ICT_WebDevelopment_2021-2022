<template>
    <b-form @submit.prevent="onSubmit(form)">
        <div class="form-group">
            <label for="username">Логин:</label>
            <b-input required v-model="form.username" type="text" id="username" placeholder="Введите ник..."></b-input>
        </div>
        <div class="form-group">
            <label for="first_name">Имя:</label>
            <b-input required v-model="form.first_name" type="text" id="first_name" placeholder="Введите ваше имя..."></b-input>
        </div>
        <div class="form-group">
            <label for="last_name">Фамилия:</label>
            <b-input required v-model="form.last_name" type="text" id="last_name" placeholder="Введите вашу фамилию..."></b-input>
        </div>

        <div class="form-group">
            <label for="password">Пароль:</label>
            <b-input required v-model="form.password" type="password" id="password" placeholder="Придумайте пароль..."></b-input>
        </div>
        <b-button  variant="primary" type="submit">Зарегестрироваться</b-button>
        <p class="mt-3">Уже зарегистрированы?
            <router-link to="/signin">Войдите</router-link>
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
                    first_name: "",
                    last_name: "",
                    password: ""
                }
            };
        },
        methods: {
            onSubmit(form) {
                this.$store.dispatch('Register', form)
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