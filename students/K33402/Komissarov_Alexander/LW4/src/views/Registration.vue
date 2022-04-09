<template>
    <main class="main-bg">
        <form @submit.prevent="login">
            <div class="form-group">
                <label class="main-h1" for="email">
                    Email:
                </label>
                <input v-model="form.email" type="email" class="input-user" id="email"
                       placeholder="Введите почту"/>
            </div>
            <div class="form-group">
                <label class="main-h1" for="username">
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
            <button class="button-user">Регистрация</button>
        </form>
    </main>
</template>

<script>
    export default {
        name: "Registration",
        data() {
            return {
                form: {
                    email: "",
                    username: "",
                    password: "",
                }
            };
        },
        methods: {
            login() {
                this.$store.dispatch('Registration', this.form);
            }
        }
    }
</script>

<style scoped>

</style>