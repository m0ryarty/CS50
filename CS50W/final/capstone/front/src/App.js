import { useContext, useState, useEffect, useMemo } from 'react'

import { useNavigate } from 'react-router'
import { ReactRouterAppProvider } from '@toolpad/core/react-router'
import { Outlet } from 'react-router'
import { BRANDING, NAVIGATION, THEME } from './utils/layout'
import AuthContext from './context/AuthContext'

import useAxios from './utils/useAxios'
import { useDispatch } from './utils/globalState'

const App = () => {
	const { user, logoutUser } = useContext(AuthContext)

	const token = localStorage.getItem('authTokens')
	const [session, setSession] = useState(null)
	const navigate = useNavigate()

	const api = useAxios()
	const dispatch = useDispatch()

	useEffect(() => {
		const fetchData = async () => {
			try {
				const boxResponse = await api.get('/archiving')

				const data = boxResponse.data.response

				console.log(data)

				boxResponse.request.status === 200 &&
					dispatch({ type: 'LOADING', payload: false })

				dispatch({
					type: 'SET_BOXES',
					payload: data.boxes,
				})

				dispatch({
					type: 'SET_SHELVES',
					payload: data.shelves,
				})

				dispatch({
					type: 'SET_ARCHIVES',
					payload: data.archives,
				})

				dispatch({
					type: 'SET_BOX_VOLS',
					payload: data.box_volumes,
				})

				dispatch({
					type: 'SET_BOX_ALL_VOLS',
					payload: data.box_all_vols,
				})

				dispatch({
					type: 'SET_RECORD_VOLS',
					payload: data.record_volumes,
				})

				dispatch({
					type: 'SET_SUMMARY',
					payload: data.summary,
				})
				dispatch({
					type: 'SET_SITUATION',
					payload: data.situation,
				})
				dispatch({
					type: 'SET_SITUATIONS',
					payload: data.situations,
				})
			} catch (error) {
				console.log(error)
			}
		}
		fetchData()
	}, [])

	useEffect(() => {
		if (token) {
			setSession({
				user: {
					name: `${user.username}`,
					email: `${user.email}`,
					image:
						'https://2.bp.blogspot.com/-e1__gaQz8fw/Uobv-jn36aI/AAAAAAAAFLk/srSymnOIVog/s1600/Capybara-Animals-Pictures.jpg',
				},
			})
		} else {
			navigate('/sign-in', { replace: true })
			setSession(null)
			console.log('No token found, redirecting to sign-in...')
		}
	}, [token])

	const authentication = useMemo(() => {
		return {
			signIn: () => {
				setSession({
					user: {
						name: `${user.username}`,
						email: `${user.email}`,
						image:
							'https://images.freeimages.com/images/large-previews/440/araucaria-1249426.jpg',
					},
				})
			},
			signOut: () => {
				logoutUser()
				setSession(null)
				navigate('/sign-in', { replace: true })
			},
		}
	}, [])

	return (
		<ReactRouterAppProvider
			navigation={NAVIGATION}
			branding={BRANDING}
			session={session}
			authentication={authentication}
			theme={THEME}
		>
			<Outlet />
		</ReactRouterAppProvider>
	)
}

export default App
