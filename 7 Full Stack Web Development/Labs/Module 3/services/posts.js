import { Post } from '../db/models/post.js'

// List all posts 
async function listPosts( 
	query = {},
	{sortBy = 'createdAt', sortOrder = 'descending'} = {},
	){
		return await Post.find(query).sort({[sortBy]: sortOrder})
	}

// Create a new post			
export async function createPost({title, author, contents, tags}) {
	const post = new Post ({title, author, contents, tags})
		return await post.save()
			
}

// List all the posts in the database
export async function listAllPosts(options){
	return await listPosts({}, options)
}

// List all the posts by an author
export async function listPostsByAuthor(author, options){
	return await listPosts({author}, options)
}

// List all posts by tags
export async function listPostsByTag(tags, options){
	return await listPosts({tags}, options)
}
