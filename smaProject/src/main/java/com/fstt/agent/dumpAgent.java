package com.fstt.agent;

import jade.core.Agent;

public class dumpAgent  extends Agent{

	private static final long serialVersionUID = 1L;

	@Override
	public void setup() {
		System.out.println("Initialisation de l'agent :"+this.getAID().getName()); 
		}

}
