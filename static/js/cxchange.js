// Generated by CoffeeScript 1.10.0
(function() {
  $(function() {
    $("#cxchangeForm").submit((function(_this) {
      return function(ev) {
        var email, fromCurrency, toCurrency;
        email = $("#emailAddress").val();
        fromCurrency = $("#fromCurrency").val();
        toCurrency = $("#toCurrency").val();
        $.post({
          url: "/rpc",
          data: JSON.stringify({
            jsonrpc: "2.0",
            method: "send_rate",
            params: [email, fromCurrency, toCurrency],
            id: "rpc" + Math.floor(Math.random() * 100000)
          }),
          error: function(err, status, thrown) {
            return alert("ERROR: " + err + " STATUS: " + status + " " + thrown);
          }
        });
        return false;
      };
    })(this));
  });

}).call(this);
