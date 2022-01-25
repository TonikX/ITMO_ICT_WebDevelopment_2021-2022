<template>
	<div class="container">
		<h1 class="mb-3">Предметы</h1>
		<div class="row">
			<div class="col-6">
				<div v-for="item in items" :key="item.id">
					<h3>{{students.find(i => i.value === item.student_id).text}}, предмет {{subjects.find(i => i.value === item.subject_id).text}}</h3>
					<p>Оценка: {{item.grade}}</p>
					<p>Четверть: {{item.quarter}}</p>
					<button @click="edit_item_btn(item.id, item.student_id, item.subject_id, item.grade, item.quarter)" class="btn btn-primary">Редактировать</button>
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
						label="Студент"
						label-for="student_id"
					>
						<b-form-select name='student_id' v-model="student_id" :options="students"></b-form-select>
					</b-form-group>

					<b-form-group
						label="Предмет"
						label-for="subject_id"
					>
						<b-form-select name='subject_id' v-model="subject_id" :options="subjects"></b-form-select>
					</b-form-group>

					<b-form-group
						label="Оценка"
						label-for="grade"
					>
							<b-form-select name='grade' v-model="grade" :options="['1', '2', '3', '4', '5']"></b-form-select>
					</b-form-group>

					<b-form-group
						label="Четверть"
						label-for="quarter"
					>
							<b-form-select name='quarter' v-model="quarter" :options="['1', '2', '3', '4']"></b-form-select>
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
			student_id: '',
			subject_id: '',
			grade: '',
			quarter: '',
			students: [],
			subjects: [],
			edit_id: -1,
			section: 'grades'
		}
	},
	mounted () {
		this.load_items()
	},
	methods: {
		load_items () {
			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/students/list/',
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then((response) => {
				this.students = []
				response.data.forEach(element => {
					this.students.push({ value: element.id, text: element.first_name + ' ' + element.last_name })
				})
			})

			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/subjects/',
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then((response) => {
				this.subjects = []
				response.data.forEach(element => {
					this.subjects.push({ value: element.id, text: element.subject })
				})
			})

			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/' + this.section + '/list/',
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then((response) => {
				this.items = response.data.Grades
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
					student_id: this.student_id,
					subject_id: this.subject_id,
					grade: this.grade,
					quarter: this.quarter
				},
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				console.log(response)
				this.load_items()
				this.edit_id = -1
				this.student_id	= ''
				this.subject_id = ''
				this.grade = ''
				this.quarter = ''
			}).catch(error => {
				console.log(error.response)
			})
		},
		edit_item_btn (id, studentId, subjectId, grade, quarter) {
			this.edit_id = id
			this.student_id	= studentId
			this.subject_id = subjectId
			this.grade = grade
			this.quarter = quarter
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
