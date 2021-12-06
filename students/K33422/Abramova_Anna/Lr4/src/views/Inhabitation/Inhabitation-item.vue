<template>
	<div class="container">
		<h1>Комната: {{item.room}}</h1>
		<p>Клиент: {{item.client}}</p>
		<p>Дата заселения: {{item.in_date}}</p>
		<p>Дата выселения: {{item.out_date}}</p>

		<a :href="'/inhabitation/update/' + this.$route.params.id" class="btn btn-success">Редактировать</a>
		<button @click="delete_item()" class="btn btn-danger">Удалить</button>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'InhabitationItem',
	data () {
		return {
			item: []
		}
	},
	props: ['id'],
	created () {
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/inhabitations/' + this.$route.params.id,
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then((response) => {
			this.item = response.data
		})
	},
	methods: {
		delete_item () {
			if (confirm('Удалить?')) {
				axios({
					method: 'delete',
					url: 'http://127.0.0.1:8000/inhabitations/' + this.$route.params.id,
					headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
				}).then(response => {
					console.log(response)
					window.location.href = '/inhabitations'
				})
			}
		}
	}
}
</script>

<style>

</style>
