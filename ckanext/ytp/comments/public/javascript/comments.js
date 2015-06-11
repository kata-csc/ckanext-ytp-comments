function ShowCommentForm(id){
    var current = $("#" + id);

    // close all other open 'togglable' forms, except the currently clicked
    $(".togglable").not(current).addClass('hidden');

    // click the current form link to toggle visibility
    current.toggleClass('hidden');
}
