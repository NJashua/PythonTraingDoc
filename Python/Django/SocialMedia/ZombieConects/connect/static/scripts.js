function likePost(postId) {
    $.ajax({
        type: 'POST',
        url: '{% url "like_post" %}',
        data: {
            'post_id': postId,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function(data) {
            console.log(data);
            // Update the like count on the page
            $('#post-' + postId + ' .like-count').text(data.likes);
        }
    });
}

function followUser(username) {
    $.ajax({
        type: 'POST',
        url: '{% url "follow_user" %}',
        data: {
            'username': username,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function(data) {
            console.log(data);
            // Update the follow button text on the page
            $('#follow-btn-' + username).text(data.button_text);
        }
    });
}