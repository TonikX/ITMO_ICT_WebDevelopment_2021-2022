<template>
	<div class="container">
		<h1 class="mb-3">Предметы</h1>
		<div class="row">
			<div class="col-6">
				<div v-for="item in items" :key="item.id">
					<h3>{{teachers.find(i => i.value === item.teacher_id).text}}, предмет {{subjects.find(i => i.value === item.subject_id).text}}</h3>
					<p>Класс: {{classes.find(i => i.value === item.class_id).text}}</p>
					<p>День недели: {{item.day_of_week}}</p>
					<p>Урок: {{item.lesson}}</p>
					<button @click="edit_item_btn(item.id, item.teacher_id, item.subject_id, item.class_id, item.room_id, item.day_of_week, item.lesson)" class="btn btn-primary">Редактировать</button>
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
						label="Учитель"
						label-for="teacher_id"
					>
						<b-form-select name='teacher_id' v-model="teacher_id" :options="teachers"></b-form-select>
					</b-form-group>

					<b-form-group
						label="Предмет"
						label-for="subject_id"
					>
						<b-form-select name='subject_id' v-model="subject_id" :options="subjects"></b-form-select>
					</b-form-group>

					<b-form-group
						label="Кабинет"
						label-for="room_id"
					>
						<b-form-select name='room_id' v-model="room_id" :options="rooms"></b-form-select>
					</b-form-group>

					<b-form-group
						label="Класс"
						label-for="class_id"
					>
						<b-form-select name='class_id' v-model="class_id" :options="classes"></b-form-select>
					</b-form-group>

					<b-form-group
						label="День недели"
						label-for="day_of_week"
					>
							<b-form-select name='day_of_week' v-model="day_of_week" :options="['1', '2', '3', '4', '5', '6']"></b-form-select>
					</b-form-group>

					<b-form-group
						label="Урок"
						label-for="lesson"
					>
							<b-form-select name='lesson' v-model="lesson" :options="['1', '2', '3', '4', '5', '6']"></b-form-select>
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
			teacher_id: '',
			subject_id: '',
			room_id: '',
			class_id: '',
			day_of_week: '',
			lesson: '',
			teachers: [],
			subjects: [],
			rooms: [],
			classes: [],
			edit_id: -1,
			section: 'timetable'
		}
	},
	mounted () {
		this.load_items()
	},
	methods: {
		load_items () {
			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/teachers/list/',
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then((response) => {
				this.teachers = []
				response.data.forEach(element => {
					this.teachers.push({ value: element.id, text: element.first_name + ' ' + element.last_name })
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
				url: 'http://127.0.0.1:8000/classes/',
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then((response) => {
				this.classes = []
				response.data.forEach(element => {
					this.classes.push({ value: element.id, text: element.name })
				})
			})

			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/rooms/',
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then((response) => {
				this.rooms = []
				response.data.forEach(element => {
					this.rooms.push({ value: element.id, text: element.room })
				})
			})

			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/' + this.section + '/',
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then((response) => {
				this.items = response.data
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
					teacher_id: this.teacher_id,
					subject_id: this.subject_id,
					class_id: this.class_id,
					room_id: this.room_id,
					day_of_week: this.day_of_week,
					lesson: this.lesson
				},
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				console.log(response)
				this.load_items()
				this.edit_id = -1
				this.teacher_id	= ''
				this.subject_id = ''
				this.class_id	= ''
				this.room_id = ''
				this.day_of_week = ''
				this.lesson = ''
			}).catch(error => {
				console.log(error.response)
			})
		},
		edit_item_btn (id, teacherId, subjectId, classId, roomId, dayOfWeek, lesson) {
			this.edit_id = id
			this.teacher_id	= teacherId
			this.subject_id = subjectId
			this.class_id	= classId
			this.room_id = roomId
			this.day_of_week = dayOfWeek
			this.lesson = lesson
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
