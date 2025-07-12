import { useDispatch } from '../../utils/globalState'
import useAxios from '../../utils/useAxios'

import Box from '@mui/material/Box'
import Card from '@mui/material/Card'
import CardContent from '@mui/material/CardContent'
import Button from '@mui/material/Button'
import TextField from '@mui/material/TextField'

const CreateArchives = () => {
	const dispatch = useDispatch()
	const api = useAxios()

	const fetchPostData = async (archiveJson) => {
		try {
			const response = await api.post('/create_archive', archiveJson, {
				headers: {
					'Content-Type': 'application/json',
				},
			})
			const data = await response.data
			dispatch({ type: 'SET_ARCHIVES', payload: data })
		} catch (error) {
			console.error(error)
		}
	}

	const handleSubmit = (event) => {
		event.preventDefault()
		const formData = new FormData(event.currentTarget)
		const archiveJson = Object.fromEntries(formData.entries())
		fetchPostData(archiveJson)
		dispatch({ type: 'CREATE_ARCHIVE', payload: false })
	}

	return (
		<Card>
			<CardContent>
				<form onSubmit={handleSubmit}>
					<Box
						sx={{
							display: 'flex',
							flexDirection: 'column',
							gap: 1,
							marginBottom: 2,
						}}
					>
						<TextField label='Name' name='name' required fullWidth />

						<TextField label='Address' name='address' required fullWidth />
					</Box>
					<Box sx={{ display: 'flex', flexDirection: 'row' }}>
						<Button type='submit' variant='standard' fullWidth>
							New Archive
						</Button>
						<Button
							onClick={() =>
								dispatch({ type: 'CREATE_ARCHIVE', payload: false })
							}
							variant='standard'
							fullWidth
						>
							Cancel
						</Button>
					</Box>
				</form>
			</CardContent>{' '}
		</Card>
	)
}

export default CreateArchives
