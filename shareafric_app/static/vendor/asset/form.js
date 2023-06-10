$(document).on('submit', '#form', function(e){
    e.preventDefault();
    $.ajax(
        {
            type: 'POST',
            url: "{% url 'mobil:contact' %}",
            data:{
                name:$('#name').val(),
                email:$('#email').val(),
                message:$('#message').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function(data){
                alert(data);
            }
        }
    )
})
