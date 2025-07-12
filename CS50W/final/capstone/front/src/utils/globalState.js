import React, { createContext, useReducer, useContext } from 'react'

// Estado inicial
const initialState = {
	loading: true,
	boxes: '',
	shelves: '',
	archives: '',
	boxAllVols: '',
	boxVols: '',
	recordVols: '',
	summary: '',
	situation: '',
	situations: '',
	which_archive: 0,
	create_archive: false,
}

// Função reducer
const reducer = (state, action) => {
	switch (action.type) {
		case 'LOADING':
			return { ...state, loading: action.payload }
		case 'SET_BOXES':
			console.log(state)
			return { ...state, boxes: action.payload }
		case 'SET_SHELVES':
			return { ...state, shelves: action.payload }
		case 'SET_ARCHIVES':
			return { ...state, archives: action.payload }
		case 'SET_BOX_ALL_VOLS':
			return { ...state, boxAllVols: action.payload }
		case 'SET_BOX_VOLS':
			return { ...state, boxVols: action.payload }
		case 'SET_RECORD_VOLS':
			return { ...state, recordVols: action.payload }
		case 'SET_SUMMARY':
			return { ...state, summary: action.payload }
		case 'SET_SITUATIONS':
			return { ...state, situations: action.payload }
		case 'SET_WITCH_ARCHIVE':
			return { ...state, which_archive: action.payload }
		case 'CREATE_ARCHIVE':
			return { ...state, create_archive: action.payload }
		case 'SET_SITUATION':
			return { ...state, situation: action.payload }
		case 'SET_SITUATIONS':
			return { ...state, situations: action.payload }
		default:
			return state
	}
}

const GlobalStateContext = createContext()
const DispatchContext = createContext()

export const GlobalStateProvider = ({ children }) => {
	const [state, dispatch] = useReducer(reducer, initialState)

	return (
		<GlobalStateContext.Provider value={state}>
			<DispatchContext.Provider value={dispatch}>
				{children}
			</DispatchContext.Provider>
		</GlobalStateContext.Provider>
	)
}

export const useGlobalState = () => useContext(GlobalStateContext)
export const useDispatch = () => useContext(DispatchContext)
