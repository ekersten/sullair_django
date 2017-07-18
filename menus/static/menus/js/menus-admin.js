(function($) {
    $(document).ready(function() {
        if ($('#id_content_type').length > 0) {
            $('#id_content_type').on('change', function(e) {
                console.log(e.currentTarget.value);
            });
        }
    });
})(jQuery);