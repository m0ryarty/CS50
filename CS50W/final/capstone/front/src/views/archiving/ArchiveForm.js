import React from 'react'
import useAxios from '../../utils/useAxios'
import {
	Card,
	CardHeader,
	CardContent,
	Button,
	TextField,
	Paper,
	Grow,
} from '@mui/material'
import { green } from '@mui/material/colors'
import { Box, Select } from '@mui/material'
import { useState } from 'react'
import InputLabel from '@mui/material/InputLabel'
import MenuItem from '@mui/material/MenuItem'
import FormControl from '@mui/material/FormControl'
import Checkbox from '@mui/material/Checkbox'
import FormControlLabel from '@mui/material/FormControlLabel'

import { styled } from '@mui/material/styles'
import Tooltip, { tooltipClasses } from '@mui/material/Tooltip'
import Typography from '@mui/material/Typography'

import { IMaskInput } from 'react-imask'
import { useGlobalState, useDispatch } from '../../utils/globalState'

const ArchiveForm = () => {
	const [selectBox, setSelectBox] = useState('')
	const [exists, setExists] = useState(true)
	const [record, setRecord] = useState('')
	const [exist_record, setExistRecord] = useState('')
	const { boxVols, recordVols, boxes } = useGlobalState()

	const dispatch = useDispatch()
	const api = useAxios()

	const handleChangeBox = (event) => {
		setSelectBox(event.target.value)
	}

	const handleExists = async (event) => {
		const value = event.target.value
		const number_length = value.length === 25

		try {
			if (number_length && verifyDigit(value)) {
				const response = await api.post(
					'/exist_record',
					{ record: value },
					{
						headers: {
							'Content-Type': 'application/json',
						},
					}
				)

				setExists(response.data.exists)
				setExistRecord(response.data.record)
				setRecord(value)
			} else if (value.length === 0) setRecord(value)
		} catch (error) {
			console.error(error)
		}
	}

	const MaskedTextField = React.forwardRef(function MaskedTextField(
		props,
		ref
	) {
		const { onChange, ...other } = props

		return (
			<IMaskInput
				{...other}
				mask='0000000-00.0000.0.00.0000'
				definitions={{
					0: /[0-9]/,
				}}
				inputRef={ref}
				onAccept={(value) => onChange({ target: { value } })}
			/>
		)
	})

	const verifyDigit = (number) => {
		const splitted = number.split(/[.-]/)

		const r1 = (Number(splitted[0]) % 97).toString()
		const r2 = (
			Number(r1 + splitted[2] + splitted[3] + splitted[4]) % 97
		).toString()

		const r3 = Number(r2 + splitted[5] + '00') % 97
		const aDigit = 98 - r3

		const digit = Number(splitted[1])

		if (digit === aDigit) {
			return true
		} else {
			throw new Error('Number is not valid!')
		}
	}

	const fetchPostData = async (recordJson) => {
		try {
			if (verifyDigit(recordJson.number)) {
				const response = await api.post('/archiving', recordJson, {
					headers: {
						'Content-Type': 'application/json',
					},
				})
				const data = await response.data.response

				console.log(response)

				await dispatch({ type: 'SET_BOXES', payload: data.boxes })

				await dispatch({ type: 'SET_BOX_VOLS', payload: data.box_volumes })

				await dispatch({ type: 'SET_RECORD_VOLS', payload: data.recordVols })

				await dispatch({ type: 'SET_BOX_ALL_VOLS', payload: data.boxAllVols })

				await dispatch({ type: 'SET_SUMMARY', payload: data.summary })

				await dispatch({ type: 'SET_SITUATIONS', payload: data.situations })

				await dispatch({ type: 'SET_SITUATION', payload: data.situation })

				setSelectBox('')
				setExists(true)
			}
		} catch (error) {
			console.error(error)
		}
	}

	const handleSubmit = (event) => {
		event.preventDefault()
		const formData = new FormData(event.currentTarget)
		const recordJson = Object.fromEntries(formData.entries())
		fetchPostData(recordJson)
	}

	const HtmlTooltip = styled(({ className, ...props }) => (
		<Tooltip {...props} classes={{ popper: className }} />
	))(({ theme }) => ({
		[`& .${tooltipClasses.tooltip}`]: {
			backgroundColor: '#f5f5f9',
			color: 'rgba(0, 0, 0, 0.87)',
			maxWidth: 220,
			fontSize: theme.typography.pxToRem(12),
			border: '1px solid #dadde9',
		},
	}))

	return (
		<Card sx={{ minWidth: 'px', backgroundColor: green.A700 }}>
			<Box
				sx={{
					display: 'flex',
					justifyContent: 'space-between',
					marginRight: 10,
				}}
			>
				<CardHeader title='Archive Record' />
				{exist_record && (
					<CardContent>
						<HtmlTooltip
							title={
								<Paper>
									{recordVols &&
										recordVols.map(
											(item) =>
												item.record === exist_record && (
													<Typography key={item.volumes}>
														Total Volumes: {item.volumes}
													</Typography>
												)
										)}
									{boxVols &&
										boxVols.map(
											(item) =>
												item.record === exist_record && (
													<Typography key={item.box}>
														Box {item.box} with {item.volumes} volumes
													</Typography>
												)
										)}
								</Paper>
							}
							TransitionComponent={Grow}
							TransitionProps={{ timeout: 800 }}
						>
							<Typography variant='h6'>Summary</Typography>
						</HtmlTooltip>
					</CardContent>
				)}
			</Box>

			<Paper sx={{ backgroundColor: 'inherit', margin: 2 }}>
				<CardContent>
					<form onSubmit={handleSubmit}>
						<Box sx={{ display: 'flex', gap: 1, marginBottom: 2 }}>
							<TextField
								label=' Number'
								name='number'
								value={record}
								onChange={handleExists}
								slotProps={{
									input: {
										inputComponent: MaskedTextField,
									},
								}}
								required
								fullWidth
							/>
							{!exists && (
								<TextField
									label='Plaintiff'
									name='plaintiff'
									required
									fullWidth
								/>
							)}
							{!exists && (
								<TextField
									label='Defendant'
									name='defendant'
									required
									fullWidth
								/>
							)}
						</Box>
						<Box sx={{ display: 'flex', gap: 1, marginBottom: 2 }}>
							{!exists && (
								<TextField label=' Old Number' name='former_code' fullWidth />
							)}
							<TextField label='Volumes' name='volumes' required fullWidth />
							<FormControl fullWidth>
								<InputLabel id='demo-simple-select-label'>Box</InputLabel>
								<Select
									labelId='demo-simple-select-label'
									id='demo-simple-select'
									value={selectBox}
									label='Box'
									name='box'
									onChange={handleChangeBox}
								>
									{boxes &&
										boxes
											.sort((a, b) => a.id - b.id)
											.map(
												(item) =>
													item.full === false && (
														<MenuItem key={item.id} value={item.id} name='box'>
															Box {item.id}
														</MenuItem>
													)
											)}
								</Select>
								<FormControlLabel
									control={<Checkbox name='full' />}
									label='Full'
								/>
							</FormControl>
						</Box>
						<Button type='submit' variant='standard' fullWidth>
							Archive Record
						</Button>
					</form>
				</CardContent>
			</Paper>
		</Card>
	)
}

export default ArchiveForm
