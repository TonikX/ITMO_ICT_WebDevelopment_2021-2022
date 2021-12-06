<template>
	<div>
		<div class="container">
			<h2 class="text-center">Администратор</h2>
		</div>
		<div class="container">
			<form class="d-flex">
				<input v-model="query_name" class="form-control me-2" type="search" placeholder="Поиск пользователей" aria-label="Поиск пользователей">
				<button @click="search()" class="btn btn-outline-success" type="button">Найти</button>
			</form>
			<br>
			<client-row
			v-for="item in items"
			:key="item.id"
			:id="item.id"
			:city="item.city"
			:pasport="item.pasport"
			:full_name="item.full_name"
			/>
		</div>
	</div>
</template>

<script>
import axios from 'axios'
import ClientRow from './Client/Client-row.vue'

export default {
	components: { ClientRow },
	name: 'AdminPanel',
	data () {
		return {
			query_name: '',
			items: []
		}
	},
	methods: {
		search () {
			axios({
				method: 'get',
				url: 'http://localhost:8000/clients/?search=' + this.query_name,
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				console.log(response)
				this.items = response.data
			})
		}
	}
}

</script>
