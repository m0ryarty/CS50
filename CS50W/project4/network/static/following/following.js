const getPosts = async () => {
	const response = await fetch('follow_posts', {
		method: 'GET',
	})
	const data = await response.json()

	return await data
}

const getCookie = (name) => {
	var cookieValue = null
	if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';')
		for (var i = 0; i < cookies.length; i++) {
			var cookie = cookies[i].trim()
			if (cookie.substring(0, name.length + 1) === name + '=') {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
				break
			}
		}
	}
	return cookieValue
}

var csrftoken = getCookie('csrftoken')

const CSRFToken = () => {
	return <input type='hidden' name='csrfmiddlewaretoken' value={csrftoken} />
}

const Like = ({ like, numberLikes, userId, postUser, postId, updateLike }) => {
	const handleLike = (e) => {
		e.preventDefault()

		if (postUser != userId) {
			const form = e.target

			const formData = new FormData(form)
			formData.append('likeUser', userId)
			formData.append('likePost', postId)

			fetch('like', { method: 'POST', body: formData })
			updateLike(postId)
		}
	}

	return (
		<div class='col col-sm-2 d-flex flex-row-reverse'>
			<form method='post' onSubmit={handleLike}>
				<CSRFToken />
				<button
					type='submit'
					class='d-flex btn justify-content-end align-items-end'
				>
					<div> {numberLikes} </div>
					<span class='fs-4'>
						{like ? (
							<div>
								<i class='bi bi-heart-fill text-danger'></i>
							</div>
						) : (
							<i class='bi bi-heart'></i>
						)}
					</span>
				</button>
			</form>
		</div>
	)
}

const AllPosts = ({ posts, setNewPosts }) => {
	const updateLike = (id) => {
		const newPosts = posts.map((item) => {
			if (item.id === id) {
				item.liked ? (item.liked = false) : (item.liked = true)
				item.liked ? item.numberLikes++ : item.numberLikes--
			}
			return item
		})

		setNewPosts(newPosts)
	}

	return (
		<div>
			<h5 class='mt-3 bg-light'>
				<span>
					<i class='bi bi-text-indent-left'></i>
				</span>
				Posts
			</h5>
			<div>
				{posts.map((item) => {
					const lines = item.post.split('\n')

					return (
						<div class='card card-text'>
							<div class='row'>
								<div class='col'>
									{lines.map((p) => {
										return <div class='lead post-text'>{p}</div>
									})}
								</div>

								<Like
									like={item.liked}
									numberLikes={item.numberLikes}
									userId={item.loggedUser}
									postUser={item.user_id}
									postId={item.id}
									updateLike={updateLike}
								/>
							</div>

							<h6 class='card-subtitle mb-2 text-body-secondary'>
								<a
									href={`/profile/${item.user_id}`}
									class='card-link link-underline-light'
								>
									by: {item.username}
								</a>
							</h6>
							<h6>Posted: {item.created}</h6>
						</div>
					)
				})}
			</div>
		</div>
	)
}

const Pagination = ({ paginator }) => {
	const { pages, page, itens, next, previous } = paginator

	const nextLink = `?page=${page + 1}`
	const previousLink = `?page=${page - 1}`

	return (
		<nav aria-label='...'>
			<ul class='pagination'>
				{previous && (
					<li class='page-item'>
						<a
							class='page-link'
							href={previousLink}
							tabindex='-1'
							aria-disabled='true'
						>
							Previous
						</a>
					</li>
				)}

				{pages.map((item) => {
					const pageLink = `?page=${item.page}`

					let active = ''
					if (item.page === page) {
						active = 'active'
					}
					return (
						<li class={`page-item ${active}`}>
							<a class='page-link' href={pageLink}>
								{item.page}
							</a>
						</li>
					)
				})}

				{next && (
					<li class='page-item'>
						<a class='page-link' href={nextLink}>
							Next
						</a>
					</li>
				)}
			</ul>
		</nav>
	)
}

const Posts = () => {
	const [posts, setPosts] = React.useState([])

	React.useEffect(() => {
		getPosts().then((data) => {
			setPosts(data)
		})
	}, [])

	const setNewPosts = (newPosts) => {
		const newData = {
			...posts,
			posts: newPosts,
		}

		setPosts(newData)
	}

	return (
		<div>
			{posts.posts ? (
				<div>
					<AllPosts posts={posts.posts} setNewPosts={setNewPosts} />
					<Pagination paginator={posts.paginator} />
				</div>
			) : (
				<div class='spinner-border text-primary' role='status'>
					<span class='visually-hidden'>Loading...</span>
				</div>
			)}
		</div>
	)
}

const App = () => {
	return (
		<div>
			<Posts />
		</div>
	)
}

ReactDOM.render(<App />, document.querySelector('#following'))
