<template>
	<div class="container">
		<h1 class="mb-3">Предметы</h1>
		<div class="row">
			<div class="col-6">
				<div v-for="item in items" :key="item.id">
					<h3>Предмет: {{item.subject}}</h3>
					<p>Учитель: {{teachers.find(i => i.value === item.teacher_id).text}}</p>
					<p>Статус: {{item.status}}</p>
					<button @click="edit_item_btn(item.id, item.subject, item.teacher_id, item.status)" class="btn btn-primary">Редактировать</button>
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
						label="Название предмета"
						label-for="subject"
					>
						<b-form-input
							name="subject"
							type="text"
							v-model="subject"
						/>
					</b-form-group>

					<b-form-group
						label="Учитель"
						label-for="teacher_id"
					>
						<b-form-select name='teacher_id' v-model="teacher_id" :options="teachers"></b-form-select>
					</b-form-group>

					<b-form-group
						label="Статус"
						label-for="status"
					>
							<b-form-select name='status' v-model="status" :options="['basic', 'profile']"></b-form-select>
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
			subject: '',
			teacher_id: '',
			teachers: [],
			edit_id: -1,
			section: 'subjects'
		}
	},
	mounted () {
		this.load_items()
	},
	methods: {
		load_items () {
			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/' + this.section + '/',
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then((response) => {
				this.items = response.data
				console.log(this.items)
			})

			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/teachers/',
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then((response) => {
				this.breeds = []
				response.data.forEach(element => {
					this.teachers.push({ value: element.id, text: element.name })
				})
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
					subject: this.subject,
					teacher_id: this.teacher_id,
					status: this.status
				},
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				console.log(response)
				this.load_items()
				this.edit_id = -1
				this.subject	= ''
				this.teacher_id = ''
				this.status = ''
			}).catch(error => {
				console.log(error.response)
			})
		},
		edit_item_btn (id, subject, teacherId, status) {
			this.edit_id = id
			this.subject	= subject
			this.teacher_id = teacherId
			this.status = status
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
