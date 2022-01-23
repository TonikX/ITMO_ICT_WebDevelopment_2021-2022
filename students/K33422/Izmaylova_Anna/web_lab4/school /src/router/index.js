import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

import Student from '../views/Student.vue'
import Teacher from '../views/Teacher.vue'
import Grades from '../views/Grades'
import Timetable from '../views/Timetable'

Vue.use(VueRouter)

const routes = [
	{
		path: '/',
		name: 'Home',
		component: Home
	},

	{
		path: '/teachers',
		name: 'Teacher',
		component: Teacher
	},
	{
		path: '/students',
		name: 'Students',
		component: Student
	},
	{
		path: '/grades',
		name: 'Grades',
		component: Grades
	},
	{
		path: '/timetable',
		name: 'Timetable',
		component: Timetable
	}
]

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes
})

export default router
