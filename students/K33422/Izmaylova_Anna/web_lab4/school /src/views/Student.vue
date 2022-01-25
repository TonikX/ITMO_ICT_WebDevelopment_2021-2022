<template>
	<div class="container">
		<h1 class="mb-3">Студенты</h1>
		<div class="row">
			<div class="col-6">
				<div v-for="item in items" :key="item.id">
					<h3>Имя: {{item.first_name}} {{item.last_name}}</h3>
					<p>Пол: {{item.gender}}</p>
					<button @click="edit_item_btn(item.id, item.first_name, item.last_name, item.gender)" class="btn btn-primary">Редактировать</button>
					<button @click="delete_item_btn(item.id)" class="btn btn-danger ml-3">Удалить</button>
					<hr>
				</div>
			</div>

			<div class="col-6">
				<b-form class="w-75 mx-auto" method='post'>

					<h2 v-if="edit_id === -1">Добавить</h2>
					<div class="d-flex align-items-center" v-else>
						<h2 >Редактировать </h2> <a class="ml-5" @click="edit_item_btn(-1, '', '', '')">Добавить</a>
					</div>

					<b-form-group
						label="Имя"
						label-for="first_name"
					>
						<b-form-input
							name="first_name"
							type="text"
							v-model="first_name"
						/>
					</b-form-group>

					<b-form-group
						label="Фамилия"
						label-for="last_name"
					>
						<b-form-input
							name="last_name"
							type="text"
							v-model="last_name"
						/>
					</b-form-group>

					<b-form-group
						label="Пол"
						label-for="gender"
					>
							<b-form-select name='gender' v-model="gender" :options="['male', 'female']"></b-form-select>
					</b-form-group>

					<b-button @click="save()" type="button" variant="success">Сохранить</b-button>
				</b-form>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'Student',
	data () {
		return {
			items: [],
			id: '',
			fio: '',
			gender: '',
			first_name: '',
			last_name: '',
			edit_id: -1,
			section: 'students'
		}
	},
	mounted () {
		this.load_items()
	},
	methods: {
		load_items () {
			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/' + this.section + '/list/',
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then((response) => {
				this.items = response.data
				console.log(this.items)
			})
		},
		save () {
			let method
			let url
			if (this.edit_id === -1) {
				method = 'post'
				url = 'http://127.0.0.1:8000/' + this.section + '/create/'
			} else {
				method = 'put'
				url = 'http://127.0.0.1:8000/' + this.section + '/update/' + this.edit_id + '/'
			}

			axios({
				method: method,
				url: url,
				responseType: 'json',
				data: {
					first_name: this.first_name,
					last_name: this.last_name,
					gender: this.gender
				},
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				console.log(response)
				this.load_items()
				this.edit_id = -1
				this.first_name	= ''
				this.last_name = ''
				this.gender = ''
			}).catch(error => {
				console.log(error.response)
			})
		},
		edit_item_btn (id, firstName, lastName, gender) {
			this.edit_id = id
			this.first_name	= firstName
			this.last_name = lastName
			this.gender = gender
		},
		delete_item_btn (id) {
			if (confirm('Удалить?')) {
				axios({
					method: 'delete',
					url: 'http://127.0.0.1:8000/' + this.section + '/delete/' + id,
					headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
				}).then(response => {
					console.log(response)
					this.load_items()
				})
			}
		}
	}
}
</script>

<style scoped>

</style>
