var data = [];

function doStuff(arr, cb) {
    var res = [];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] % 2 == 0) {
            res.push(arr[i] * arr[i]);
        }
    }
    setTimeout(function() {
        if (res.length == 0) {
            cb('no data', null);
        } else {
            cb(null, res);
        }
    }, 1000);
}

function show(err, result) {
    if (err) {
        console.log('ERROR: ' + err);
    } else {
        for (var i = 0; i < result.length; i++) {
            console.log(result[i]);
        }
    }
}

for (var i = 1; i <= 10; i++) {
    data.push(i);
}

doStuff(data, function(err, result) {
    show(err, result);
    doStuff([100, 200, 300], function(err2, result2) {
        show(err2, result2);
    });
});
