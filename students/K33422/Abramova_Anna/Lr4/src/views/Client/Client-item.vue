<template>
	<div class="container">
		<h1>{{item.full_name}}</h1>
		<p>Паспорт: {{item.pasport}}</p>
		<p>Город: {{item.city}}</p>
		<ul v-if="room_count">
			Номера:
			<li v-for="room in item.rooms" :key="room">{{room}}</li>
		</ul>
		<div v-else >
			Нет снятых номеров
		</div>
		<a :href="'/client/update/' + this.$route.params.id" class="btn btn-success">Редактировать</a>
		<button @click="delete_item()" class="btn btn-danger">Удалить</button>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'ClientItem',
	data () {
		return {
			item: [],
			room_count: 0
		}
	},
	props: ['id'],
	created () {
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/clients/' + this.$route.params.id,
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then((response) => {
			this.item = response.data
			console.log(response)
			this.room_count = response.data.rooms.length
		})
	},
	methods: {
		delete_item () {
			if (confirm('Удалить?')) {
				axios({
					method: 'delete',
					url: 'http://127.0.0.1:8000/clients/' + this.$route.params.id,
					headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
				}).then(response => {
					console.log(response)
					window.location.href = '/clients'
				})
			}
		}
	}
}
</script>

<style>

</style>
