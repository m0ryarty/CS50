import { createContext, useState, useEffect } from 'react'
import { jwtDecode } from 'jwt-decode'

const AuthContext = createContext()

export default AuthContext

export const AuthProvider = ({ children }) => {
	const [authTokens, setAuthTokens] = useState(() =>
		localStorage.getItem('authTokens')
			? JSON.parse(localStorage.getItem('authTokens'))
			: null
	)

	const [user, setUser] = useState(() =>
		localStorage.getItem('authTokens')
			? jwtDecode(localStorage.getItem('authTokens'))
			: null
	)

	const [loading, setLoading] = useState(true)

	const loginUser = async (email, password) => {
		try {
			const response = await fetch('http://127.0.0.1:8000/token/', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({
					email,
					password,
				}),
			})
			const data = await response.json()
			if (response.status === 200) {
				setAuthTokens(data)
				setUser(jwtDecode(data.access))
				localStorage.setItem('authTokens', JSON.stringify(data))
			}

			return { status: response.status, data: data }
		} catch (e) {
			return e
		}
	}

	const logoutUser = () => {
		setAuthTokens(null)
		setUser(null)
		localStorage.removeItem('authTokens')
	}

	const contextData = {
		user,
		setUser,
		authTokens,
		setAuthTokens,
		loginUser,
		logoutUser,
	}

	useEffect(() => {
		if (authTokens) {
			setUser(jwtDecode(authTokens.access))
		}
		setLoading(false)
	}, [authTokens, loading])

	return (
		<AuthContext.Provider value={contextData}>
			{loading ? null : children}
		</AuthContext.Provider>
	)
}
