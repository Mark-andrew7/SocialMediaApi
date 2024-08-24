// view_profile.js

function likePost(postId) {
  var url = likePostUrl.replace('0', postId);
  
  $.ajax({
      url: url,
      method: "POST",
      headers: {
          'X-CSRFToken': csrfToken  // CSRF token should be sent in headers
      },
      success: function(response) {
          $('.post[data-post-id="' + postId + '"] .like-count').text(response.likes);
      },
      error: function(xhr, status, error) {
          console.error('Error liking post:', error);
      }
  });
}

function toggleCommentSection(postId) {
  $('#comments-section-' + postId).toggle();
}

function addComment(event, postId) {
  event.preventDefault();
  var commentContent = $('#comment-input-' + postId).val();
  if (commentContent.trim()) {
      $.ajax({
          url: addCommentUrl,  // This uses the URL defined in the HTML file
          method: "POST",
          data: {
              post_id: postId,
              content: commentContent,
              csrfmiddlewaretoken: csrfToken  // This uses the CSRF token defined in the HTML file
          },
          success: function(response) {
              var commentHtml = '<p>' + response.username + ': ' + response.content + '</p>';
              $('#comments-section-' + postId + ' .comments-list').append(commentHtml);
              $('#comment-input-' + postId).val('');  // Clear the input field
          }
      });
  }
}
