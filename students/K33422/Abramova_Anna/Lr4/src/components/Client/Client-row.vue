<template>
	<div>
		<h3>{{full_name}}</h3>
		<p>Паспорт: {{pasport}}</p>
		<p>Город: {{city}}</p>
		<a :href="'/clients/' + id" class="btn btn-primary">Подробнее</a>
		<hr>
	</div>
</template>

<script>
export default {
	name: 'ClientRow',
	props: ['id', 'full_name', 'pasport', 'city']
}
</script>

<style>

</style>
