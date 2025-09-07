import {
listAllPosts, 
listPostsByAuthor, 
listPostsByTag, 
getPostById,
deletePost,
updatePost, 
createPost
} from '../services/posts.js'

// Routes for the application============================

// Route to get all the posts
export function postRoutes(app){
	// Get all the posts
	app.get('/api/v1/posts', async (req, res ) => { 
		const { sortBy, sortOrder, author, tag} = req.query 
		const options = { sortBy, sortOrder }
	
		try{
			if (author && tag) {
				return res
					.status (400)
					.json({error: 'query by either author or tag, not both'})
			}
			else if (author){
				return res.json(await listPostsByAuthor(author, options))
			}
			else if (tag){
				return res.json(await listPostsByTag(tag, options))
			}
			else{
				return res.json(await listAllPosts(options))
			}
			
		}catch(err){
			console.error('error listing posts', err)
			return res.status(500).end()
		}	
	})
	// Get the post with a specific id
	app.get('/api/v1/posts/:id', async (req, res) => {
		const {id} = req.params
		try{
			const post = await getPostById(id)
			
			if (post === null) return res.status(404).end()
			return res.json(post)
		}catch(err){
			console.error('error getting post', err)
			return res.status(500).end()		
		}
	})
	// Create a post
	app.post('api/v1/posts', async (req, res) => {
		try{
			const post = await createPost(req.body)
			return res.json(post)
		}catch(err){
			console.error('error creating post', err)
			return res.status(500).end()
		}
	})
	// Update a post given an id
	app.patch('api/v1/posts/:id', async (req, res) => {
		try{
			const post = await updatePost(req.params.id, req.body)
			return res.json(post)
		}
		catch (err){
			console.error('error updating post', err)
			return res.status(500).end()
		}
	})
	// Delete a post with a given id
	app.delete('api/v1/posts/:id', async (req, res) => {
		try {
			const { deletedCount } = await deletedPost(req.params.id)
			if (deletedCount === 0) return res.senStaus(404)
			return res.status(204).end()
		}
		catch (err){
			console.error('error deleting post' , err)
			return res.status(500).end)
		}
	})
}