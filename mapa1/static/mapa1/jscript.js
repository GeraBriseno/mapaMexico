let popChart;
let pibChart;
let denChart;

window.addEventListener("load", function() {

    var mapa = document.getElementById('svg-object').contentDocument;
    var texto_nombre_estado = document.getElementById("titulo");
    var estados = mapa.querySelectorAll("path");
    var b_pop = document.getElementById("boton-pop");
    var b_pib = document.getElementById("boton-pib");

    var received_data_pop = JSON.parse(document.getElementById("datospop").innerHTML);
    var received_data_pib = JSON.parse(document.getElementById("datospib").innerHTML);

    var color1 = "#88bb88";
    var color2 = '#004400';
    var colorg1 = '#2EB62C';
    var colorg2 = '#57C84D';
    var colorg3 = '#83D475';
    var colorg4 = '#ABE098';
    var colorg5 = '#C5E8B7';

    estados.forEach(element => {

        element.addEventListener("click", function(){

            estados.forEach(element => {
                element.style.fill = color1;
            });

            element.style.fill = color2;
            texto_nombre_estado.innerHTML = element.id;

            document.getElementById("escudo").src="static/mapa1/escudos/"+element.id+".jpg"

            //Charts code

            //var received_data_pop = JSON.parse(document.getElementById("datospop").innerHTML);
            //var received_data_pib = JSON.parse(document.getElementById("datospib").innerHTML);

            var datospop = received_data_pop[element.id];
            //var datospop = datospop_r.map(function (x) { 
                //return parseInt(x.replace(/\s/g, '')); 
            //});
            var datospib = received_data_pib[element.id];
            const labelspop = ['1910','1920','1930','1940','1950','1960','1970','1980','1990','2000','2010','2020'];
            const labelspib = ["2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"];
            
            const datapop = {
                labels: labelspop,
                datasets: [{
                    label: "Población 1910-2020",
                    backgroundColor: 'rgb(70, 164, 111)',
                    borderColor: 'rgb(70, 164, 111)',
                    data: datospop,
                }]
            };
            const datapib = {
                labels: labelspib,
                datasets:[{
                    label: "PIB 2003-2020 (Millones de Pesos)",
                    backgroundColor: 'rgb(70, 164, 111)',
                    borderColor: 'rgb(70, 164, 111)',
                    data: datospib,
                }]
            };
            
            const config = {
                type: 'line',
                data: datapop,
                options:{ 
                    scales:{
                        x:{
                            ticks:{
                                autoSkip:false,
                                offset:true,
                                fontSize:2,
                            }
                        }
                    }                   
                }
            };
            const configPib = {
                type: 'line',
                data: datapib,
                options:{ 
                    scales:{
                        x:{
                            ticks:{
                                autoSkip:false,
                                offset:true,
                                fontSize:2,
                            }
                        }
                    }                   
                }
            };

            if (popChart) {
                popChart.destroy();
            };
            popChart = new Chart(
                document.getElementById('popChart'),
                config
                );

            if (pibChart) {
                pibChart.destroy();
            };
            pibChart = new Chart(
                document.getElementById('pibChart'),
                configPib
                );

            //Charts code

            });

        });

    b_pop.onclick = function(){
        
        estados.forEach(element => {

            poblacion = received_data_pop[element.id][11]//.replace(/\s/g, '');
            
            if(poblacion > 6000000){
                element.style.fill = colorg1;
            }
            else if(3700000 < poblacion && poblacion < 6000000){
                element.style.fill = colorg2;
            }
            else if(2900000 < poblacion && poblacion < 3700000){
                element.style.fill = colorg3;
            }
            else if(1800000 < poblacion && poblacion < 2900000){
                element.style.fill = colorg4;
            }
            else{
                element.style.fill = colorg5;
            }
            
        });
        
    }

    b_pib.onclick = function(){

        estados.forEach(element => {
            pib = received_data_pib[element.id][11];

            if(pib > 650000){
                element.style.fill = colorg1;
            }
            else if(470000 < pib && pib < 650000){
                element.style.fill = colorg2;
            }
            else if(243000 < pib && pib < 470000){
                element.style.fill = colorg3;
            }
            else if(189000 < pib && pib < 243000){
                element.style.fill = colorg4;
            }
            else{
                element.style.fill = colorg5;
            }
        })
    }
});