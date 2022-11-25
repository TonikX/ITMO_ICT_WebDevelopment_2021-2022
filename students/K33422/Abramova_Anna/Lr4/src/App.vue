<template>
	<div id="app">
		<nav v-if="is_auth" class="navbar navbar-expand-lg navbar-light bg-light">
			<div class="container d-flex align-items-center">
				<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
					aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
					<span class="navbar-toggler-icon"></span>
				</button>
				<div class="collapse navbar-collapse" id="navbarSupportedContent">
					<ul class="navbar-nav me-auto mb-2 mb-lg-0  d-flex align-items-center">
						<li class="nav-item">
							<a class="nav-link active" aria-current="page" href="/">Главная</a>
						</li>
						<li class="nav-item">
							<a class="nav-link" href="/clients">Клиенты</a>
						</li>
						<li class="nav-item">
							<a class="nav-link" href="/rooms">Комнаты</a>
						</li>
						<li class="nav-item">
							<a class="nav-link" href="/inhabitations">Проживание</a>
						</li>
						<li class="nav-item">
							<a class="nav-link" href="/cleanings">Расписание уборки</a>
						</li>
						<li class="nav-item">
							<a @click="exit()" class="nav-link">Выйти</a>
						</li>
					</ul>
				</div>
			</div>
		</nav>
		<main class="py-3">
			<div>
				<router-view />
			</div>
		</main>
	</div>
</template>

<script>
import Vue from 'vue'
import {
	BootstrapVue,
	IconsPlugin
} from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

export default {
	name: 'App',

	data: () => ({
		is_auth: false
	}),
	components: {
		//
	},
	methods: {
		exit () {
			sessionStorage.removeItem('auth_token')
			window.location.href = '/'
		}
	},
	mounted () {
		this.is_auth = Boolean(sessionStorage.getItem('auth_token') !== null)
	}
}

</script>

<style>
	#app {
		font-family: Avenir, Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		color: #2c3e50;
	}

</style>
