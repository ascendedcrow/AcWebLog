function create_comment_modal() {
    $("#comment_form").load("/comments/", function () {
        // load the url into the modal
        $("#SubmitComment").on("click", function (event) {
            document.getElementById("CommentForm").submit();
        });
    });
}