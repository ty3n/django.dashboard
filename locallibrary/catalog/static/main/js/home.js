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
            // type: 'post',
            // data: {time:$('[name="time"]').val()},
            success: function (e) {
                if (JSON.stringify(d) !== JSON.stringify(Object.values(e.chartpass))) {
                    updateData(myChart,e.chartlabel,e.chartpass,e.chartfail)
                    d = Object.values(e.chartpass)
                }
                // updateData(myChart,e.chartlabel,e.chartpass,e.chartfail)
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

    function objectsAreSame(x, y) {
       var objectsAreSame = true;
       for(var propertyName in x) {
          if(x[propertyName] !== y[propertyName]) {
             objectsAreSame = false;
             break;
          }
       }
       return objectsAreSame;
    }

    function colorize(opaque) {
      return (ctx) => {
        if (!(opaque)) {        
            var v = ctx.parsed.y;
            var c = v > 5000 ? '#D60000'
              : v > 500 ? '#F46300'
              : v > 50 ? '#0358B6'
              : '#44DE28';
            return c
        } else {
            var c = v < 5000 ? '#D60000'
              : v < 500 ? '#F46300'
              : v < 50 ? '#0358B6'
              : '#13ad6b';
            return c
        }
      };
    }

    function updateData(chart, label, pc, fc) {
        console.log(label)
        chart.data = {
            // labels:  Object.keys(data),
            labels: label,
            datasets: [
                {
                    label: 'PASS',
                    // data: Object.values(data),
                    data: pc,
                    backgroundColor: colorize(true),
                    borderColor: colorize(true),
                borderWidth: 1
                },
                {
                    label: 'FAIL',
                    // data: Object.values(data),
                    data: fc,
                    backgroundColor: colorize(false),
                    borderColor: colorize(false),
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
        // console.log(data)
        for (element in data){
            // console.log(data[element])
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

