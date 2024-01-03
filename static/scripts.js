$(document).ready(function(){
    $.getJSON('/videos', function(videos) {
        $.each(videos, function(i, video) {
            $('#video_links').append('<p><a href="/video/' + video.id + '">' + video.title + '</a></p>');
        });
    });

    $.getJSON('/categories', function(categories) {
        $.each(categories, function(i, category) {
            $('#categoriesDropdown').append('<li><a href="/category/' + category + '">' + category + '</a></li>');
        });
    });
    
    // Fetch channels
    $.getJSON('/channels', function(channels) {
        $.each(channels, function(i, channel) {
            $('#channelsDropdown').append('<li><a href="/channel/' + channel + '">' + channel + '</a></li>');
        });
    });
});
