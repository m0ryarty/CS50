import { Box, Typography } from '@mui/material'
import { useState } from 'react'
import { useNavigate } from 'react-router'

const Splash = () => {
	const navigate = useNavigate()
	const [splash, setSplash] = useState(true)

	setTimeout(() => {
		navigate('/home', { replace: true })
		setSplash(false)
	}, 3000)

	return (
		splash && (
			<Box
				sx={{
					display: 'flex',
					justifyContent: 'center',
					alignItems: 'center',
					height: '100vh',
					border: '1px',
				}}
			>
				<Box
					sx={{
						display: 'flex',
						flexDirection: 'column',
						justifyContent: 'center',
						alignItems: 'center',
					}}
				>
					<Typography sx={{ fontSize: 50 }}>Welcome to</Typography>
					<Typography sx={{ fontSize: 200 }}>Archive</Typography>
				</Box>
			</Box>
		)
	)
}

export default Splash
