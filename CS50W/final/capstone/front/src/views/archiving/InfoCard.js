import { useGlobalState } from '../../utils/globalState'
import CreateBox from './CreateBox'
import CreateShelf from './CreateShelf'
import {
	Card,
	CardContent,
	Typography,
	CircularProgress,
	Paper,
} from '@mui/material'
import { Link } from 'react-router-dom'
import TableBox from './TableBox'
import TableShelf from './TableShelf'

const InfoCard = ({ cardColor, cardTitle, cardItem }) => {
	const { loading } = useGlobalState()

	return (
		<Card
			sx={{
				display: 'flex',
				flexDirection: 'column',
				justifyContent: 'space-between',
				backgroundColor: cardColor,
				width: '100%',
				minWidth: 300,
				maxWidth: 550,
				height: 250,
			}}
		>
			<CardContent>
				<Typography variant='h6' component='div'>
					<Link
						style={{ textDecoration: 'none', color: 'inherit' }}
						to={`/${cardTitle.toLowerCase()}`}
					>
						{cardTitle}
					</Link>
				</Typography>
				{loading ? (
					<CircularProgress size='3rem' color='inherit' />
				) : (
					<Paper
						sx={{
							width: '100%',
							overflow: 'hidden',
							backgroundColor: 'inherit',
						}}
					>
						{cardTitle === 'Boxes' && <TableBox cardColor={cardColor} />}
						{cardTitle === 'Shelves' && <TableShelf cardColor={cardColor} />}
					</Paper>
				)}
				{cardItem === 'Box' && <CreateBox />}
				{cardItem === 'Shelf' && <CreateShelf />}
			</CardContent>
		</Card>
	)
}

export default InfoCard
