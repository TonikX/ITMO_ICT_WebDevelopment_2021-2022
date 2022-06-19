<template>
	<div class="container">
		<h1>Уборщик: {{cleaner_name}}</h1>
		<p>Этаж: {{item.cleaning_floor}}</p>
		<p>Дата уборки: {{item.cleaning_day}}</p>

		<a :href="'/cleaning/update/' + this.$route.params.id" class="btn btn-success">Редактировать</a>
		<button @click="delete_item()" class="btn btn-danger">Удалить</button>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'cleaningsItem',
	data () {
		return {
			item: [],
			cleaner_name: ''
		}
	},
	props: ['id'],
	mounted () {
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/cleanings/' + this.$route.params.id,
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then((response) => {
			this.item = response.data
			console.log(this.item.cleaner)

			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/cleaners/' + this.item.cleaner + '/',
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				this.cleaner_name = response.data.full_name
			})
		})
	},
	methods: {
		delete_item () {
			if (confirm('Удалить?')) {
				axios({
					method: 'delete',
					url: 'http://127.0.0.1:8000/cleanings/' + this.$route.params.id,
					headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
				}).then(response => {
					console.log(response)
					window.location.href = '/cleanings'
				})
			}
		}
	}
}
</script>

<style>

</style>
