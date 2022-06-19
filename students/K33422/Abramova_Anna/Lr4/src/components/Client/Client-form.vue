<template>
	<div class="container">
		<b-form class="w-50 mx-auto" method='post'>
			<h2>Вход</h2>
			<b-form-group
				label="ФИО"
				label-for="full_name"
			>
				<b-form-input
					name="full_name"
					type="text"
					v-model="full_name"
				/>
				<p>{{full_name_error}}</p>
			</b-form-group>

			<b-form-group
				label="Паспорт"
				label-for="pasport"
			>
				<b-form-input
					name="pasport"
					type="text"
					v-model="pasport"
				/>
				<p>{{pasport_error}}</p>
			</b-form-group>

			<b-form-group
				label="Город"
				label-for="city"
			>
				<b-form-input
					name="city"
					type="text"
					v-model="city"
				/>
				<p>{{pasport_error}}</p>
			</b-form-group>

			<b-button @click="save()" type="button" variant="success">Сохранить</b-button>
		</b-form>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'ClientForm',
	data () {
		return {
			id: '',
			full_name: '',
			full_name_error: '',
			pasport: '',
			pasport_error: '',
			city: '',
			city_error: ''
		}
	},
	props: ['mode'],
	mounted () {
		this.id = this.$route.params.id
		if (this.mode === 'update') {
			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/clients/' + this.id,
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				this.full_name = response.data.full_name
				this.pasport = response.data.pasport
				this.city = response.data.city
			})
		}
	},
	methods: {
		save () {
			let method
			let url
			if (this.mode === 'add') {
				method = 'post'
				url = 'http://127.0.0.1:8000/clients/'
			} else {
				method = 'put'
				url = 'http://127.0.0.1:8000/clients/' + this.id + '/'
			}

			axios({
				method: method,
				url: url,
				responseType: 'json',
				data: {
					city: this.city,
					full_name: this.full_name,
					pasport: this.pasport
				},
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				console.log(response)
				window.location.href = '/clients'
			}).catch(error => {
				console.log(error.response)
			})
		}
	}
}
</script>

<style>

</style>
