package com.fstt;

import org.springframework.boot.SpringApplication;
//import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.web.client.RestTemplate;

@SpringBootApplication
public class SmaProjectApplication {
	
	@Bean
	public RestTemplate getRestTemplate() {
	      return new RestTemplate();
	}
	
	public static void main(String[] args) {
		 new SpringApplicationBuilder(SmaProjectApplication.class).headless(false).run(args);
	}

}
