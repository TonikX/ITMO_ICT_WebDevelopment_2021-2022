<template>
	<div>
		<h3>Клиент: {{client.full_name}}</h3>
		<p>Паспорт: {{client.pasport}}</p>
		<p>Город: {{client.city}}</p>
		<ul v-if="client.rooms">
			<li v-for="room in client.rooms" :key="room.id">{{room.id}}</li>
		</ul>
		<div v-else >
			Нет снятых номеров
		</div>
	</div>
</template>

<script>
export default {
	name: 'ClientData',
	props: ['client']
}
</script>

<style>

</style>
