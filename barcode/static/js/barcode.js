$(document).ready(function () {
    $('#input_barcode').keyup(function(){
        const barcode = $(this).val();
        if(barcode.length == 13){
            $('#warning').text('')
            if(check_barcode(barcode)){
                $.get(
                    'create/' + barcode + '/',
                    function(data){
                        if(data['status'] == 'ready'){
                            $('img').attr('src', '/static/img/barcode/' + barcode + '.png');
                        }
                    },
                    'json'
                )
            }
            else{
                $('#warning').text('Wrong code.');
            }
        }
        else {
            $('img').attr('src', '');
            if(barcode.length > 13){
                $('#warning').text('Code too long.');
            }
            else{
                $('#warning').text('');
            }
        }
    });
});

function check_barcode(barcode){
    const barcode_split = barcode.split('');
    let result = 0;
    let i = 1;
    for (let counter = 11; counter >= 0; counter--){
        result = result + parseInt(barcode.charAt(counter)) * (1 + (2 * (i % 2)));
        i++;
    }
    return ((10 - (result % 10)) % 10) === parseInt(barcode.charAt(12));
}