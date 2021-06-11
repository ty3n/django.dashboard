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
	        success: function (data) {
	        	if (JSON.stringify(d) !== JSON.stringify(Object.values(data))) {
					updateData(myChart,data)
					d = Object.values(data)
	        	}
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
	}
})
