import Box from '@mui/material/Box'
import Card from '@mui/material/Card'
import CardContent from '@mui/material/CardContent'
import Typography from '@mui/material/Typography'

import AnalysisTable from './AnalysisTable'
import ExpireTable from './ExpireTable'

import { useGlobalState } from '../../utils/globalState'

const ArchivesContent = () => {
	const { which_archive, archives, summary } = useGlobalState()

	const reducedSummary =
		summary &&
		summary.reduce((accumulator, current) => {
			for (const key in current) {
				// Check if the key exists in the accumulator, else initialize it
				if (key !== 'archive') {
					// Exclude the "archive" key if needed
					accumulator[key] = (accumulator[key] || 0) + current[key]
				}
			}
			return accumulator
		}, {})

	return (
		<Box>
			{which_archive === 0 ? (
				<Card>
					<CardContent>
						<Typography variant='h5' component='div'>
							All Archives
						</Typography>
						<Typography variant='body2'>
							{reducedSummary.total_volumes} volumes in{' '}
							{reducedSummary.num_boxes} boxes in {reducedSummary.num_shelves}{' '}
							shelves
						</Typography>
						<AnalysisTable />
						<ExpireTable />
					</CardContent>
				</Card>
			) : (
				summary &&
				summary.map((summary, index) => {
					return (
						index + 1 === which_archive && (
							<Card key={summary.id}>
								<CardContent>
									{archives.map(
										(archive, index) =>
											index + 1 === which_archive && (
												<Typography
													key={archive.name}
													variant='h5'
													component='div'
												>
													{archive.name}
												</Typography>
											)
									)}
									<Typography variant='body2'>
										{summary.total_volumes} volumes in {summary.num_boxes} boxes
										in {summary.num_shelves} shelves
									</Typography>
									<AnalysisTable />
									<ExpireTable />
								</CardContent>
							</Card>
						)
					)
				})
			)}
		</Box>
	)
}

export default ArchivesContent
