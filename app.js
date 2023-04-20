$(document).ready(function() {
    // Read the JSON data
    $.getJSON("data.json", function(data) {
      // Create the dropdown menu options
      var options = $("#select-firm");
      $.each(data.firms, function(key, value) {
        options.append($("<option />").val(key).text(value.Standard));
      });
  
      // Display the data based on the selected firm
      $("#select-firm").change(function() {
        var selected = $(this).val();
        if (selected === "") {
          $("#data-table tbody").empty();
          return;
        }
        var row = $("<tr />");
        var value = data.firms[selected];
        $.each(value, function(key, value) {
          row.append($("<td />").text(value));
        });
        $("#data-table tbody").empty().append(row);
      });
    });
  });
  