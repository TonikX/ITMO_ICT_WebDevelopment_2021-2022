import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Superadmin from '../views/Superadmin.vue'

import ClientTable from '../views/Client/Client-table.vue'
import ClientItem from '../views/Client/Client-item.vue'
import ClientUpdate from '../views/Client/Client-update.vue'
import ClientCreate from '../views/Client/Client-create.vue'

import RoomTable from '../views/Room/Room-table.vue'
import RoomItem from '../views/Room/Room-item.vue'
import RoomUpdate from '../views/Room/Room-update.vue'
import RoomCreate from '../views/Room/Room-create.vue'

import InhabitationTable from '../views/Inhabitation/Inhabitation-table.vue'
import InhabitationItem from '../views/Inhabitation/Inhabitation-item.vue'
import InhabitationUpdate from '../views/Inhabitation/Inhabitation-update.vue'
import InhabitationCreate from '../views/Inhabitation/Inhabitation-create.vue'

import CleaningTable from '../views/Cleaning/Cleaning-table.vue'
import CleaningItem from '../views/Cleaning/Cleaning-item.vue'
import CleaningUpdate from '../views/Cleaning/Cleaning-update.vue'
import CleaningCreate from '../views/Cleaning/Cleaning-create.vue'

Vue.use(VueRouter)

const routes = [
	{
		path: '/',
		name: 'Home',
		component: Home
	},

	{
		path: '/superadmin',
		name: 'Superadmin',
		component: Superadmin
	},

	{
		path: '/clients',
		name: 'ClientTable',
		component: ClientTable
	},
	{
		path: '/clients/:id',
		name: 'ClientItem',
		component: ClientItem
	},
	{
		path: '/client/update/:id',
		name: 'ClientUpdate',
		component: ClientUpdate
	},
	{
		path: '/client/create',
		name: 'ClientCreate',
		component: ClientCreate
	},

	{
		path: '/rooms',
		name: 'RoomTable',
		component: RoomTable
	},
	{
		path: '/rooms/:id',
		name: 'RoomItem',
		component: RoomItem
	},
	{
		path: '/room/update/:id',
		name: 'RoomUpdate',
		component: RoomUpdate
	},
	{
		path: '/room/create',
		name: 'RoomCreate',
		component: RoomCreate
	},

	{
		path: '/inhabitations',
		name: 'InhabitationTable',
		component: InhabitationTable
	},
	{
		path: '/inhabitations/:id',
		name: 'InhabitationItem',
		component: InhabitationItem
	},
	{
		path: '/inhabitation/update/:id',
		name: 'InhabitationUpdate',
		component: InhabitationUpdate
	},
	{
		path: '/inhabitation/create',
		name: 'InhabitationCreate',
		component: InhabitationCreate
	},

	{
		path: '/Cleanings',
		name: 'CleaningTable',
		component: CleaningTable
	},
	{
		path: '/Cleanings/:id',
		name: 'CleaningItem',
		component: CleaningItem
	},
	{
		path: '/Cleaning/update/:id',
		name: 'CleaningUpdate',
		component: CleaningUpdate
	},
	{
		path: '/Cleaning/create',
		name: 'CleaningCreate',
		component: CleaningCreate
	}
]

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes
})

export default router
