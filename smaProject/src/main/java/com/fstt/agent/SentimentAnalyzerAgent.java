package com.fstt.agent;

import java.io.IOException;
import java.io.Serializable;
import java.util.HashMap;
import java.util.Map;

import javax.sound.midi.Soundbank;

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
import jade.core.behaviours.OneShotBehaviour;
import jade.core.behaviours.ParallelBehaviour;
import jade.lang.acl.ACLMessage;
import jade.lang.acl.MessageTemplate;

@RestController
@CrossOrigin("*")
public class SentimentAnalyzerAgent extends Agent {
	
	private static final long serialVersionUID = 1L;
	@Autowired
	private RestService restService;
	
	
	
	@Override
	public void setup() {
		System.out.println("Initialisation de l'agent :"+this.getAID().getName());
		setEnabledO2ACommunication(true, 0);
		ParallelBehaviour parallelBehaviour = new ParallelBehaviour();
	  	addBehaviour(parallelBehaviour);
	  	parallelBehaviour.addSubBehaviour(new CyclicBehaviour() {
					
			@Override
			public void action() {	
				
			}
	  	});
		
		
	}
	

	
	
	
	

	@RequestMapping(value = "/getNews/{sentiment}/{number}", method = RequestMethod.GET)
	public JsonNode getSentiment(@PathVariable("sentiment") String sentiment, @PathVariable("number") String number) throws JsonMappingException, JsonProcessingException{
		
		return restService.get("api/v1/getNews?number="+number+"&sentiment="+sentiment+"");
	}
	
//	@RequestMapping(value = "/startScraping/{numOfPages}/{csvName}", method = RequestMethod.GET)
//	public String startScraping(@PathVariable("numOfPages") String numOfPages, @PathVariable("csvName") String csvName) throws JsonMappingException, JsonProcessingException{
//		ACLMessage demande = new ACLMessage(ACLMessage.REQUEST);
//		demande.setContent("Start scraping");
//		
//		
//		HashMap<String, String> args=new HashMap<String, String>();
//		
//		args.put("numOfPages", numOfPages );
//		args.put("csvName", csvName);
//		System.out.println("map : "+args.toString());
//		try {
//			demande.setContentObject((Serializable) args);
//		} catch (IOException e) {
//			// TODO Auto-generated catch block
//			System.out.println("error catched***************************");
//			e.printStackTrace();
//		}
//		demande.addReceiver(new AID("PreprocessingAgent", AID.ISLOCALNAME));
//		send(demande);
//		System.out.println(demande.toString());
//
//		return "success";
//	}

}




