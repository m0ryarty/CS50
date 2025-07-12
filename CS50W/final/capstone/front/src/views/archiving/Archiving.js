import Box from '@mui/material/Box'
import InfoCard from './InfoCard'
import { blue, orange } from '@mui/material/colors'
import ArchiveForm from './ArchiveForm'
import { useGlobalState } from '../../utils/globalState'

const Archiving = () => {
	const { boxes } = useGlobalState()

	return (
		<Box sx={{ display: 'flex', flexDirection: 'column', gap: 5 }}>
			<Box
				sx={{
					display: 'flex',
					flexWrap: 'wrap',
					gap: 3,
					justifyContent: 'space-between',
				}}
			>
				<InfoCard cardColor={orange.A700} cardTitle='Boxes' cardItem='Box' />
				<InfoCard cardColor={blue.A700} cardTitle='Shelves' cardItem='Shelf' />
			</Box>
			<ArchiveForm selectItem={boxes} />
		</Box>
	)
}

export default Archiving
