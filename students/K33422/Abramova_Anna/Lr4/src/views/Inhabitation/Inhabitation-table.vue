<template>
	<div class="container">
		<h3>Проживание</h3>
		<hr>
		<inhabitation-row
			v-for="item in items"
			:key="item.id"
			:id="item.id"
			:client="item.client"
			:room="item.room"
			:in_date="item.in_date"
			:out_date="item.out_date"
		/>
		<a href="/inhabitation/create" class="btn btn-success">Добавить</a>
	</div>
</template>

<script>
import axios from 'axios'
import InhabitationRow from '../../components/Inhabitation/Inhabitation-row'

export default {
	components: { InhabitationRow },
	name: 'InhabitationTable',
	data () {
		return {
			items: []
		}
	},
	mounted () {
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/inhabitations/',
			responseType: 'json',
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then((response) => {
			this.items = response.data
		})
	}
}
</script>

<style>

</style>
