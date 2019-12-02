function downloadTemperatureDataOnClick() {
    var tokenKey = localStorage.getItem("indoor_air_token");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            const dataString = this.responseText;

            //----------------------------------------------------------------//
            // THE FOLLOWING CODE WAS MODIFIED FROM THE STACKOVERFLOW LINK:   //
            // https://stackoverflow.com/a/14966131                           //
            //----------------------------------------------------------------//

            // console.log(typeof dataString);
            var rows = dataString.split('\n');

            var processedRows = [];
            for (row of rows) {
                var cols = row.split(",");
                // console.log(cols);
                processedRows.push(cols);
            }

            let csvContent = "data:text/csv;charset=utf-8,";

            processedRows.forEach(function(rowArray) {
                let row = rowArray.join(",");
                csvContent += row + "\n";
            });

            var encodedUri = encodeURI(csvContent);
            var link = document.createElement("a");
            link.setAttribute("href", encodedUri);
            link.setAttribute("download", "my_data.csv");
            document.body.appendChild(link); // Required for FF

            link.click(); // This will download the data file named "my_data.csv"
        }
    }
    const detailURL = "{{ BACKEND_API_SERVER_ADDRESS }}/api/report/1";
    console.log(detailURL);
    xhttp.open("GET", detailURL, true);
    var tokenValue = "Token " + tokenKey;
    xhttp.setRequestHeader("Authorization", tokenValue);
    xhttp.send();
}
