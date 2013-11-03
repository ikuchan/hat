jQuery(function($){
	$('.js-open-tags').click(function(){
		$.getJSON('/tags', function(tags){
			$('.js-tags').empty();
			
			var $list = $('<ul>');
			for (var i = 0; i < tags.length; i++) {
				var $tag = $('<li>').append($('<a class="off" href="#">').text(tags[i]));
				$tag.find('a').click(function(){
					if ($(this).hasClass('off')) {
						$(this).removeClass('off').addClass('on');
					} else {
						$(this).removeClass('on').addClass('off');
					}
					return false;
				});
				$list.append($tag);
			}

			$('.js-tags').append($list);
		});
		return false;
	});

	$('.js-search').click(function(){
		$.getJSON('/get', function(response){
			for (var i = 0; i < response.length; i++) {
				var row = response[i];
				var $template = $($('.js-row-template').html());

				$template.find('.js-client dd').text(row.client_name + 'さん')

				$('#result').append($template);
			}
		});
		return false;
	});

});