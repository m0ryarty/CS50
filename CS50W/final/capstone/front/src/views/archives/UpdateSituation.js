import useAxios from '../../utils/useAxios'
import { useDispatch, useGlobalState } from '../../utils/globalState'
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
	Typography,
} from '@mui/material'

const UpdateSituation = ({ record, open, setOpen }) => {
	const api = useAxios()
	const dispatch = useDispatch()
	const { situations } = useGlobalState()

	const handleClose = () => {
		setOpen(false)
	}
	const fetchPostData = async (situationJson) => {
		try {
			const response = await api.post('/create_situations', situationJson, {
				headers: {
					'Content-Type': 'application/json',
				},
			})

			console.log(response.data)

			dispatch({
				type: 'SET_SITUATION',
				payload: response.data.response.situation,
			})
		} catch (error) {
			console.error(error)
		}
	}

	const handleSubmit = (event) => {
		event.preventDefault()
		const formData = new FormData(event.currentTarget)

		const rawObject = Object.fromEntries(formData.entries())
		console.log(rawObject)
		fetchPostData(rawObject)
		handleClose()
	}

	const capitalize = (str) => str.charAt(0).toUpperCase() + str.slice(1)

	console.log(record)

	return (
		<>
			<Dialog
				open={open}
				onClose={handleClose}
				fullWidth={true}
				maxWidth={'xs'}
				slotProps={{
					paper: {
						component: 'form',
						onSubmit: (e) => handleSubmit(e),
					},
				}}
			>
				<DialogTitle>Update Record</DialogTitle>
				<DialogContent
					sx={{ display: 'flex', flexDirection: 'column', gap: 5 }}
				>
					<TextField
						name='id'
						sx={{ display: 'none' }}
						defaultValue={record.id}
					/>
					<TextField
						label='Record'
						name='record'
						defaultValue={record.record}
						slotProps={{
							input: {
								readOnly: true,
							},
						}}
						variant='standard'
					/>

					<FormControl>
						<InputLabel id='update-select-label'>Situation</InputLabel>
						<Select
							labelId='update-select-label'
							id='update-select-label'
							name='situation'
							label='Situation'
							defaultValue={record.situation || 1}
						>
							{situations &&
								situations.map((situation) => (
									<MenuItem key={situation.id} value={situation.id}>
										{capitalize(situation.type)}
									</MenuItem>
								))}
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

export default UpdateSituation
