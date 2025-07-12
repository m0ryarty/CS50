import Box from '@mui/material/Box'
import Card from '@mui/material/Card'
import CardContent from '@mui/material/CardContent'
import Typography from '@mui/material/Typography'
import CircularProgress from '@mui/material/CircularProgress'
import { Link } from 'react-router-dom'

import { useGlobalState, useDispatch } from '../utils/globalState'

const Homepage = () => {
	const { summary, archives, loading } = useGlobalState()
	const dispatch = useDispatch()
	const handleArchive = (archive) => {
		dispatch({ type: 'SET_WITCH_ARCHIVE', payload: archive })
	}

	return loading ? (
		<CircularProgress size='8rem' />
	) : (
		<Box>
			{archives &&
				summary.map((archive) => {
					return (
						<Card sx={{ minWidth: 275, marginBottom: 1 }}>
							<Link
								key={archive.archive}
								style={{ textDecoration: 'none', color: 'inherit' }}
								to={'/archives'}
							>
								<CardContent
									key={archive.archive}
									onClick={() => handleArchive(archive.archive)}
								>
									{archives.map(
										(item) =>
											item.id === archive.archive && (
												<Typography
													key={item.name}
													variant='h5'
													component='div'
												>
													{item.name}
												</Typography>
											)
									)}
									<Typography variant='body2'>
										{archive.total_volumes} volumes in {archive.num_boxes} boxes
										in {archive.num_shelves} shelves
									</Typography>
									<Typography variant='body2'>
										{archive.analysis} records to analysis
									</Typography>
									<Typography variant='body2'>
										{archive.expired} records with expired date
									</Typography>
									<Typography variant='body2'>
										{archive.elimination} records to be eliminated
									</Typography>
								</CardContent>
							</Link>
						</Card>
					)
				})}
		</Box>
	)
}

export default Homepage
