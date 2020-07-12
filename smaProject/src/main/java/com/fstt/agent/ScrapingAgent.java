package com.fstt.agent;

import java.io.Serializable;
import java.util.HashMap;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fstt.service.RestService;

import jade.core.AID;
import jade.core.Agent;
import jade.core.behaviours.Behaviour;
import jade.core.behaviours.CyclicBehaviour;
import jade.core.behaviours.ParallelBehaviour;
import jade.lang.acl.ACLMessage;
import jade.lang.acl.MessageTemplate;
import jade.lang.acl.UnreadableException;

import org.springframework.web.bind.annotation.RestController;

@RestController
@CrossOrigin("*")
public class ScrapingAgent extends Agent {
	private static final long serialVersionUID = 1L;
	@Autowired
	private RestService restService;
	boolean isterminated=false;
	
	
	public void setup() {
		System.out.println("Initialisation de l'agent :"+this.getAID().getName());
		ParallelBehaviour parallelBehaviour = new ParallelBehaviour();
	  	addBehaviour(parallelBehaviour);
	  	
	  	parallelBehaviour.addSubBehaviour(new Behaviour() {
	  		
			@Override
			public void action() {
				
			
				try {
					ACLMessage demande = new ACLMessage(ACLMessage.REQUEST);
					demande.addReceiver(new AID("PreprocessingAgent", AID.ISLOCALNAME));
					demande.setContent("Start preprocessing");
					//demande.setContentObject((Serializable)args);
					send(demande);
				} catch (Exception e) {
					e.printStackTrace();
				}	
//				ACLMessage aclMessage = receive();
//				//System.out.println(aclMessage.toString());
//				if (aclMessage!=null) {
//					System.out.println("acl message-------------"+ aclMessage.toString());
//					try {
//						HashMap<String,String> args= (HashMap<String,String>) aclMessage.getContentObject();
//						String numOfPages="2";
//								//args.get("numOfPages");
//						String csvName="springTest";
//						//args.get("csvName");
//						JsonNode result=restService.get("/api/v1/scrapNews?numOfPages=2&csvName=springTest");
//						ACLMessage demande = new ACLMessage(ACLMessage.REQUEST);
//						demande.addReceiver(new AID("PreprocessingAgent", AID.ISLOCALNAME));
//						demande.setContent("Start preprocessing");
//						demande.setContentObject((Serializable)args);
//						send(demande);
//					} catch (Exception e) {
//						e.printStackTrace();
//					}	
//					
//					}
			}
			
			@RequestMapping(value = "/startScraping", method = RequestMethod.GET)
			public String startScraping() throws JsonMappingException, JsonProcessingException{
	  			
				
				isterminated=true;
				
				System.out.println("first send");
			  	return "ok";
			}

			@Override
			public boolean done() {
				// TODO Auto-generated method stub
				return isterminated;
			}
			
			
			
			
					 
	  	});
	}
	
	

	

}
