import DashboardIcon from '@mui/icons-material/Dashboard'
import AppsIcon from '@mui/icons-material/Apps'
import BarChartIcon from '@mui/icons-material/BarChart'

import HomeIcon from '@mui/icons-material/Home'
import LayersIcon from '@mui/icons-material/Layers'
import { createTheme } from '@mui/material/styles'
import { blueGrey, orange } from '@mui/material/colors'
import AccountBalanceIcon from '@mui/icons-material/AccountBalance'
import CalendarViewMonthIcon from '@mui/icons-material/CalendarViewMonth'
import FactCheckIcon from '@mui/icons-material/FactCheck'
import FlipCameraIosIcon from '@mui/icons-material/FlipCameraIos'
import ThumbDownAltIcon from '@mui/icons-material/ThumbDownAlt'

const NAVIGATION = [
	{
		kind: 'header',
		title: 'Main items',
	},
	{
		segment: 'home',
		title: 'Home',
		icon: <HomeIcon />,
	},
	{
		segment: 'archiving',
		title: 'Archiving',
		icon: <DashboardIcon />,
	},
	{
		kind: 'divider',
	},
	{
		kind: 'header',
		title: 'Structure',
	},
	{
		segment: 'archives',
		title: 'Archives',
		icon: <AccountBalanceIcon />,
	},
	{
		segment: 'shelves',
		title: 'Shelves',
		icon: <CalendarViewMonthIcon />,
	},
	{
		segment: 'boxes',
		title: 'Boxes',
		icon: <FactCheckIcon />,
	},
	{
		kind: 'divider',
	},
	{
		kind: 'header',
		title: 'Analytics',
	},
	{
		segment: 'reports',
		title: 'Reports',
		icon: <BarChartIcon />,
		children: [
			{
				segment: 'analysis',
				title: 'Analysis',
				icon: <FlipCameraIosIcon />,
			},
			{
				segment: 'elimination',
				title: 'Elimination',
				icon: <ThumbDownAltIcon />,
			},
		],
	},
	{
		segment: 'integrations',
		title: 'Integrations',
		icon: <LayersIcon />,
	},
]

const BRANDING = {
	logo: <AppsIcon color='primary' sx={{ fontSize: 35 }} />,
	title: 'Archive',
	homeUrl: '/home',
}

const THEME = createTheme({
	cssVariables: {
		colorSchemeSelector: 'data-toolpad-color-scheme',
	},
	colorSchemes: {
		light: {
			palette: {
				background: {
					default: blueGrey[100],
					paper: blueGrey[50],
					boxCardColor: orange[400],
				},
			},
		},
		dark: {
			palette: {
				background: {
					default: blueGrey[800],
					paper: blueGrey[900],
					boxCardColor: orange[700],
				},
			},
		},
	},
	breakpoints: {
		values: {
			xs: 0,
			sm: 600,
			md: 600,
			lg: 1200,
			xl: 1536,
		},
	},
})

export { NAVIGATION, BRANDING, THEME }
