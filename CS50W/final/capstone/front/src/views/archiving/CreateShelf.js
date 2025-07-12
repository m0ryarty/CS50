import { useState } from 'react'
import { useGlobalState, useDispatch } from '../../utils/globalState'

import {
	Button,
	Box,
	DialogActions,
	Dialog,
	TextField,
	Select,
	FormControl,
	MenuItem,
	InputLabel,
	DialogTitle,
	DialogContent,
} from '@mui/material'
import useAxios from '../../utils/useAxios'

const CreateShelf = () => {
	const [newShelf, setNewShelf] = useState('')
	const [open, setOpen] = useState(false)
	const api = useAxios()
	const dispatch = useDispatch()
	const { archives } = useGlobalState()

	const handleChange = (event) => {
		setNewShelf(event.target.value)
	}

	const handleClickOpen = () => {
		setOpen(true)
	}

	const handleClose = () => {
		setOpen(false)
	}

	const fetchPostData = async (shelfJson) => {
		try {
			const response = await api.post('/shelves', shelfJson, {
				headers: {
					'Content-Type': 'application/json',
				},
			})

			await dispatch({
				type: 'SET_SHELVES',
				payload: response.data.response.shelves,
			})
			await dispatch({
				type: 'SET_SUMMARY',
				payload: response.data.response.summary,
			})
		} catch (error) {
			console.error(error)
		}
	}

	const handleSubmit = (event) => {
		event.preventDefault()
		const formData = new FormData(event.currentTarget)
		const shelfJson = Object.fromEntries(formData.entries())
		fetchPostData(shelfJson)
		setNewShelf('')
		handleClose()
	}

	return (
		<>
			<Button variant='standard' onClick={handleClickOpen}>
				Create New Shelf
			</Button>
			<Dialog
				open={open}
				onClose={handleClose}
				slotProps={{
					paper: {
						component: 'form',
						onSubmit: (e) => {
							handleSubmit(e)
						},
					},
				}}
			>
				<DialogTitle>Create Shelf</DialogTitle>
				<DialogContent>
					<Box sx={{ display: 'flex', gap: 3, marginBottom: 5 }}>
						<TextField name='type' label='Type' variant='standard' required />
						<TextField
							name='location'
							label='Location'
							variant='standard'
							required
						/>
						<TextField
							name='capacity'
							label='Capacity'
							variant='standard'
							required
						/>
					</Box>
					<FormControl sx={{ marginTop: 2 }} fullWidth>
						<InputLabel
							sx={{ backgroundColor: '#eceff1' }}
							id='demo-simple-select-label'
						>
							Archive *
						</InputLabel>
						<Select
							labelId='demo-simple-select-label'
							id='demo-simple-select'
							name='archive'
							value={newShelf}
							label='newShelf'
							onChange={handleChange}
							required
						>
							{archives &&
								archives.map((item) => (
									<MenuItem key={item.id} value={item.id}>
										{item.name}
									</MenuItem>
								))}
						</Select>
					</FormControl>
				</DialogContent>
				<DialogActions>
					<Button onClick={handleClose}>Cancel</Button>
					<Button type='submit'>Create</Button>
				</DialogActions>
			</Dialog>
		</>
	)
}

export default CreateShelf
