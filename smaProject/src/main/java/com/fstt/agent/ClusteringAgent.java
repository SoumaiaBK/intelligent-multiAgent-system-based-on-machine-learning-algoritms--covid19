package com.fstt.agent;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RestController;

import jade.core.Agent;

@RestController
@CrossOrigin("*")
public class ClusteringAgent extends Agent{
	private static final long serialVersionUID = 1L;

	@Override
	public void setup() {
		System.out.println("Initialisation de l'agent :"+this.getAID().getName());
	}
	
	

}
