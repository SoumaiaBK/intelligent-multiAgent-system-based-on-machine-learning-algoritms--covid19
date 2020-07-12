import { Component, OnInit } from '@angular/core';
import {Chart} from 'node_modules/chart.js'
import { MyService } from '../services/MyService';


@Component({
  selector: 'app-main-container',
  templateUrl: './main-container.component.html',
  styleUrls: ['./main-container.component.css','./Scrapping.css']
})
export class MainContainerComponent implements OnInit {

  isPositive:string="n"; 
  numberNews:number=0; 
  number:string; 
  numberPages: number=0;

  stat :any;
  dataNews:any;
  dataClustes:any;
  dataPrediction:any;

  data1 : any ;
  data2 : any ;
  data3 : any ;
  
  selector:string = "Visualisation";

  nDeaths:number=0;
  nCured:number=0;
  nCases:number=0;

  msg : any;
  constructor( private service :MyService) { }

  ngOnInit() {
    this.getData();
    
    setTimeout(()=>{ 
      this.graphe();
    }, 2000);
  } 

  setPositiveValue(e){
    if(e.checked){
      this.isPositive="p";
    }else{
      this.isPositive="n";
    }
  }
  setNewsNumber(e){
    this.numberNews = e.value;
    this.number = e.value;
  }


 

  statAnalysis(){
    this.service.statAnalysis().subscribe(data => {
      console.log(data);  
      this.stat=data;
    });
    }
    setPagesNumber(e){
      this.numberPages = e.value;
    }
  scrapping_news(){
    this.service.scrapping_news(this.numberPages).subscribe(data => {
      console.log(data);  
      this.msg=data;
    });
    console.log("scrapping_news");  

  }
  getNews(){
    this.service.getNews(this.number,this.isPositive).subscribe(data => {
      console.log(data);  
      this.dataNews=data;
    });
    }
  ChangeSelector(msg:string){
    this.selector = msg;
    setTimeout(()=>{   
      this.graphe();
    }, 2000);
  }

  getData(){
    this.service.getGraphe1().subscribe(data => {
      console.log(data);  
      this.data1=data;
    });
    this.service.getGraphe2().subscribe(data => {
      console.log(data);  
      this.data2=data;
   });
   this.service.getGraphe3().subscribe(data => {
    console.log(data);  
    this.data3=data;
  });
  this.service.prediction().subscribe(data => {
    console.log(data);  
    this.dataPrediction=data;
  });
  this.service.GetClusters().subscribe(data => {
    console.log(data);  
    this.dataClustes=data;
  });
  
    
  }

  graphe(){
    this.CalculCases();

    this.Clusters();
    this.DataVisualisation();
    this.prediction();
  }

