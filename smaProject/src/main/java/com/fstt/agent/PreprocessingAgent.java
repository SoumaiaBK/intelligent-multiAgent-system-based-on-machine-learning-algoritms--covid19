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
public class PreprocessingAgent extends Agent{
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
				ACLMessage aclMessage = receive();
				if (aclMessage!=null) {
					System.out.println("inside ++++++++++++++++++++");
//					try {
////						HashMap<String,String> args= (HashMap<String,String>) aclMessage.getContentObject();
////						String numOfPages="2";
////						//args.get("numOfPages");
////						String csvName="springTest";
////						JsonNode result=restService.get("/api/v1/preprocessing?csvName="+csvName);
////						ACLMessage demande = new ACLMessage(ACLMessage.REQUEST);
////						demande.addReceiver(new AID("LoadingAgent", AID.ISLOCALNAME));
////						demande.setContent("Start loading");
////						demande.setContentObject((Serializable)args);
////						send(demande);
//					} catch (Exception e) {
//						e.printStackTrace();
//					}	
					
					}
				//block();
			}
					 
	  	});
	}
	
	
	
}
