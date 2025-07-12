import { useGlobalState, useDispatch } from '../../utils/globalState'

import Tabs from '@mui/material/Tabs'
import Tab from '@mui/material/Tab'
import Box from '@mui/material/Box'
import Button from '@mui/material/Button'

const ArchiveTabs = () => {
	const { which_archive, archives } = useGlobalState()
	const dispatch = useDispatch()

	const handleChange = (event, newValue) => {
		dispatch({ type: 'SET_WITCH_ARCHIVE', payload: newValue })
	}

	return (
		<Box
			sx={{
				display: 'flex',
				flexDirection: 'row',
				justifyContent: 'space-between',
			}}
		>
			<Tabs
				onChange={handleChange}
				value={which_archive}
				aria-label='Tabs where selection follows focus'
				selectionFollowsFocus
			>
				<Tab label='All' />
				{archives &&
					archives.map((archive) => (
						<Tab key={archive.id} label={archive.name} />
					))}
			</Tabs>
			<Button
				onClick={() => dispatch({ type: 'CREATE_ARCHIVE', payload: true })}
			>
				New Archive
			</Button>
		</Box>
	)
}

export default ArchiveTabs
