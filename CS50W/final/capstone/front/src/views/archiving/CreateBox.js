import { useState } from 'react'
import { useGlobalState, useDispatch } from '../../utils/globalState'
import useAxios from '../../utils/useAxios'
import {
	Button,
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
const CreateBox = () => {
	const [newBox, setNewBox] = useState('')
	const [open, setOpen] = useState(false)

	const { shelves } = useGlobalState()
	const dispatch = useDispatch()

	const api = useAxios()

	const handleChange = (event) => {
		setNewBox(event.target.value)
	}

	const handleClickOpen = () => {
		setOpen(true)
	}

	const handleClose = () => {
		setOpen(false)
	}
	const fetchPostData = async (boxJson) => {
		try {
			const response = await api.post('/boxes', boxJson, {
				headers: {
					'Content-Type': 'application/json',
				},
			})

			await dispatch({
				type: 'SET_BOXES',
				payload: response.data.response.boxes,
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
		const boxJson = Object.fromEntries(formData.entries())
		fetchPostData(boxJson)
		setNewBox('')
		handleClose()
	}

	return (
		<>
			<Button variant='standard' onClick={handleClickOpen}>
				Create New Box
			</Button>
			<Dialog
				open={open}
				onClose={handleClose}
				slotProps={{
					paper: {
						component: 'form',
						onSubmit: (e) => handleSubmit(e),
					},
				}}
			>
				<DialogTitle>Create Box</DialogTitle>
				<DialogContent>
					<FormControl sx={{ marginTop: 2 }} fullWidth>
						<InputLabel
							sx={{ backgroundColor: '#eceff1' }}
							id='shelf-select-label'
						>
							Shelf
						</InputLabel>
						<Select
							labelId='shelf-select-label'
							id='shelf-select-label'
							name='shelf'
							value={newBox}
							label='newBox'
							onChange={handleChange}
						>
							{shelves &&
								shelves.map(
									(item) =>
										item.boxes < item.capacity && (
											<MenuItem key={item.id} value={item.id}>
												Shelf {item.id}
											</MenuItem>
										)
								)}
						</Select>
					</FormControl>
					<TextField name='Obs' label='Obs' variant='standard' />
				</DialogContent>
				<DialogActions>
					<Button onClick={handleClose}>Cancel</Button>
					<Button type='submit'>Create</Button>
				</DialogActions>
			</Dialog>
		</>
	)
}

export default CreateBox
