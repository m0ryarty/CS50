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

const ExpireTable = () => {
	const { situation, which_archive } = useGlobalState()
	const [open, setOpen] = useState(false)
	const [record, setRecord] = useState({})

	const RenderUpdate = ({ row }) => {
		return (
			<Box
				onClick={() => {
					open ? setOpen(false) : setOpen(true)
					setRecord({
						id: row.id,
						record: row.record,
						situation: row.situation,
					})
				}}
				sx={{ cursor: 'pointer' }}
			>
				Update
			</Box>
		)
	}

	const columns = [
		{
			field: 'record',
			headerName: 'Record',
			width: 200,
		},
		{
			field: 'date',
			headerName: 'When expired',
			type: 'number',
			width: 130,
		},
		{
			field: 'expire',
			headerName: 'Days',
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

	const analysisRows = () => {
		const analysis = []
		situation &&
			situation.forEach((element) => {
				if (which_archive === 0) {
					if (element.days_to_expire < 0) {
						const data = {
							id: element.record,
							record: `${element.code}-${element.digit}.${element.year}.8.16.${element.unity}`,
							date: formatDate(element.expire),
							expire: element.days_to_expire * -1,
							situation: element.situation_type,
						}
						analysis.push(data)
					}
				} else {
					if (element.days_to_expire < 0 && element.archive === which_archive) {
						const data = {
							id: element.record,
							record: `${element.code}-${element.digit}.${element.year}.8.16.${element.unity}`,
							date: formatDate(element.expire),
							expire: element.days_to_expire * -1,
							situation: element.situation_type,
						}
						analysis.push(data)
					}
				}
			})
		return analysis
	}

	return (
		analysisRows().length > 0 && (
			<>
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
				</Box>
				<UpdateSituation record={record} open={open} setOpen={setOpen} />
			</>
		)
	)
}

export default ExpireTable
