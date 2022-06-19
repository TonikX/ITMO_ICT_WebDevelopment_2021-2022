<template>
	<div class="container">
		<div class="mb-3">
			<button @click="tab=1" class="btn btn-primary mr-2">Администраторы</button>
			<button @click="tab=2" class="btn btn-primary">Уборщики</button>
		</div>
		<div v-if="tab===1" class="">
			<b-form class="w-50 mx-auto" method='post'>
				<h2>Добавить администратора</h2>
				<b-form-group
					label="Login"
					label-for="username"
				>
					<b-form-input
						name="username"
						type="text"
						v-model="username"
						required
					/>
				</b-form-group>

				<b-form-group
					label="ФИО"
					label-for="full_name"
				>
					<b-form-input
						name="full_name"
						type="text"
						v-model="full_name"
						required
					/>
				</b-form-group>

				<b-form-group
					label="password"
					label-for="password"
				>
					<b-form-input
						name="password"
						type="password"
						v-model="password"
						required
					/>
				</b-form-group>

				<b-form-group
					label="phone"
					label-for="phone"
				>
					<b-form-input
						name="phone"
						type="text"
						v-model="phone"
						required
					/>
				</b-form-group>

				<button @click="create_admin()" type="button" class="btn btn-success">Создать</button>
			</b-form>
			<hr>
			<h2>Существующие администраторы:</h2>
			<hr>
			<div v-for="admin in admins" :key="admin.id">
				<h3>{{admin.full_name}}</h3>
				<p>Телефон: {{admin.phone}}</p>
				<!-- <button type="button" class="btn btn-primary">Редактировать</button> -->
				<button @click="delete_admin(admin.id)" type="button" class="btn btn-danger">Удалить</button>
				<hr>
			</div>
		</div>

		<div v-if="tab===2" class="">
			<b-form class="w-50 mx-auto" method='post'>
				<h2>Добавить уборщика</h2>

				<b-form-group
					label="ФИО"
					label-for="full_name"
				>
					<b-form-input
						name="full_name"
						type="text"
						v-model="full_name"
						required
					/>
				</b-form-group>

				<b-form-group
					label="phone"
					label-for="phone"
				>
					<b-form-input
						name="phone"
						type="text"
						v-model="phone"
						required
					/>
				</b-form-group>

				<b-form-group
					label="contract number"
					label-for="contract_number"
				>
					<b-form-input
						name="contract_number"
						type="text"
						v-model="contract_number"
						required
					/>
				</b-form-group>

				<button @click="create_cleaner()" type="button" class="btn btn-success">Создать</button>
			</b-form>
			<hr>
			<h2>Существующие уборщики:</h2>
			<hr>
			<div v-for="cleaner in cleaners" :key="cleaner.id">
				<h3>{{cleaner.full_name}}</h3>
				<p>Телефон: {{cleaner.phone}}</p>
				<button @click="delete_cleaner(cleaner.id)" type="button" class="btn btn-danger">Удалить</button>
				<hr>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios'
export default {
	name: 'Superuser',
	data () {
		return {
			admins: [],
			cleaners: [],
			username: '',
			full_name: '',
			password: '',
			phone: '',
			contract_number: '',
			tab: 1
		}
	},
	created () {
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/admins/',
			responseType: 'json',
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then(response => {
			this.admins = response.data
		})

		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/cleaners/',
			responseType: 'json',
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then(response => {
			this.cleaners = response.data
		})
	},
	methods: {
		delete_admin (id) {
			axios({
				method: 'delete',
				url: 'http://127.0.0.1:8000/admins/' + id + '/',
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				document.location.reload()
			})
		},
		delete_cleaner (id) {
			axios({
				method: 'delete',
				url: 'http://127.0.0.1:8000/cleaner/' + id + '/',
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				document.location.reload()
			})
		},
		create_admin () {
			axios({
				method: 'post',
				url: 'http://127.0.0.1:8000/admins/',
				responseType: 'json',
				data: {
					username: this.username,
					password: this.password,
					full_name: this.full_name,
					phone: this.phone
				},
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				document.location.reload()
			}).catch(err => {
				console.log(err.response)
			})
		},
		create_cleaner () {
			axios({
				method: 'post',
				url: 'http://127.0.0.1:8000/cleaners/',
				responseType: 'json',
				data: {
					contract_number: this.contract_number,
					full_name: this.full_name,
					phone: this.phone
				},
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				document.location.reload()
			}).catch(err => {
				console.log(err.response)
			})
		}
	}
}
</script>

<style>

</style>
