<template>
	<div>
		<h3>Комната {{number}}</h3>
		<p>Этаж: {{floor}}</p>
		<p>Стоимость проживания: {{cost_of_living}}</p>
		<p>Тип номера: {{room_type}}</p>
		<a :href="'/rooms/' + id" class="btn btn-primary">Подробнее</a>
		<hr>
	</div>
</template>

<script>
export default {
	name: 'RoomRow',
	props: ['id', 'number', 'floor', 'cost_of_living', 'room_type']
}
</script>

<style>

</style>
