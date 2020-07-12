package com.fstt.container;

import org.springframework.stereotype.Service;

import jade.core.Profile;
import jade.core.ProfileImpl;
import jade.core.Runtime;
import jade.wrapper.AgentContainer;
import jade.wrapper.AgentController;
import jade.wrapper.ContainerController;
import jade.wrapper.StaleProxyException;


public class ScrapingContainer {

	public ScrapingContainer() {
		try {
			// TODO Auto-generated method stub
			Runtime runtime = Runtime.instance();
			Profile profile = new ProfileImpl(false);
			profile.setParameter(Profile.MAIN_HOST, "localhost");
			AgentContainer agentContainer = runtime.createAgentContainer(profile); 
			AgentController agentController = agentContainer.createNewAgent("ScrapingAgent", "com.fstt.agent.ScrapingAgent", new Object[] {});
			AgentController agentController1 = agentContainer.createNewAgent("PreprocessingAgent", "com.fstt.agent.PreprocessingAgent", new Object[] {});
			AgentController agentController2 = agentContainer.createNewAgent("LoadingAgent", "com.fstt.agent.LoadingAgent", new Object[] {});
			AgentController agentController3 = agentContainer.createNewAgent("SentimentAnalyzerAgent", "com.fstt.agent.SentimentAnalyzerAgent", new Object[] {});

			agentController.start();	
			agentController1.start();
			agentController2.start();
			agentController3.start();
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
	}
}

