$(document).ready(function(){
    // Fetches the videos in JSON format from '/videos' URL and loops over them
    $.getJSON('/videos', function(videos) {
        $.each(videos, function(i, video) {
            // Appends a HTML paragraph containing each video link to the 'video_links' element
            $('#video_links').append('<p><a href="/video/' + video.id + '">' + video.title + '</a></p>');
        });
    });

    // Fetches the categories in JSON format from '/categories' URL and loops over them
    $.getJSON('/categories', function(categories) {
        $.each(categories, function(i, category) {
            // Appends an HTML list item containing each category link to the 'categoriesDropdown' element
            $('#categoriesDropdown').append('<li><a href="/category/' + category + '">' + category + '</a></li>');
        });
    });

    // Fetches the channels in JSON format from '/channels' URL and loops over them
    $.getJSON('/channels', function(channels) {
        $.each(channels, function(i, channel) {
            // Appends an HTML list item containing each channel link to the 'channelsDropdown' element
            $('#channelsDropdown').append('<li><a href="/channel/' + channel + '">' + channel + '</a></li>');
        });
    });

    // Setup a timer
    var delayTimer;

    $('#search-input').on('input', function() {
        var search_term = $(this).val();

        // Clear the existing timer
        clearTimeout(delayTimer);

        // Set a new timer
        delayTimer = setTimeout(function() {
            $.getJSON('/search', { 'q': search_term }, function(videos) {
                // Clear current results
                $('#search-results').empty();
                // Add new results
                $.each(videos, function(i, video) {
                    $('#search-results').append('<li><a href="/video/' + video[0] + '">' + video[1] + '</a></li>');
                });
            });
        }, 250); // Will do the AJAX stuff after 250 ms, or 1/4 s
    });
});