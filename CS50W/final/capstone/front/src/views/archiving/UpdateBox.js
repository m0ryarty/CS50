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

const UpdateBox = ({ row, open, setOpen }) => {
	const api = useAxios()
	const dispatch = useDispatch()

	const handleClose = () => {
		setOpen(false)
	}
	const fetchPostData = async (boxJson) => {
		try {
			const response = await api.put('/boxes', boxJson, {
				headers: {
					'Content-Type': 'application/json',
				},
			})

			dispatch({
				type: 'SET_BOXES',
				payload: response.data.response.boxes,
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
				<DialogTitle>Update Box</DialogTitle>
				<DialogContent
					sx={{ display: 'flex', flexDirection: 'column', gap: 5 }}
				>
					<TextField value={row.id} name='id' label='Box' variant='standard' />
					<TextField
						defaultValue={row.shelf}
						name='shelf'
						label='Shelf'
						variant='standard'
					/>
					<TextField
						defaultValue={row.box_obs}
						name='obs'
						label='Obs'
						variant='standard'
					/>
					<FormControl>
						<InputLabel id='update-select-label'>Full</InputLabel>
						<Select
							labelId='update-select-label'
							id='update-select-label'
							name='full'
							label='Full'
							defaultValue={false}
						>
							<MenuItem value={false}>False</MenuItem>
							<MenuItem value={true}>True</MenuItem>
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

export default UpdateBox
