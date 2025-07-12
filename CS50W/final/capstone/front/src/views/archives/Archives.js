import { useGlobalState } from '../../utils/globalState'

import Box from '@mui/material/Box'

import CreateArchives from './CreateArchives'
import ArchiveTabs from './ArchiveTabs'
import ArchivesContent from './ArchivesContent'

const Archives = () => {
	const { create_archive } = useGlobalState()

	return create_archive ? (
		<CreateArchives />
	) : (
		<Box sx={{ width: '100%' }}>
			<ArchiveTabs />
			<ArchivesContent />
		</Box>
	)
}

export default Archives
