console.log($('#id_is_employer'))
    $('#id_is_employer').addClass('form-check-input');
    $('#id_avatar').addClass('form-control')
    $('#id_is_employer').click(function(){
        if ($(this).is(':checked')){
            $('strong')[2].innerText = 'Наименование компании:*'
        } else {
            $('strong')[2].innerText = 'Имя:*'
        }
    });    