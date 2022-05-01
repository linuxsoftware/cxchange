$ ->
    $("#cxchangeForm").submit (ev) =>
        email = $("#emailAddress").val()
        fromCurrency = $("#fromCurrency").val()
        toCurrency = $("#toCurrency").val()
        $.post
            url:    "/rpc"
            data:   JSON.stringify
                        jsonrpc:  "2.0"
                        method:   "send_rate"
                        params:   [email, fromCurrency, toCurrency]
                        id:       "rpc"+Math.floor(Math.random()*100000)
            error: (err, status, thrown) ->
                 alert "ERROR: "+err+" STATUS: "+status+" "+thrown
        return false
    return
