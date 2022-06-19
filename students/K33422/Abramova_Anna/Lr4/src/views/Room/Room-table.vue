<template>
	<div class="container">
		<h3>Номера</h3>
		<hr>
		<room-row
			v-for="item in items"
			:key="item.id"
			:id="item.id"
			:number="item.number"
			:floor="item.floor"
			:cost_of_living="item.cost_of_living"
			:room_type="item.room_type"
		/>
		<a href="/room/create" class="btn btn-success">Добавить</a>
	</div>
</template>

<script>
import axios from 'axios'
import RoomRow from '../../components/Room/Room-row'

export default {
	components: { RoomRow },
	name: 'RoomTable',
	data () {
		return {
			items: []
		}
	},
	mounted () {
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/rooms/',
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
