let request = new XMLHttpRequest

request.open('GET', 'http://127.0.0.1:5000/reddit/positive?keyword=bitcoin', true);
request.onload = function () {
    let data = JSON.parse(this.response);
    console.log(data);
}

request.send();