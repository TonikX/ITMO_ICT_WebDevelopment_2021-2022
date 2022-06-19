<template>
	<div class="container">
		<b-form class="w-50 mx-auto" method='post'>
			<h2>Проживание</h2>
			<b-form-group
				label="Номер комнаты"
				label-for="room"
			>
				<b-form-select name="room" v-model="room" :options="rooms"></b-form-select>

				<p>{{room_error}}</p>
			</b-form-group>

			<b-form-group
				label="Клиент"
				label-for="client"
			>
				<b-form-select name="client" v-model="client" :options="clients"></b-form-select>
				<p>{{client_error}}</p>
			</b-form-group>

			<b-form-group
				label="Дата заселения"
				label-for="in_date"
			>
				<b-form-datepicker
					name="in_date"
					v-model="in_date"
				/>
			</b-form-group>

			<b-form-group
				label="Дата выселения"
				label-for="out_date"
			>
				<b-form-datepicker
					name="out_date"
					v-model="out_date"
				/>
			</b-form-group>

			<b-button @click="save()" type="button" variant="success">Сохранить</b-button>
		</b-form>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'InhabitationForm',
	data () {
		return {
			id: '',
			room: '',
			room_error: '',
			client: '',
			client_error: '',
			out_date: '',
			in_date: '',
			rooms: [],
			clients: []
		}
	},
	props: ['mode'],
	mounted () {
		this.id = this.$route.params.id
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/rooms/',
			responseType: 'json',
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then(response => {
			response.data.forEach(element => {
				this.rooms.push({ value: element.id, text: element.number })
			})
		})

		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/clients/',
			responseType: 'json',
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then(response => {
			response.data.forEach(element => {
				this.clients.push({ value: element.id, text: element.full_name })
			})
		})

		if (this.mode === 'update') {
			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/inhabitations/' + this.id,
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				console.log(response)
				this.room = response.data.room
				this.client = response.data.client
				this.in_date = response.data.in_date
				this.out_date = response.data.out_date
			})
		}
	},
	methods: {
		save () {
			let method
			let url
			if (this.mode === 'add') {
				method = 'post'
				url = 'http://127.0.0.1:8000/inhabitations/'
			} else {
				method = 'put'
				url = 'http://127.0.0.1:8000/inhabitations/' + this.id + '/'
			}

			axios({
				method: method,
				url: url,
				responseType: 'json',
				data: {
					room: this.room,
					client: this.client,
					in_date: this.in_date,
					out_date: this.out_date
				},
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				console.log(response)
				window.location.href = '/inhabitations'
			}).catch(error => {
				console.log(error.response)
			})
		}
	}
}
</script>

<style>

</style>
