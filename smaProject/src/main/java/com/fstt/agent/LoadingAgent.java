package com.fstt.agent;

import java.io.Serializable;
import java.util.HashMap;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RestController;

import com.fasterxml.jackson.databind.JsonNode;
import com.fstt.service.RestService;

import jade.core.AID;
import jade.core.Agent;
import jade.core.behaviours.Behaviour;
import jade.core.behaviours.CyclicBehaviour;
import jade.core.behaviours.ParallelBehaviour;
import jade.lang.acl.ACLMessage;

@RestController 
@CrossOrigin("*")
public class LoadingAgent extends Agent {
	private static final long serialVersionUID = 1L;
	@Autowired
	private RestService restService;

	@Override
	public void setup() {
		System.out.println("Initialisation de l'agent :"+this.getAID().getName());
		ParallelBehaviour parallelBehaviour = new ParallelBehaviour();
	  	addBehaviour(parallelBehaviour);
	  	parallelBehaviour.addSubBehaviour(new CyclicBehaviour() {
			
			
			@Override
			public void action() {
//				ACLMessage aclMessage = receive();
//				if (aclMessage!=null) {
//					try {
//						HashMap<String,String> args= (HashMap<String,String>) aclMessage.getContentObject();
//						//String csvName=args.get("csvName");
//						String csvName="springTest";
//						JsonNode result=restService.get("/api/v1/loadToDB?csvName="+csvName);
//						ACLMessage demande = new ACLMessage(ACLMessage.INFORM);
//						demande.addReceiver(new AID("SentimentAnalyzerAgent", AID.ISLOCALNAME));
//						demande.setContent("Start loading");
//						send(demande);
//					} catch (Exception e) {
//						e.printStackTrace();
//					}	
//					
//					}
			}
					 
	  	});
	}
	

}
