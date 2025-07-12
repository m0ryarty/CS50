import React from 'react';
import ReactDOM from 'react-dom/client';

import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';

import { GlobalStateProvider } from './utils/globalState'
import { RouterProvider } from 'react-router'
import { AuthProvider } from './context/AuthContext'
import router from './utils/router'

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(
	<React.StrictMode>
		<GlobalStateProvider>
			<AuthProvider>
				<RouterProvider router={router} />
			</AuthProvider>
		</GlobalStateProvider>
	</React.StrictMode>
)

