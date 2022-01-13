<template>
    <div class="d-flex justify-content-center">
        <form @submit.prevent="login">
            <input-field v-model="username" type="text" placeholder="Username" icon="person-fill" />
            <input-field v-model="password" type="password" placeholder="Password" icon="lock-fill" />
            <b-row class="mt-3 d-flex justify-content-center">
                <input class="btn btn-primary mb-3" type="submit" value="Log in"/>
            </b-row>
        </form>
    </div>
</template>

<script>
import InputField from '@/components/InputField.vue'

export default {
    name: 'LoginForm',
    components: {
        InputField
    },
    data: () => ({
        username: '',
        password: ''
    }),
    methods: {
        async login () {
            const url = 'http://127.0.0.1:8000/auth/token/login/'

            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username: this.username, password: this.password })
            })

            const data = await response.json()
            console.log(data)

            if (data.auth_token !== undefined) {
                sessionStorage.setItem('auth_token', data.auth_token)
                this.$store.commit('isLoggedUpdate')
                this.$router.push('/')
            }
        }
    }

}
</script>

<style scoped>
.input-field input {
    margin: 0.5rem;
}

.input-field input[type='checkbox'], input[type='radio'] {
    margin-left: 3rem;
}

::placeholder, input[type='email'], input[type='password'] {
    color: var(--color-placeholder);
    background-color: var(--background-color-input);
    text-indent: 0.3rem;
}

.fa {
    font-size: 1.5rem;
    padding-right: 1rem;
    width: 1rem;
}
</style>
