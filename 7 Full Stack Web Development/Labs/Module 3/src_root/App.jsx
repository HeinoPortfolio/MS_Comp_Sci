//import { Post } from './components/Post.jsx'
import { PostList } from './components/PostList.jsx'


// List of posts for testing
const posts = [
{title: 'Full-Stack React Projects',
	contents: "Let's become full-stack developers!",
	author: 'Daniel Bugl'
},
{title: 'Hello React!'},
]



export function App() {
/*	return(
		<Post 
			title='Full-Stack React Projects'
			contents="Let's become full-stack developers!"
			author='Daniel Bugl'
		/> 
	)*/
	return <PostList posts={posts} />
} 