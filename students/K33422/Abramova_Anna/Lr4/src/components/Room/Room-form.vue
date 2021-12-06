<template>
	<div class="container">
		<b-form class="w-50 mx-auto" method='post'>
			<h2>Комната</h2>
			<b-form-group
				label="Номер комнаты"
				label-for="number"
			>
				<b-form-input
					name="number"
					type="number"
					v-model="number"
				/>
				<p>{{number_error}}</p>
			</b-form-group>

			<b-form-group
				label="Этаж"
				label-for="floor"
			>
				<b-form-input
					name="floor"
					type="number"
					v-model="floor"
				/>
				<p>{{floor_error}}</p>
			</b-form-group>

			<b-form-group
				label="Стоимость проживания"
				label-for="cost_of_living"
			>
				<b-form-input
					name="cost_of_living"
					type="number"
					v-model="cost_of_living"
				/>
				<p>{{cost_of_living_error}}</p>
			</b-form-group>

			<b-form-group
				label="Тип комнаты"
				label-for="room_type"
			>
				<b-form-select name='room_type' v-model="room_type" :options="options"></b-form-select>
			</b-form-group>

			<b-button @click="save()" type="button" variant="success">Сохранить</b-button>
		</b-form>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'RoomForm',
	data () {
		return {
			id: '',
			number: '',
			number_error: '',
			floor: '',
			floor_error: '',
			cost_of_living: '',
			cost_of_living_error: '',
			room_type: '',
			options: [1, 2, 3]
		}
	},
	props: ['mode'],
	mounted () {
		this.id = this.$route.params.id
		if (this.mode === 'update') {
			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/rooms/' + this.id,
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				console.log(response)
				this.number = response.data.number
				this.floor = response.data.floor
				this.cost_of_living = response.data.cost_of_living
				this.room_type = response.data.room_type
			})
		}
	},
	methods: {
		save () {
			let method
			let url
			if (this.mode === 'add') {
				method = 'post'
				url = 'http://127.0.0.1:8000/rooms/'
			} else {
				method = 'put'
				url = 'http://127.0.0.1:8000/rooms/' + this.id + '/'
			}

			axios({
				method: method,
				url: url,
				responseType: 'json',
				data: {
					number: this.number,
					floor: this.floor,
					cost_of_living: this.cost_of_living,
					room_type: this.room_type
				},
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				console.log(response)
				window.location.href = '/rooms'
			}).catch(error => {
				console.log(error.response)
			})
		}
	}
}
</script>

<style>

</style>
