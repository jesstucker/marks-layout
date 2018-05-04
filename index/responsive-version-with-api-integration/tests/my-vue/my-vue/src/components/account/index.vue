<template>
	<div>
		<div class="headline">
			<img src="x">
			<h1>Your doggieasdf profile</h1>
	</div>
	<p v-if="profile.name">
		<strong>Name:</strong>{{profile.title}} {{profile.name}}
	</p>
</div>
</template>

<script>
	import { mapState } from 'vuex'

	export default {
		name: 'account',
		computed: mapState({profile: state => state.user.profile})
	}
</script>