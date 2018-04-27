import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'


const routerOptions = [
	{ path: '/', component: 'Landing' },
	{ path: '/signin', component: 'Signin' },
	{ path: '/signup', component: 'Signup' },
	{ path: '/home', component: 'Home'}
]

const routes = routerOptions.map(route => {
	return {
		...route,
		component: () => import(`@/components/${route.component}.vue`)
	}
})

Vue.use(Router)

export default new Router({
	mode: 'history',
	routes
})

// export default new Router({
//   routes: [
//     {
//       path: '/',
//       name: 'HelloWorld',
//       component: HelloWorld
//     }
//   ]
// })
