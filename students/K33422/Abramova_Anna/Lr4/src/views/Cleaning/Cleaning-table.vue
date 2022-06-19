<template>
	<div class="container">
		<h3>Расписание уборки</h3>
		<hr>
		<cleaning-row
			v-for="item in items"
			:key="item.id"
			:id="item.id"
			:cleaner="item.cleaner"
			:cleaning_floor="item.cleaning_floor"
			:cleaning_day="item.cleaning_day"
		/>
		<a href="/cleaning/create" class="btn btn-success">Добавить</a>
	</div>
</template>

<script>
import axios from 'axios'
import CleaningRow from '../../components/Cleaning/Cleaning-row'

export default {
	components: { CleaningRow },
	name: 'CleaningTable',
	data () {
		return {
			items: []
		}
	},
	mounted () {
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/cleanings/',
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
