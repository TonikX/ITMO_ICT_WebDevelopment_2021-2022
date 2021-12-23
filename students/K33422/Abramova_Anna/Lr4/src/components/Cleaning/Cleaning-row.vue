<template>
	<div>
		<h3>Уборщик: {{cleaner}}</h3>
		<p>Этаж: {{cleaning_floor}}</p>
		<p>Дата уборки: {{cleaning_day}}</p>
		<a :href="'/cleanings/' + id" class="btn btn-primary">Подробнее</a>
		<hr>
	</div>
</template>

<script>
export default {
	name: 'CleaningRow',
	props: ['id', 'cleaner', 'cleaning_floor', 'cleaning_day']
}
</script>

<style>

</style>
