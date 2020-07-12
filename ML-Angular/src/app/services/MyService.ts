import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { Injectable } from '@angular/core';


@Injectable({
    providedIn: 'root'
  })
export class MyService {
    url:string="http://localhost:5000"

    constructor(private httpClient: HttpClient, private router: Router) { }
//  Pour graphe 1 : selon regions / nbre des cas & deces & gueris 
    getGraphe1(){
        return this.httpClient.get(this.url+'/getGraphe1');
    }
//  pour graphe 2 : selon date / nbr des cas & nbr des deces
    getGraphe2(){
        return this.httpClient.get(this.url+'/getGraphe2');
    }
//  pour graphe 3 : selon pays / nbr des cas & nbr des deces
    getGraphe3(){
        return this.httpClient.get(this.url+'/getGraphe3');
    }

//  Pour le modèle de prédiction
    prediction(){
        return this.httpClient.get(this.url+'/prediction');
    }

//  Pour le modèle de Clustering 
    GetClusters(){
        return this.httpClient.get(this.url+'/clustering');
    }
//  Pour scrapping les nouvelles
    scrapping_news(pages: number){
        console.log("scrapping_news service");  
        return this.httpClient.get(this.url+'/scrapping_news/'+pages);

    }
//  Pour scrapping data1
    scraping_data1(){
        return this.httpClient.get(this.url+'/scraping_data1');
    }
//  Pour scrapping data2
    scraping_data2(){
        return this.httpClient.get(this.url+'/scraping_data2');
    }
// Pour get les nouvelles
    getNews(n:string,s:string){
        let data = {
          "number": n,
            "sentiment" : s
        }
        return this.httpClient.get(this.url+'/getNews/'+s+'/'+n);
      } 
// Pour les statiqtiques
    statAnalysis(){
        return this.httpClient.get(this.url+'/statAnalysis');
    }
}