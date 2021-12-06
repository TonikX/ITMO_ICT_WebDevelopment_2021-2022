<template>
	<div>
		<h3>id комнаты: {{room}}</h3>
		<p>id клиента: {{client}}</p>
		<p>Дата заселения: {{in_date}}</p>
		<p>Дата выселения: {{out_date}}</p>
		<a :href="'/inhabitations/' + id" class="btn btn-primary">Подробнее</a>
		<hr>
	</div>
</template>

<script>
export default {
	name: 'InhabitationRow',
	props: ['id', 'client', 'room', 'in_date', 'out_date']
}
</script>

<style>

</style>
