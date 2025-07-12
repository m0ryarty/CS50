import App from '../App'

import { createBrowserRouter } from 'react-router'
import Homepage from '../views/Homepage'
import Splash from '../views/Splash'
import Archiving from '../views/archiving/Archiving'
import Archives from '../views/archives/Archives'
import Shelves from '../views/shelves/Shelves'
import Boxes from '../views/boxes/Boxes'
import Analysis from '../views/analytics/Analysis'
import Elimination from '../views/analytics/Elimination'
import Integrations from '../views/analytics/Integrations'
import Reports from '../views/analytics/Reports'
import Layout from './dashboard'

import SignInPage from '../views/SignIn'

const router = createBrowserRouter([
	{
		Component: App,
		children: [
			{
				path: '/',
				Component: Layout,
				children: [
					{
						path: '/',
						Component: Splash,
					},
					{
						path: '/home',
						Component: Homepage,
					},
					{
						path: '/archiving',
						Component: Archiving,
					},
					{
						path: '/archives',
						Component: Archives,
					},
					{
						path: '/shelves',
						Component: Shelves,
					},
					{
						path: '/boxes',
						Component: Boxes,
					},
					{
						path: '/integrations',
						Component: Integrations,
					},
					{
						path: '/reports',
						Component: Reports,
						children: [
							{ path: '/reports/analysis', Component: Analysis },
							{ path: '/reports/elimination', Component: Elimination },
						],
					},
				],
			},
			{
				path: '/sign-in',
				Component: SignInPage,
			},
		],
	},
])

export default router
