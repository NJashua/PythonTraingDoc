// Like button functionality
document.addEventListener('DOMContentLoaded', function() {
    const likeButtons = document.querySelectorAll('.like-btn');
    likeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const postId = button.dataset.postId;
            fetch(`/like/${postId}`, {
                method: 'PUT',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}'
                }
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // Update like count
                const likeCount = document.querySelector(`#like-count-${postId}`);
                likeCount.textContent = `Likes: ${data.likes}`;
            })
            .catch(error => console.error(error));
        });
    });
});

// Save button functionality
document.addEventListener('DOMContentLoaded', function() {
    const saveButtons = document.querySelectorAll('.save-btn');
    saveButtons.forEach(button => {
        button.addEventListener('click', function() {
            const postId = button.dataset.postId;
            fetch(`/save/${postId}`, {
                method: 'PUT',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}'
                }
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // Update save count
                const saveCount = document.querySelector(`#save-count-${postId}`);
                saveCount.textContent = `Saves: ${data.saves}`;
            })
            .catch(error => console.error(error));
        });
    });
});

// Comment button functionality
document.addEventListener('DOMContentLoaded', function() {
    const commentButtons = document.querySelectorAll('.comment-btn');
    commentButtons.forEach(button => {
        button.addEventListener('click', function() {
            const postId = button.dataset.postId;
            const commentInput = document.querySelector(`#comment-input-${postId}`);
           // Like button functionality
document.addEventListener('DOMContentLoaded', function() {
    const likeButtons = document.querySelectorAll('.like-btn');
    likeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const postId = button.dataset.postId;
            fetch(`/like/${postId}`, {
                method: 'PUT',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}'
                }
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // Update like count
                const likeCount = document.querySelector(`#like-count-${postId}`);
                likeCount.textContent = `Likes: ${data.likes}`;
            })
            .catch(error => console.error(error));
        });
    });
});

// Save button functionality
document.addEventListener('DOMContentLoaded', function() {
    const saveButtons = document.querySelectorAll('.save-btn');
    saveButtons.forEach(button => {
        button.addEventListener('click', function() {
            const postId = button.dataset.postId;
            fetch(`/save/${postId}`, {
                method: 'PUT',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}'
                }
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // Update save count
                const saveCount = document.querySelector(`#save-count-${postId}`);
                saveCount.textContent = `Saves: ${data.saves}`;
            })
            .catch(error => console.error(error));
        });
    });
});

// Comment button functionality
document.addEventListener('DOMContentLoaded', function() {
    const commentButtons = document.querySelectorAll('.comment-btn');
    commentButtons.forEach(button => {
        button.addEventListener('click', function() {
            const postId = button.dataset.postId;
            const commentInput = document.querySelector(`#comment-input-${postId}`);
            const commentContent = commentInput.value;
            fetch(`/comment/${postId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': '{{ csrf_token }}'
                },
                body: JSON.stringify({ comment_text: commentContent })
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // Add new comment to the page
                const commentsContainer = document.querySelector(`#comments-container-${postId}`);
                const newComment = document.createElement('div');
                newComment.classList.add('comment');
                newComment.innerHTML = `
                    <p>${data.comment.comment_content}</p>
                    <p>${data.comment.comment_time.strftime("%b %d %Y, %I:%M %p")}</p>
                `;
                commentsContainer.appendChild(newComment);
                // Clear the comment input
                commentInput.value = '';
            })
            .catch(error => console.error(error));
        });
    });
});

// Follow button functionality
document.addEventListener('DOMContentLoaded', function() {
    const followButtons = document.querySelectorAll('.follow-btn');
    followButtons.forEach(button => {
        button.addEventListener('click', function() {
            const username = button.dataset.username;
            fetch(`/follow/${username}`, {
                method: 'PUT',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}'
                }
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // Update follower count
                const followerCount = document.querySelector(`#follower-count-${username}`);
                followerCount.textContent = `Followers: ${data.follower_count}`;
                // Update following count
                const followingCount = document.querySelector(`#following-count-${username}`);
                followingCount.textContent = `Following: ${data.following_count}`;
                // Change button text
                button.textContent = 'Unfollow';
                button.classList.remove('follow-btn');
                button.classList.add('unfollow-btn');
            })
            .catch(error => console.error(error));
        });
    });
});

// Unfollow button functionality
document.addEventListener('DOMContentLoaded', function() {
    const unfollowButtons = document.querySelectorAll('.unfollow-btn');
    unfollowButtons.forEach(button => {
        button.addEventListener('click', function() {
            const username = button.dataset.username;
            fetch(`/unfollow/${username}`, {
                method: 'PUT',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}'
                }
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // Update follower count
                const followerCount = document.querySelector(`#follower-count-${username}`);
                followerCount.textContent = `Followers: ${data.follower_count}`;
                // Update following count
                const followingCount = document.querySelector(`#following-count-${username}`);
                followingCount.textContent = `Following: ${data.following_count}`;
                // Change button text
                button.textContent = 'Follow';
                button.classList.remove('unfollow-btn');
                button.classList.add('follow-btn');
            })
            .catch(error => console.error(error));
        });
    });
});