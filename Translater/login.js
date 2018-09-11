var url = 'http://127.0.0.1:5000/';

function login(info) {
    let result = null;
    $.get(url + 'login/' + info.toString(), function (data, status) {
        result = data;
        if (result['result'] !== 'OK') {
            $('#results').text('Sorry, code is invalid, please try again');
        }
        else {
            //$('#results').text('You were successfully logged in');
            window.location='main_page.html';
            Cookies.set('key',info.toString());
        }
        return result;
    });
}