  CalculCases(){
    this.nDeaths=0;
    this.nCured=0;
    this.nCases=0;
    this.data1.Deaths.forEach(element => {
      this.nDeaths = this.nDeaths + element;
    });
    this.data1.Confirmed.forEach(element => {
      this.nCases = this.nCases+ element;
    });
    this.data1.Recovered.forEach(element => {
      this.nCured = this.nCured + element;
    });
    console.log(this.nDeaths,this.nCases,this.nCured);
  }

  
  DataVisualisation (){
    // graphe 1
    var myChart1 = new Chart("myChart1", {
      type: 'bar',
      data: {
          labels:   this.data1.regions,
          datasets: [
            {
              label: 'Nombre de décès',
              data: this.data1.Deaths,
              backgroundColor: "#DB3F29",
              fill: false,
              pointRadius:0,
              pointHitRadius: 0,
              borderWidth: 2,
              borderColor : "#ccc"
          }
          ,
            {
              label: 'Nombre de cas',
              data: this.data1.Confirmed,
              backgroundColor:"#D7A449",
              pointRadius:0,
              pointHitRadius: 0,
              borderWidth: 2,
              fill: false,
              borderColor: "#ccc"
          }
          ,      
        {
          label: 'Nombre de guéris',
          data: this.data1.Recovered,
          backgroundColor: '#33ff77',
          fill: false,
          pointRadius:0,
          pointHitRadius: 0,
          borderWidth: 2,
          borderColor : "#ccc"         
      }]
    },
      options: {
        title: {
          display: true,
          text: "Les cas en Maroc"
        }
      }
    });
    // graphe 22
    var myChart22 = new Chart("myChart22", {
      type: 'line',
      data: {
          labels:   this.data1.regions,
          datasets: [{
              label: '# Nombre de cas ',
              data: this.data1.Confirmed,
              backgroundColor: '#D7A449',
              fill: true,
    
            borderWidth: 2,
            borderColor : '#8B0000'
          }]
      },
      options: {
        title: {
          display: true,
          text: "Les cas en Maroc selon les régions"
        }
      }
    });
    // graphe2
    var myChart2 = new Chart("myChart2", {
      type: 'line',
      data: {
          labels:   this.data2.jours,
          datasets: [{
              label: '# nbre des cas ',
              data: this.data2.cas,
              pointRadius:0,
              pointHitRadius: 0,
              borderWidth: 2,
              fill: false,
              borderColor: 'red'
          },
          {
            label: '# nbre de déces ',
            data: this.data2.deces,
            fill: false,
            pointRadius:0,
            pointHitRadius: 0,
            borderWidth: 2,
            borderColor : '#8B0000'
            
        }
        
        ]
      },
      options: {
        title: {
          display: true,
          text: "Les cas en Maroc selon les jours"
        }
      }
    });
  // graphe3
    var myChart3 = new Chart("myChart3", {
      type: 'line',
      data: {
        labels:   this.data3.pays,
        datasets: [{
          label: '# Nombre de cas ',
          fill: false,
          lineTension: 0,
          data: this.data3.cas,
            pointRadius:0,
            pointHitRadius: 0,
            borderWidth: 2,
            borderColor : '#0d0d6c'
        },
      {
        label: '# Nombre de décès ',
        fill: false,
        lineTension: 0,
        data: this.data3.deces,
        pointRadius:0,
        pointHitRadius: 0,
        borderWidth: 2,
        borderColor : '#c21020'
      }
      ]
      },
      options: {
        title: {
          display: true,
          text: "Selon les pays"
        }
      }
    });
  // grpahe4 :%
    var myChart4 = new Chart("myChart4", {
      type: 'pie',
      data: {
        labels: ["Nombre de décès", "Nombre de guéris", "Nombre de cas"],
        datasets: [{
          backgroundColor: ["#DB3F29", "#1DC690","#D7A449"],
          data: [this.nDeaths, this.nCured, this.nCases]
        }]
      },
      options: {
        title: {
          display: true,
          text: "Les cas en Maroc"
        }
      }
  });
  
  }

  prediction(){
    var prediction = new Chart("prediction", {
      type: 'line',
      data: {
          labels:   this.dataPrediction.day,
          datasets: [{
              label: '# Le nombre de cas ',
              data: this.dataPrediction.predicted,
              backgroundColor: '#F5F5F5',
              borderColor : '##FF0000'
              
          }]
      },
      
  });

  }
  StatScraping(){
    var stat = new Chart("stat", {
      type: 'pie',
      data: {
        labels: ["Positive", "Négative"],
        datasets: [{
          backgroundColor: ["#DB3F29", "#1DC690","#D7A449"],
          data: [this.stat.positive, this.stat.negative]
        }]
      },
      options: {
        title: {
          display: true,
          text: "Statistiques sur l'analyse des sentiments "
        }
      }
  });
  }
  Clusters(){
    var clusters = new Chart("Clusters",{
      type: 'bubble',
      data: {
        datasets: [
          {
            label: ["CasablancaSettat"],
            backgroundColor: "#fe0a0a",
            borderColor: "#fe0a0a",
            data: [{
              x: 3979083,
              y: 6.994,
              r: 30
            }]
          },
          {
            label: ["FesMeknes - MarrakeshSafi - RabatSaleKenitra - TangerTetouanAlHoceima"],
            backgroundColor: "#362da6",
            borderColor: "#362da6",
            data: [{
              x: 21269017,
              y: 5.245,
              r: 25
            }]
          },{
            label: ["BeniMellalKhenifra - DraaTafilalet - DakhlaOuedEdDahab - GuelmimOuedNoun - LaayouneSakiaEl Hamra - Oriental - SoussMassa"],
            backgroundColor: "#3a701f",
            borderColor: "#3a701f",
            data: [{
              x: 258702,
              y: 7.526,
              r: 20
            }]
          }]
      }
    });
  }
}
