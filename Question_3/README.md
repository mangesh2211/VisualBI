# Architecture model
## 1.Explain the architecture model
```
This architecture uses CDN with load balancer. It is very resilent or I would say critical application.

1. what is CDN?
A content delivery network refers to a geographically distributed group of servers which work together to provide fast delivery internet content. CDN caches frequently accessed data 
and distributes to user in fraction of seconds.
2. what is load balancer?
Users send mltiple requests in seconds to acces the data that is there on the server. so it is always a good practice to distribute the incoming request load among the servers.
load balancer does this work. there are different algorithms like round-robin about how you want to distribute the load among the servers.

3. our architecture uses a CDN which constitutes regions such as US,EU,CA,ME,AP. requests from the CDN servers are distributed across Load balancer 1 and Load balancer 2. 
these Load Balancers are attched to our application service. this service is at the same deployment version on both the load balancers

```

## 2. If you have to deploy this App to the Cloud what services would you use and explain the Architecture

```
1. For the implementation of this architecture on clodu we can use Azure cloud with CDN( Azure CDN standard from microsoft azure). Benefit of using this service is that
it offers dynamic site acceleration via Azure front door service
2. benefits of using microsoft front door is that it accelerates application performance, increases application availability with smart health check probe( it works on layer 7 application protocol)
3. frontdoor is a global service that means once you create this service azure deploys it globally to avoid any downtime

```
## 3. How do you roll out an update without any downtime?
```
1. Azure frontdoor comes with application backend health check probe and load balancing. while setting up azure frontdoor, it asks for latencey of teh request and if that time
passes it will route the request to another server. 
2. In our case, if we want to roll out update. we can start with updating service on load balancer 1, then because of code changes on service, health check of load balancer1 will fail.
but, our appplication will be up and running through load balancer2.
3. After the code upgrade on service under load balancer 1, we should do the application healthcheck and ensure that all the services are up and running also check if load balancer1 is taking the trafffic.
4. After ensuring everything is running fine and Load balancer 1 is taking the traffic,we are good to roll out an update on service under load balancer 2
5. In this way we can keep out application up and running , roll out update without any downtime.
```


