package com.fstt.agent;

import java.util.HashMap;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RestController;

import com.fasterxml.jackson.databind.JsonNode;

import jade.core.AID;
import jade.core.Agent;
import jade.core.behaviours.CyclicBehaviour;
import jade.core.behaviours.ParallelBehaviour;
import jade.lang.acl.ACLMessage;
import jade.lang.acl.UnreadableException;

@RestController
@CrossOrigin("*")
public class DataVisualizationAgent extends Agent{
	private static final long serialVersionUID = 1L;

	@Override
	public void setup() {
		System.out.println("Initialisation de l'agent :"+this.getAID().getName());
		ParallelBehaviour parallelBehaviour = new ParallelBehaviour();
	  	addBehaviour(parallelBehaviour);
	  	parallelBehaviour.addSubBehaviour(new CyclicBehaviour() {
			
			
			@Override
			public void action() {
				ACLMessage aclMessage = receive();
				if (aclMessage!=null) {
					
//					System.out.println("inside99999999999999999999 ");
//					HashMap<String, String> args;
//					try {
//						args = (HashMap<String,String>) aclMessage.getContentObject();
//						System.out.println("args received: "+args);
//					} catch (UnreadableException e) {
//						// TODO Auto-generated catch block
//						e.printStackTrace();
//					}
					
				}
						
					
					}
			});
	}

}
