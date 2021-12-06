<template>
	<div>
		<h3>Уборщик: {{cleaner_name}}</h3>
		<p>Этаж: {{item.floor}}</p>
		<p>Дата уборки: {{item.cost_of_living}}</p>
	</div>
</template>

<script>
import axios from 'axios'
export default {
	name: 'CleaningData',
	props: ['item'],
	data () {
		return {
			cleaner_name: ''
		}
	},
	mounted () {
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/cleanings/' + this.item.id + '/',
			responseType: 'json',
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then(response => {
			this.cleaner_name = response.data.full_name
		})
	}
}
</script>

<style>

</style>
