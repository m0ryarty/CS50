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
import ArticleOutlinedIcon from '@mui/icons-material/ArticleOutlined'

import UpdateShelf from './UpdateShelf'

const TableShelf = ({ cardColor }) => {
	const [open, setOpen] = useState(false)
	const [shelfRow, setShelfRow] = useState({})
	const { shelves, archives } = useGlobalState()

	const handleClickOpen = (e) => {
		const x = e.target.getAttribute('value')
		if (shelves) {
			const shelf = shelves.find((item) => item.id === Number(x))
			setShelfRow(shelf)
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
						backgroundColor: 'blue',
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
								Shelf
							</TableCell>
							<TableCell
								sx={{
									backgroundColor: cardColor,
									borderBottom: 'none',
								}}
								align='right'
							>
								Type
							</TableCell>
							<TableCell
								sx={{ backgroundColor: cardColor, borderBottom: 'none' }}
								align='right'
							>
								Sector
							</TableCell>
							<TableCell
								sx={{ backgroundColor: cardColor, borderBottom: 'none' }}
								align='right'
							>
								Capacity
							</TableCell>
							<TableCell
								sx={{ backgroundColor: cardColor, borderBottom: 'none' }}
								align='right'
							>
								Archive
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
						{shelves &&
							shelves
								.sort((a, b) => b.id - a.id)
								.map(
									(row) =>
										row.boxes < row.capacity && (
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
												<TableCell
													align='center'
													sx={{ borderBottom: 'none' }}
													component='th'
													scope='row'
												>
													{row.type}
												</TableCell>
												<TableCell sx={{ borderBottom: 'none' }} align='center'>
													{row.location}
												</TableCell>
												<TableCell sx={{ borderBottom: 'none' }} align='center'>
													{row.boxes}/{row.capacity}
												</TableCell>
												{archives.map(
													(item) =>
														item.id === row.archive && (
															<TableCell
																key={item.id}
																sx={{ borderBottom: 'none' }}
																align='center'
															>
																{item.name}
															</TableCell>
														)
												)}

												{row.obs ? (
													<TableCell
														sx={{ borderBottom: 'none' }}
														align='center'
													>
														<Tooltip disableFocusListener title={row.obs} arrow>
															<ArticleOutlinedIcon fontSize='small' />
														</Tooltip>
													</TableCell>
												) : (
													<TableCell
														sx={{ borderBottom: 'none' }}
														align='right'
													></TableCell>
												)}

												<TableCell
													value={row.id}
													onClick={handleClickOpen}
													sx={{ borderBottom: 'none', cursor: 'pointer' }}
													align='right'
												>
													update
												</TableCell>
											</TableRow>
										)
								)}
						{shelfRow && (
							<UpdateShelf row={shelfRow} open={open} setOpen={setOpen} />
						)}
					</TableBody>
				</Table>
			</TableContainer>
		</>
	)
}

export default TableShelf
