<template>
	<div>
		<loading v-if="loading" />
		<div v-if="isAuthenticated">
			<feed-item v-for="(feed, index) in fakeFeed" :key="index" :feed="feed" />
		</div>
		<div v-if="!isAuthenticated && authStatus !== 'loading'">
			<h1>Welcome to BOGEBAWK !</h1>
			<p>When meating new boge fiends is hardar than evar, Bogebawk closes the gap between all paws in the world</p>
			<login />
		</div>
	</div>
</template>

<style>
  .home {
    display: flex;
    align-items: center;
    flex-direction: column;
  }
</style>

<script>
	import fakeFeed from './fakeFeed'
	import FeedItem from './feedItem.vue'
	import { mapGetters } from 'vuex'
	import Login from 'components/login'

	export default {
		components: {
			Login,
			FeedItem
		},
		name: 'home',
		computed: {
			...mapGetters(['isAuthenticated', 'authStatus']),
			loading: function () {
				return this.authStatus === 'loading' && !this.isAuthenticated
			}
		},
		data () {
			return ({ fakeFeed })
		},
	}
</script>