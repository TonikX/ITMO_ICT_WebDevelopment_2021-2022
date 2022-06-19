<template>
	<div>
		<h3>Комната: {{item.number}}</h3>
		<p>Этаж: {{item.floor}}</p>
		<p>Цена проживания: {{item.cost_of_living}}</p>
		<p>Тип комнаты: {{item.room_type}}</p>
	</div>
</template>

<script>
export default {
	name: 'RoomData',
	props: ['item']
}
</script>

<style>

</style>
