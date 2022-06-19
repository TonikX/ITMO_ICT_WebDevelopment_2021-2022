<template>
	<div class="container">
		<b-form class="w-50 mx-auto" method='post'>
			<h2>Расписание уборки</h2>
			<b-form-group
				label="Уборщик"
				label-for="cleaner"
			>
				<b-form-select name="cleaner" v-model="cleaner" :options="cleaners"></b-form-select>

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
			</b-form-group>

			<b-form-group
				label="Дата уборки"
				label-for="cleaning_day"
			>
				<b-form-datepicker
					name="cleaning_day"
					v-model="cleaning_day"
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
			cleaner: '',
			floor: '',
			cleaning_day: '',

			cleaners: []
		}
	},
	props: ['mode'],
	mounted () {
		this.id = this.$route.params.id
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/cleaners/',
			responseType: 'json',
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then(response => {
			response.data.forEach(element => {
				this.cleaners.push({ value: element.id, text: element.full_name })
			})
		})

		if (this.mode === 'update') {
			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/cleanings/' + this.id,
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				console.log(response)
				this.cleaner = response.data.cleaner
				this.floor = response.data.cleaning_floor
				this.cleaning_day = response.data.cleaning_day
			})
		}
	},
	methods: {
		save () {
			let method
			let url
			if (this.mode === 'add') {
				method = 'post'
				url = 'http://127.0.0.1:8000/cleanings/'
			} else {
				method = 'put'
				url = 'http://127.0.0.1:8000/cleanings/' + this.id + '/'
			}

			axios({
				method: method,
				url: url,
				responseType: 'json',
				data: {
					cleaner: this.cleaner,
					cleaning_floor: this.floor,
					cleaning_day: this.cleaning_day
				},
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				console.log(response)
				window.location.href = '/cleanings'
			}).catch(error => {
				console.log(error.response)
			})
		}
	}
}
</script>

<style>

</style>
