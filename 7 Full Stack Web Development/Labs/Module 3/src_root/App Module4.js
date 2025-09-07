import {Blog} from './Blog.jsx'

//Create a client
const queryClient = new QueryClient() 

// setup for TanStack Query
export function App(){
	return(
		<QueryClientProvider client={queryClient}>
			<Blog/>
		</QueryClientProvider>
	)
}