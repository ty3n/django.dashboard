$(document).ready( function() {
    var ctx = document.getElementById('myChart');
    var d = []
    var endpoint = '/api/chart/data';
    var myChart = new Chart(ctx,{
            labels: [],
            type: 'bar',
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    setInterval(function () {
        $.ajax({
            url: endpoint,
            success: function (e) {
        //      if (JSON.stringify(d) !== JSON.stringify(Object.values(data))) {
                    // updateData(myChart,data)
                    // d = Object.values(data)
        //      }
                // console.log(typeOf(e.data))
                var recData = JSON.parse(e.data)
                // tableBodyData[recData['indexName']]['currentVal']=recData['value']
                // console.log(tableBodyData[recData['indexName']]['currentVal'])
                tableContent=document.getElementById("customers")
                tableContent.innerHTML = ""
                createHeader(tableContent,e.tableheader)
                createtableBody(tableContent,recData) 
            },
            error: function (err) {
                console.log('error');   
            }
        })
    },1000)

    function getRandomInt(max) {
      return Math.floor(Math.random() * max);
    }

    function updateData(chart, data) {
        chart.data = {
            labels:  Object.keys(data),
            // labels: [],
            datasets: [
                {
                    label: 'Update Counts',
                    data: Object.values(data),
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                borderWidth: 1
                }
            ]
        };
        chart.update();
    };

    // let tableheader = {tableheader};
    // let tableBodyData= {data};

    function createHeader(table,headervalues){
        let tHead = table.createTHead();
        let trow = tHead.insertRow();
        for (val in headervalues){
            // console.log(headervalues[val]);
            let th =document.createElement('th');
            let text = document.createTextNode(headervalues[val]);
            th.appendChild(text);
            trow.appendChild(th);
        }
    }

    function createtableBody(table,data){
        console.log(data)
        for (element in data){
            console.log(data[element])
            let row = table.insertRow();
            for (key in data[element]){
                let cell = row.insertCell();
                let text = document.createTextNode(data[element][key]);
                cell.appendChild(text);
            }
        }
    }
    // var tableContent = document.getElementById('customers');
    // createHeader(tableContent,tableheader);
    // createtableBody(tableContent,tableBodyData);
})

