import { useState } from 'react'
import Box from '@mui/material/Box'
import { DataGrid } from '@mui/x-data-grid'
import { useGlobalState } from '../../utils/globalState'

import UpdateSituation from './UpdateSituation'

const formatDate = (timestamp) => {
	const date = new Date(timestamp)
	const day = date.getDate()
	const month = date.getMonth() + 1
	const year = date.getFullYear()
	const formattedDate = `${day}/${month}/${year}`

	return formattedDate
}

const AnalysisTable = () => {
	const { situation, which_archive } = useGlobalState()
	const [open, setOpen] = useState(false)
	const [record, setRecord] = useState({})

	const RenderUpdate = ({ row }) => {
		return (
			<Box
				onClick={() => {
					open ? setOpen(false) : setOpen(true)
					setRecord({ id: row.id, record: row.record })
				}}
				sx={{ cursor: 'pointer' }}
			>
				Update
			</Box>
		)
	}

	const analysisRows = () => {
		const analysis = []
		situation &&
			situation.forEach((element) => {
				if (element.situation_type === 1) {
					if (which_archive === 0) {
						if (element.days_to_expire > 0) {
							const data = {
								id: element.record,
								record: `${element.code}-${element.digit}.${element.year}.8.16.${element.unity}`,
								date: formatDate(element.date),
								expire: element.days_to_expire,
								situation: element.situation_type,
							}
							analysis.push(data)
						}
					} else {
						if (
							element.days_to_expire > 0 &&
							element.archive === which_archive
						) {
							const data = {
								id: element.record,
								record: `${element.code}-${element.digit}.${element.year}.8.16.${element.unity}`,
								date: formatDate(element.date),
								expire: element.days_to_expire,
								situation: element.situation_type,
							}
							analysis.push(data)
						}
					}
				}
			})
		return analysis
	}

	const columns = [
		{
			field: 'record',
			headerName: 'Record',
			width: 200,
		},
		{
			field: 'date',
			headerName: 'Date of Analysis',
			type: 'number',
			width: 130,
		},
		{
			field: 'expire',
			headerName: 'Days to expire',
			type: 'number',
			width: 110,
		},
		{
			field: 'update',
			headerName: '',
			width: 110,
			renderCell: RenderUpdate,
		},
	]

	return (
		<Box sx={{ display: 'flex', flexDirection: 'columns' }}>
			<DataGrid
				rows={analysisRows()}
				columns={columns}
				initialState={{
					pagination: {
						paginationModel: {
							pageSize: 5,
						},
					},
				}}
				autosizeOptions={{
					includeOutliers: true,
				}}
				pageSizeOptions={[5]}
				disableRowSelectionOnClick
			/>
			<UpdateSituation record={record} open={open} setOpen={setOpen} />
		</Box>
	)
}

export default AnalysisTable
