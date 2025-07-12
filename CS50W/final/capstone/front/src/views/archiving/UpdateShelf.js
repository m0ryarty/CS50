import useAxios from '../../utils/useAxios'
import { useDispatch } from '../../utils/globalState'
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

const UpdateShelf = ({ row, open, setOpen }) => {
	const api = useAxios()
	const dispatch = useDispatch()

	const handleClose = () => {
		setOpen(false)
	}
	const fetchPostData = async (boxJson) => {
		try {
			const response = await api.put('/shelves', boxJson, {
				headers: {
					'Content-Type': 'application/json',
				},
			})

			dispatch({
				type: 'SET_SHELVES',
				payload: response.data.response.shelves,
			})
		} catch (error) {
			console.error(error)
		}
	}

	const handleSubmit = (event) => {
		event.preventDefault()
		const formData = new FormData(event.currentTarget)

		const rawObject = Object.fromEntries(formData.entries())
		const boxJson = {
			...rawObject,
			id: Number(rawObject.id),
			full: rawObject.full === 'true',
		}
		fetchPostData(boxJson)
		handleClose()
	}

	return (
		<>
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
				<DialogTitle>Update Shelf</DialogTitle>
				<DialogContent
					sx={{ display: 'flex', flexDirection: 'column', gap: 5 }}
				>
					<TextField
						defaultValue={row.id}
						name='id'
						label='box'
						variant='standard'
						slotProps={{
							input: {
								readOnly: true,
							},
						}}
					/>
					<TextField
						defaultValue={row.location}
						name='location'
						label='Sector'
						variant='standard'
					/>
					<TextField
						defaultValue={row.type}
						name='type'
						label='Type'
						variant='standard'
					/>
					<TextField
						defaultValue={row.capacity}
						name='capacity'
						label='Capacity'
						variant='standard'
					/>
					<TextField
						defaultValue={row.obs}
						name='obs'
						label='Obs.'
						variant='standard'
					/>
					<FormControl>
						<InputLabel id='update-select-label'>Full</InputLabel>
						<Select
							labelId='update-select-label'
							id='update-select-label'
							name='archive'
							label='Archive'
							defaultValue={row.archive}
						>
							<MenuItem value={row.archive}>Archive {row.archive}</MenuItem>
						</Select>
					</FormControl>
				</DialogContent>
				<DialogActions>
					<Button onClick={handleClose}>Cancel</Button>
					<Button type='submit'>Update</Button>
				</DialogActions>
			</Dialog>
		</>
	)
}

export default UpdateShelf
