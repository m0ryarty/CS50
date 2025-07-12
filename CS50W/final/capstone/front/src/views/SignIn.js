'use client'
import * as React from 'react'
import { SignInPage } from '@toolpad/core/SignInPage'
import { useNavigate } from 'react-router'
import AuthContext from '../context/AuthContext'
import { useContext } from 'react'

const SignIn = () => {
	const { loginUser } = useContext(AuthContext)
	const navigate = useNavigate()
	return (
		<SignInPage
			providers={[{ id: 'credentials', name: 'Email, Password' }]}
			signIn={async (provider, formData) => {
				try {
					const email = formData.get('email')
					const password = formData.get('password')

					const data = await loginUser(email, password)

					if (data.status === 200) {
						navigate('/home', { replace: true })
					} else {
						throw new Error(data.data.detail)
					}
				} catch (error) {
					return {
						type: 'CredentialsSignin',
						error: error.message,
					}
				}
			}}
		/>
	)
}

export default SignIn
