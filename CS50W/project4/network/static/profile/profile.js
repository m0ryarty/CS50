const getPosts = async (id) => {
	const response = await fetch(`/user_profile/${id}`, {
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

const redirect = (link) => {
	window.location.href = link
}

const EditPost = ({ toggleEdit, postId, post, setNewPosts }) => {
	const handleSubmit = (e) => {
		e.preventDefault()
		const form = e.target

		const formData = new FormData(form)

		formData.append('postId', postId)

		fetch('/edit', { method: 'POST', body: formData })
			.then((response) => response.json())
			.then((data) => setNewPosts(data))

		toggleEdit('')
	}

	return (
		<div>
			{
				<form method='post' onSubmit={handleSubmit} class='mt-3'>
					<CSRFToken />
					<div class='card'>
						<div class='card-body'>
							<h5
								onClick={() => {
									toggleEdit('')
								}}
							>
								<span>
									<i class='bi bi-pen'></i>
								</span>
								Edit Post
							</h5>

							<textarea
								autoFocus
								name='edit'
								class='form-control'
								id='edit-text'
								rows='10'
							>
								{post}
							</textarea>
						</div>
						<input type='submit' class='btn btn-light' value='Save' />
					</div>
				</form>
			}
		</div>
	)
}

const UpperBar = ({ data, follow }) => {
	const toggleFollow = (e) => {
		e.preventDefault()
		const form = e.target
		const formData = new FormData(form)

		fetch(`/profile/${data.profile}`, {
			method: 'POST',
			body: formData,
		})

		redirect('/following')
	}

	return (
		<div class='d-flex flex-row justify-content-between align-items-baseline mb-3 mt-3 bg-light'>
			<span class='d-flex flex-row'>
				<i class='bi bi-text-indent-left'></i>
				<h5>{data.username}'s Posts</h5>
			</span>
			{data.userId === data.profile ? (
				<span class='d-flex flex-row g-3'>
					<div class='me-4'>Folowing: {follow.following}</div>
					<div class='me-4'>Folowers: {follow.follower}</div>
				</span>
			) : (
				<span class='d-flex flex-row'>
					<form method='post' onSubmit={toggleFollow} class='mt-3'>
						<CSRFToken />
						<div name='userId' value={data.userId}></div>
						<button type='submit' class='btn'>
							<h5>
								{data.follow ? (
									<i class='bi bi-person-dash'></i>
								) : (
									<i class='bi bi-person-add'></i>
								)}
							</h5>
						</button>
					</form>
				</span>
			)}
		</div>
	)
}

const Like = ({ like, numberLikes, userId, postUser, postId, updateLike }) => {
	const handleLike = (e) => {
		e.preventDefault()
		if (postUser != userId) {
			const form = e.target

			const formData = new FormData(form)
			formData.append('likeUser', userId)
			formData.append('likePost', postId)

			fetch('/like', { method: 'POST', body: formData })
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

const AllProfilePosts = ({ profileData, setNewPosts }) => {
	const [toggle, setToggle] = React.useState('')

	const toggleEditPost = (id) => {
		setToggle(id)
	}

	const updateLike = (id) => {
		const newPosts = profileData.map((item) => {
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
			{profileData.map((item) => {
				const lines = item.post.split('\n')
				return toggle === item.id ? (
					<EditPost
						toggleEdit={(id) => {
							toggleEditPost(id)
						}}
						post={item.post}
						postId={item.id}
						setNewPosts={setNewPosts}
					/>
				) : (
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
						<div class='d-flex justify-content-between'>
							<h6>Posted: {item.created}</h6>
							{item.user_id == item.loggedUser && (
								<button
									onClick={() => {
										toggleEditPost(item.id)
									}}
									type='button'
									class='btn btn-light btn-sm'
								>
									Edit
								</button>
							)}
						</div>
					</div>
				)
			})}
		</div>
	)
}

const Pagination = ({ pageData }) => {
	const { itens, next, page, pages, previous } = pageData

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

const Profile = ({ profile_data }) => {
	const [profilePosts, setProfilePosts] = React.useState([])

	const data = JSON.parse(profile_data)

	React.useEffect(() => {
		getPosts(data.profile).then((data) => {
			setProfilePosts(data)
		})
	}, [])

	const setNewPosts = (newPosts) => {
		const newData = {
			...profilePosts,
			profileData: newPosts,
		}

		setProfilePosts(newData)
	}

	return (
		<div>
			{profilePosts.profileData ? (
				<div>
					<UpperBar data={data} follow={profilePosts.follow} />
					<AllProfilePosts
						profileData={profilePosts.profileData}
						setNewPosts={setNewPosts}
					/>

					<Pagination pageData={profilePosts.paginator} />
				</div>
			) : (
				<div class='spinner-border text-primary' role='status'>
					<span class='visually-hidden'>Loading...</span>
				</div>
			)}
		</div>
	)
}

const App = ({ profile_data }) => {
	return (
		<div>
			<Profile profile_data={profile_data} />
		</div>
	)
}

ReactDOM.render(
	<App
		profile_data={
			document.querySelector('#profile').attributes.profile_data.value
		}
	/>,
	document.querySelector('#profile')
)
