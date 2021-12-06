<template>
	<b-container
	class="mt-5 w-50"
	>
		<b-form method='post'>
			<h2>Вход</h2>
			<b-form-group
				label="Login"
				label-for="username"
			>
				<b-form-input
					name="username"
					type="text"
					v-model="login"
					required
				/>
				<p>{{login_error}}</p>
			</b-form-group>

			<b-form-group
				label="password"
				label-for="password"
			>
				<b-form-input
					name="password"
					type="password"
					v-model="password"
					required
				/>
				<p>{{password_error}}</p>
			</b-form-group>

			<b-button @click="signIn()" type="button" variant="success">Войти</b-button>
		</b-form>

	</b-container>

</template>

<script>
import axios from 'axios'

export default {
	name: 'Login',
	data () {
		return {
			login: '',
			password: '',
			login_error: '',
			password_error: ''
		}
	},
	methods: {
		signIn () {
			axios({
				method: 'post',
				url: 'http://127.0.0.1:8000/auth/token/login/',
				data: {
					username: this.login,
					password: this.password
				},
				responseType: 'json'
			}).then((response) => {
				sessionStorage.setItem('auth_token', response.data.auth_token)

				window.location.reload()
			}).catch((error) => {
				this.login_error = ''
				this.password_error = ''
				try {
					this.login_error = error.response.data.username[0]
				} catch (error) {
					console.log(error.response)
				}
				try {
					this.password_error = error.response.data.password[0]
				} catch (error) {
					console.log(error.response)
				}
			})
		}
	}

}

</script>

<style>

</style>
