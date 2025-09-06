import mongoose from 'mongoose'
import { describe, expect, test, beforeEach} from '@jest/globals'
import { createPost,listAllPosts, listPostsByTag, listPostsByAuthor } from '../services/posts.js'
import { Post } from '../db/models/post.js'

const samplePosts = [ 		
	{title: 'Learning Redux', author: 'Daniel Bugl', tags: ['redux']},
	{title: 'Learn React Hooks', author: 'Daniel Bugl', tags: ['react']},
	{title: 'Full-Stack React Projects', author: 'Daniel Bugl', tags: ['react','nodejs']},
	{title: 'Guide to Typescript'},
]

let createdSamplePosts = []

beforeEach(async () => {
	await Post.deleteMany({})
	
	createdSamplePosts = []	
		for (const post of samplePosts){
			const createdPost = new Post(post)
			createdSamplePosts.push(await createdPost.save())
		}
})

// Test listing posts
describe ('listing posts', () => {
	test('should return all posts', async () => {
		const posts = await listAllPosts()
		expect(posts.length).toEqual(createdSamplePosts.length)
	})
	test('should be able to filter post by tag', async () => {
		const posts = await listPostsByTag('nodejs')
		expect(posts.length).toBe(1)
	})
	test('should be able to filter post by author', async () => {
   		const posts = await listPostsByAuthor('Daniel Bugl')
		expect(posts.length).toBe(3)
  	})	
	test('should return posts in sorted by creation data descending', async () => {
		const posts = await listAllPosts()
		const sortedSamplePosts = createdSamplePosts.sort(
			(a, b) => b.createdAt - a.createdAt,
		)
		expect(posts.map((post) => post.createdAt)).toEqual(
		sortedSamplePosts.map((post) => post.createdAt),
		)
	})
	test('should take into account provided sorting options', async () => {
		const posts = await listAllPosts({
		sortBy: 'updateAt',
		sortOrder: 'ascending',
        })
		const sortedSamplePosts = createdSamplePosts.sort(
		(a, b) => a.updatedAt - b.updatedAt,
		)
		expect(posts.map((post) => post.updatedAt)).toEqual(
		sortedSamplePosts.map((post) => post.updatedAt), )
	})
})


// Test creating posts ===============================================
describe('creating posts', () => {
		
	test('with all parameters should succeed',  async () => {
		const post = {
			title: 'Hello Mongoose!',
			author: 'Huseyin Ergin',
			contents: 'This post is stored in a MongoDB database using Mongoose.',
			tags: ['mongoose','mongodb']
		}
		
		const createdPost = await createPost(post)
		
		expect 	(createdPost._id).toBeInstanceOf(mongoose.Types.ObjectId)
		
		const foundPost = await Post.findById(createdPost._id)
		
		expect(foundPost).toEqual(expect.objectContaining(post))
		expect(foundPost.createdAt).toBeInstanceOf(Date)
		expect(foundPost.updatedAt).toBeInstanceOf(Date)
		
		})
		
	test('without title should fail',  async () => {
		const post = {
			author: 'Huseyin Ergin',
			contents: 'This post is stored in a MongoDB database using Mongoose.',
			tags: ['empty']
		}
		try {
			await createPost(post)
		}
		catch(err){
			expect(err).toBeInstanceOf(mongoose.Error.ValidationError)
			expect(err.message).toContain('`title` is required') 
		}	
	})
	test('with minimal parameters should succeed',  async () => {
		const post = {
			title: 'Only a title',
		}
			
		const createdPost = await createPost(post)
		expect 	(createdPost._id).toBeInstanceOf(mongoose.Types.ObjectId)
	})
})