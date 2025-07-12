import { useState } from 'react'
import { useGlobalState } from '../../utils/globalState'

import {
	TableCell,
	TableContainer,
	Table,
	TableHead,
	TableRow,
	TableBody,
	Tooltip,
} from '@mui/material'
import UpdateBox from './UpdateBox'
import ArticleOutlinedIcon from '@mui/icons-material/ArticleOutlined'

const TableBox = ({ cardColor }) => {
	const [open, setOpen] = useState(false)
	const [boxRow, setBoxRow] = useState({})
	const { boxes, boxVols } = useGlobalState()

	const renderBoxes =
		boxes &&
		boxes.map((box) => {
			const exisVols = boxVols.find((item) => item.box === box.id)
			if (exisVols) {
				return { ...box, vols: exisVols.volumes }
			}
			return { ...box, vols: 0 }
		})

	const handleClickOpen = (e) => {
		const x = e.target.getAttribute('value')
		if (boxes) {
			const box = boxes.find((item) => item.id === Number(x))
			setBoxRow(box)
		}
		open ? setOpen(false) : setOpen(true)
	}

	return (
		<>
			<TableContainer
				sx={{
					maxHeight: 160,
					'&::-webkit-scrollbar': {
						width: '12px',
					},
					'&::-webkit-scrollbar-thumb': {
						backgroundColor: 'orange',
						borderRadius: '4px',
					},
					'&::-webkit-scrollbar-track': {
						backgroundColor: cardColor,
					},
				}}
			>
				<Table sx={{ backgroundColor: 'inherit' }} stickyHeader size='small'>
					<TableHead>
						<TableRow>
							<TableCell
								sx={{ backgroundColor: cardColor, borderBottom: 'none' }}
							>
								Box
							</TableCell>
							<TableCell
								sx={{
									backgroundColor: cardColor,
									borderBottom: 'none',
								}}
								align='right'
							>
								Shelf
							</TableCell>
							<TableCell
								sx={{
									backgroundColor: cardColor,
									borderBottom: 'none',
								}}
								align='right'
							>
								Volumes
							</TableCell>
							<TableCell
								sx={{ backgroundColor: cardColor, borderBottom: 'none' }}
								align='right'
							>
								Obs.
							</TableCell>
						</TableRow>
					</TableHead>

					<TableBody>
						{renderBoxes &&
							renderBoxes
								.sort((a, b) => b.id - a.id)
								.map((row) => (
									<TableRow
										key={row.id}
										sx={{
											'&:last-child td, &:last-child th': { border: 0 },
										}}
									>
										<TableCell
											sx={{ borderBottom: 'none' }}
											component='th'
											scope='row'
										>
											{row.id}
										</TableCell>
										<TableCell sx={{ borderBottom: 'none' }} align='right'>
											{row.shelf}
										</TableCell>

										<TableCell sx={{ borderBottom: 'none' }} align='right'>
											{row.vols}
										</TableCell>

										<TableCell sx={{ borderBottom: 'none' }} align='right'>
											<Tooltip disableFocusListener title={row.box_obs} arrow>
												<ArticleOutlinedIcon fontSize='small' />
											</Tooltip>
										</TableCell>
										<TableCell
											value={row.id}
											onClick={handleClickOpen}
											sx={{ borderBottom: 'none', cursor: 'pointer' }}
											align='right'
										>
											update
										</TableCell>
									</TableRow>
								))}
						{boxRow && <UpdateBox row={boxRow} open={open} setOpen={setOpen} />}
					</TableBody>
				</Table>
			</TableContainer>
		</>
	)
}

export default TableBox
