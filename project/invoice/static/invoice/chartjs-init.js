var ctx = document.getElementById( "doughutChart" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'doughnut',
        data: {
            datasets: [ {
                data: [ 35, 40,],
                backgroundColor: [
                                    "#28a745",
                                    "#dc3545",
                                ],
                hoverBackgroundColor: [
                                    "#28a745",
                                    "#dc3545",
                                ]

                            } ],
            labels: [
                            "платено",
                            "неплатено",
                        ]
        },
        options: {
            responsive: true
        }
    } );